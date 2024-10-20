import React, { useState } from "react";
import axios from "axios";

function RuleEvaluator() {
  const [ruleString, setRuleString] = useState("");
  const [ast, setAst] = useState(null);
  const [data, setData] = useState("");
  const [result, setResult] = useState(null);

  const handleCreateRule = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/create_rule", {
        rule_string: ruleString,
      });
      setAst(response.data.ast);
    } catch (error) {
      console.error(error);
    }
  };

  const handleEvaluateRule = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:5000/evaluate_rule", {
        ast: ast,
        data: JSON.parse(data),
      });
      setResult(response.data.result);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h2>Create Rule</h2>
      <textarea
        value={ruleString}
        onChange={(e) => setRuleString(e.target.value)}
        placeholder="Enter rule string"
      />
      <button onClick={handleCreateRule}>Create Rule</button>

      {ast && (
        <div>
          <h3>AST:</h3>
          <pre>{JSON.stringify(ast, null, 2)}</pre>
        </div>
      )}

      <h2>Evaluate Rule</h2>
      <textarea
        value={data}
        onChange={(e) => setData(e.target.value)}
        placeholder='Enter JSON data for evaluation (e.g., {"key": "value"})'
      />
      <button onClick={handleEvaluateRule}>Evaluate Rule</button>

      {result !== null && (
        <div>
          <h3>Result:</h3>
          <p>{result.toString()}</p>
        </div>
      )}
    </div>
  );
}

export default RuleEvaluator;
