import os, argparse, json
from flask import Flask, render_template, request, jsonify, send_from_directory
from orchestrator import Orchestrator

app = Flask(__name__, template_folder=TEMPLATE_DIR), static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/run', methods=['POST'])
def api_run():
    payload = request.json or {}
    query = payload.get('query', 'Summarize Agents Intensive capstone')
    n = int(payload.get('n', 3))
    steps = int(payload.get('steps', 5))
    orch = Orchestrator(n_agents=n)
    timeline = orch.run(query=query, steps=steps)
    return jsonify({'status': 'ok', 'timeline': timeline})

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--port', type=int, default=int(os.environ.get('PORT', 5000)))
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port, debug=True)
