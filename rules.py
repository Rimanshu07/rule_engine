import re

class ASTNode:
    def __init__(self, node_type, value=None):
        self.node_type = node_type
        self.value = value

    def to_dict(self):
        return {'node_type': self.node_type, 'value': self.value}

def create_rule(rule_string):
    tokens = re.split(r'(\s+|\(\s*|\s*\)|&&|\|\|)', rule_string)
    # Add logic to parse tokens and create AST
    # This is a simple example; you should implement proper parsing
    return ASTNode('example', 'parsed_rule')

def combine_rules(rules):
    # Logic to combine multiple rules into one AST
    return ASTNode('combined', rules)

def evaluate_rule(ast, data):
    # Example evaluation logic
    return True  # Replace with actual evaluation logic
 
