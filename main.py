from flask import Flask, request, jsonify, render_public
from flask_cors import CORS
from database import Database
from rules import create_rule, combine_rules, evaluate_rule

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
db = Database()

@app.route('/')
def index():
    return render_public('index.html')

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    try:
        data = request.get_json()
        rule_string = data.get('rule_string')

        if not rule_string:
            return jsonify({'error': 'No rule string provided'}), 400

        ast = create_rule(rule_string)

        if ast is None:
            return jsonify({'error': 'Invalid rule syntax'}), 400

        return jsonify({'message': 'Rule created successfully', 'ast': ast}), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    rules = request.json.get('rules', [])
    combined_ast = combine_rules(rules)
    return jsonify({'message': 'Rules combined successfully', 'ast': combined_ast}), 200

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    ast = request.json.get('ast')
    data = request.json.get('data', {})
    result = evaluate_rule(ast, data)
    return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run(debug=True)

