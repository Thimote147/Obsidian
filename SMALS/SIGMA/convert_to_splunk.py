#!/usr/bin/env python3
"""
Sigma to Splunk Converter
Converts Sigma YAML rules to Splunk queries using pipeline transformations
"""

import yaml
import sys
import os
from pathlib import Path
from typing import Dict, List, Any


class SigmaToSplunkConverter:
    def __init__(self, pipeline_file: str):
        """Initialize converter with pipeline configuration"""
        self.pipeline = self._load_pipeline(pipeline_file)
        self.transformations = self.pipeline.get('transformations', [])
    
    def _load_pipeline(self, pipeline_file: str) -> Dict:
        """Load pipeline configuration from YAML file"""
        with open(pipeline_file, 'r') as f:
            return yaml.safe_load(f)
    
    def _load_rule(self, rule_file: str) -> Dict:
        """Load Sigma rule from YAML file"""
        with open(rule_file, 'r') as f:
            return yaml.safe_load(f)
    
    def _apply_field_mappings(self, rule: Dict) -> Dict:
        """Apply field name mappings from pipeline"""
        for transform in self.transformations:
            if transform.get('type') == 'field_name_mapping':
                mapping = transform.get('mapping', {})
                rule_conditions = transform.get('rule_conditions', [])
                
                # Check if this mapping applies to the rule
                if self._matches_rule_conditions(rule, rule_conditions):
                    rule = self._apply_mapping(rule, mapping)
        return rule
    
    def _matches_rule_conditions(self, rule: Dict, conditions: List[Dict]) -> bool:
        """Check if rule matches the specified conditions"""
        logsource = rule.get('logsource', {})
        
        for condition in conditions:
            if condition.get('type') == 'logsource':
                for key, value in condition.items():
                    if key != 'type' and logsource.get(key) == value:
                        return True
        return False
    
    def _apply_mapping(self, rule: Dict, mapping: Dict) -> Dict:
        """Apply field name mapping to rule detection"""
        detection = rule.get('detection', {})
        
        def map_fields(obj):
            if isinstance(obj, dict):
                new_dict = {}
                for key, value in obj.items():
                    # Map field names
                    new_key = mapping.get(key, key)
                    new_dict[new_key] = map_fields(value)
                return new_dict
            elif isinstance(obj, list):
                return [map_fields(item) for item in obj]
            else:
                return obj
        
        rule['detection'] = map_fields(detection)
        return rule
    
    def _get_index_for_rule(self, rule: Dict) -> str:
        """Determine the index pattern based on logsource"""
        logsource = rule.get('logsource', {})
        
        for transform in self.transformations:
            if transform.get('type') == 'add_condition':
                rule_conditions = transform.get('rule_conditions', [])
                if self._matches_rule_conditions(rule, rule_conditions):
                    index = transform.get('conditions', {}).get('index', 'main')
                    return index
        
        return 'main'
    
    def _build_splunk_search(self, detection: Dict, logsource: Dict) -> str:
        """Build Splunk SPL query from detection section"""
        conditions = []
        filter_conditions = []
        
        # Process each detection item
        for key, value in detection.items():
            if key == 'condition':
                continue
            elif key.startswith('selection'):
                conditions.append(self._build_condition(value))
            elif key.startswith('filter'):
                filter_conditions.append(self._build_condition(value))
        
        # Combine conditions
        search_parts = []
        if conditions:
            if len(conditions) > 1:
                search_parts.append(f"({' OR '.join(conditions)})")
            else:
                search_parts.append(conditions[0])
        
        if filter_conditions:
            for filter_cond in filter_conditions:
                search_parts.append(f"NOT ({filter_cond})")
        
        return ' '.join(search_parts)
    
    def _build_condition(self, condition: Dict) -> str:
        """Build a single condition for Splunk"""
        parts = []
        
        for field, values in condition.items():
            if '|' in field:
                # Handle field modifiers (e.g., contains, all, etc.)
                field_name, *modifiers = field.split('|')
                
                if 'contains' in modifiers:
                    if 'all' in modifiers:
                        # All values must be present
                        if isinstance(values, list):
                            for val in values:
                                parts.append(f'{field_name}=*{val}*')
                    else:
                        # Any value can match
                        if isinstance(values, list):
                            value_parts = [f'{field_name}=*{val}*' for val in values]
                            parts.append(f"({' OR '.join(value_parts)})")
                        else:
                            parts.append(f'{field_name}=*{values}*')
                else:
                    # Default behavior
                    if isinstance(values, list):
                        value_parts = [f'{field_name}="{val}"' for val in values]
                        parts.append(f"({' OR '.join(value_parts)})")
                    else:
                        parts.append(f'{field_name}="{values}"')
            else:
                # Simple field matching
                if isinstance(values, list):
                    value_parts = [f'{field}="{val}"' for val in values]
                    parts.append(f"({' OR '.join(value_parts)})")
                else:
                    parts.append(f'{field}="{values}"')
        
        return ' '.join(parts)
    
    def convert(self, rule_file: str) -> Dict[str, str]:
        """Convert a Sigma rule to Splunk query"""
        # Load the rule
        rule = self._load_rule(rule_file)
        
        # Apply field mappings
        rule = self._apply_field_mappings(rule)
        
        # Get index
        index = self._get_index_for_rule(rule)
        
        # Build Splunk search
        detection = rule.get('detection', {})
        logsource = rule.get('logsource', {})
        search_query = self._build_splunk_search(detection, logsource)
        
        # Build complete Splunk query
        splunk_query = f'index={index} {search_query}'
        
        return {
            'title': rule.get('title', 'Untitled'),
            'id': rule.get('id', ''),
            'description': rule.get('description', ''),
            'index': index,
            'query': splunk_query,
            'level': rule.get('level', 'medium'),
            'tags': rule.get('tags', []),
            'author': rule.get('author', ''),
            'date': rule.get('date', '')
        }


