from flask import Flask, request, jsonify, render_template
from orchestrator import Orchestrator

app = Flask(__name__, template_folder="../templates")
orc = Orchestrator()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/run", methods=["POST"])
def api_run():
    data = request.get_json()
    query = data.get("query", "")
    timeline = orc.run(query)
    return jsonify({"timeline": timeline})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
