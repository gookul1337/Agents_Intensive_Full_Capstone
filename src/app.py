import os
from flask import Flask, render_template, request, jsonify
from orchestrator import Orchestrator

# Absolute path to templates
TEMPLATE_DIR = "/home/gookul1337/Agents_Intensive_Full_Capstone/templates"
print("Using templates from:", TEMPLATE_DIR)

app = Flask(__name__, template_folder=TEMPLATE_DIR)

# ---------------------------
# FRONTEND PAGE
# ---------------------------
@app.route("/")
def index():
    return render_template("index.html")


# ---------------------------
# MAIN API ENDPOINT
# ---------------------------
@app.route("/api/run", methods=["POST"])
def api_run():
    try:
        data = request.json
        query = data.get("query", "")

        orch = Orchestrator()
        timeline = orch.run(query=query)

        return jsonify({"timeline": timeline})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ---------------------------
# RUN SERVER
# ---------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
