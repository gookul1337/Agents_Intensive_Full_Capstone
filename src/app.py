import os
from flask import Flask, render_template, request, jsonify
from orchestrator import run_agents

# Auto-detect template directory
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")

print("Using templates from:", TEMPLATE_DIR)

app = Flask(__name__, template_folder=TEMPLATE_DIR)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/run', methods=['POST'])
def run():
    data = request.json
    n_agents = int(data.get("num_agents", 3))
    result = run_agents(n_agents)
    return jsonify({"result": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)

