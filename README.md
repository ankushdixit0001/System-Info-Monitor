# SystemPulse

A small, cross-platform system monitoring dashboard built with Python, Flask, psutil, and Chart.js.

Monitor CPU, memory, disk usage, and running processes from a simple local web interface.

## Features
- Live CPU, RAM, and disk usage
- Running process list with PID, status, CPU, and memory
- Search processes by name or PID
- CPU and RAM history charts
- Basic system information
- Windows, Linux, and macOS support through psutil
- Read-only monitoring; no process termination or service modification

## Requirements
- Python 3.9+
- pip

## Run on Windows (PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

## Run on Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000** in your browser and stop the server with Ctrl+C.

## Project structure
```
SystemPulse/
├── app.py
├── monitor.py
├── requirements.txt
├── templates/index.html
├── static/style.css
├── static/app.js
├── README.md
├── LICENSE
└── .gitignore
```

## API
| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/system` | CPU, memory, disk, uptime and system details |
| GET | `/api/processes` | Current process list; optional `?search=` |
| GET | `/api/performance` | Current CPU and memory readings |

## Notes
- The dashboard refreshes every three seconds.
- Some process details may be unavailable due to OS permissions.
- This is a local development application. Do not expose the Flask development server to an untrusted network.
- Chart.js loads from a CDN, so the charts require an internet connection.

## License
MIT. See [LICENSE](LICENSE).