def main():
    if len(sys.argv) < 2:
        print("Usage: python convert_to_splunk.py <rule.yml> [pipeline.yml]")
        print("Example: python convert_to_splunk.py test1.yml pipeline.yml")
        sys.exit(1)
    
    rule_file = sys.argv[1]
    pipeline_file = sys.argv[2] if len(sys.argv) > 2 else 'pipeline.yml'
    
    if not os.path.exists(rule_file):
        print(f"Error: Rule file '{rule_file}' not found")
        sys.exit(1)
    
    if not os.path.exists(pipeline_file):
        print(f"Error: Pipeline file '{pipeline_file}' not found")
        sys.exit(1)
    
    # Convert the rule
    converter = SigmaToSplunkConverter(pipeline_file)
    result = converter.convert(rule_file)
    
    # Generate output filename
    output_file = Path(rule_file).stem + '.spl'
    
    # Write to .spl file
    with open(output_file, 'w') as f:
        f.write(f"# Title: {result['title']}\n")
        f.write(f"# ID: {result['id']}\n")
        f.write(f"# Description: {result['description']}\n")
        f.write(f"# Level: {result['level']}\n")
        f.write(f"# Author: {result['author']}\n")
        f.write(f"# Date: {result['date']}\n")
        f.write(f"# Tags: {', '.join(result['tags'])}\n")
        f.write(f"# Index: {result['index']}\n")
        f.write(f"#\n")
        f.write(f"# Splunk Query:\n")
        f.write(f"{result['query']}\n")
    
    # Display results
    print("=" * 80)
    print(f"Title: {result['title']}")
    print(f"ID: {result['id']}")
    print(f"Description: {result['description']}")
    print(f"Level: {result['level']}")
    print(f"Author: {result['author']}")
    print(f"Date: {result['date']}")
    print(f"Tags: {', '.join(result['tags'])}")
    print("=" * 80)
    print(f"\nIndex: {result['index']}")
    print(f"\nSplunk Query:\n{result['query']}")
    print("=" * 80)
    print(f"\n✓ Splunk query saved to: {output_file}")


if __name__ == '__main__':
    main()
