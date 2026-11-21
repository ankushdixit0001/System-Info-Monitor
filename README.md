# SystemScope — PC Insights

SystemScope is a lightweight, browser-based system information dashboard for Windows, macOS and Linux (including Ubuntu). Run a read-only scan locally, import the generated JSON snapshot, and explore your operating system, processor, memory, storage, network and uptime in one place.

## Live application

https://system-info-monitor.vercel.app

## Getting started

1. Open the live application.
2. Select your operating system: Windows, macOS or Ubuntu / Linux.
3. Copy the matching scan command shown on the page.
4. Run it in PowerShell (Windows) or Terminal (macOS / Linux).
5. Copy the JSON output and paste it into SystemScope.
6. Choose **Analyze my system** to view the report.
7. Export your report as JSON, CSV or PDF if needed.

macOS and Ubuntu/Linux commands use Python 3. Ubuntu normally includes Python 3. On macOS, install Python 3 if it is not already available.

## Features

- Windows, macOS and Linux scan instructions
- Operating system, device and processor details
- Installed and available memory
- Disk capacity and usage
- Local IPv4 and network adapter MAC address
- System uptime and last boot time
- Snapshot import with validation
- Sample data for exploring the dashboard
- JSON and CSV export, plus print-to-PDF

## Privacy and security

SystemScope is a static frontend. It does not remotely inspect your computer. The scan command runs locally and collects read-only system details; you choose whether to paste the result into the page. The pasted snapshot is processed in your browser and is not sent to a backend by this application.

Reports may contain device names, local IP addresses and MAC addresses. Review the contents before sharing them.

## Deploy on Vercel

- Framework preset: **Other**
- Build command: leave empty
- Output directory: `. ` (repository root; configure as `.`)
- Install command: leave empty

Connect the GitHub repository to Vercel. Pushes to the `main` branch can trigger production deployments.
