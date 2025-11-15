import os
from flask import Flask, render_template, request, jsonify
from orchestrator import Orchestrator

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(os.path.dirname(BASE_DIR), "templates")

app = Flask(__name__, template_folder=TEMPLATE_DIR)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/run", methods=["POST"])
def api_run():
    data = request.json
    query = data.get("query", "")

    orch = Orchestrator()
    result = orch.run(query=query)

    return jsonify({"timeline": result})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print("Using templates from:", TEMPLATE_DIR)
    app.run(host="0.0.0.0", port=port, debug=True)
