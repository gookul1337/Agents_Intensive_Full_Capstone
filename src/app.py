import os
from flask import Flask, render_template, request, jsonify
from orchestrator import run_agents

# ABSOLUTE PATH TO YOUR TEMPLATE FOLDER
TEMPLATE_DIR = "/home/gookul1337/Agents_Intensive_Full_Capstone/templates"

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

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
