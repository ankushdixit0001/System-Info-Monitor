from flask import Flask, jsonify, render_template, request
from monitor import get_processes, get_system_info, get_performance

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html")

@app.get("/api/system")
def system():
    return jsonify(get_system_info())

@app.get("/api/processes")
def processes():
    query = request.args.get("search", "").strip().lower()
    items = get_processes()
    if query:
        items = [p for p in items if query in p["name"].lower() or query == str(p["pid"])]
    return jsonify(items)

@app.get("/api/performance")
def performance():
    return jsonify(get_performance())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
