# SystemScope — PC Insights

SystemScope is a lightweight, browser-based system information dashboard. Run a read-only PowerShell scan on your Windows computer, import the generated JSON snapshot, and explore your operating system, processor, memory, storage, network and uptime in one place.

## Live application

https://system-info-monitor.vercel.app

## Getting started

1. Open the live application.
2. Copy the **system scan command** shown on the page.
3. Open Windows PowerShell on the computer you want to inspect.
4. Paste the command and press Enter.
5. Copy the JSON output printed by PowerShell.
6. Return to SystemScope, paste the JSON into the snapshot box, and choose **Analyze my system**.
7. Review the dashboard or export the report as JSON, CSV, or PDF.

The same command is also available in `MASTER_COMMAND.txt`.

## Features

- Operating system, device and processor details
- Installed and available memory
- Disk capacity and usage by drive
- Local IPv4 and active network adapter MAC address
- System uptime and last boot time
- Snapshot import with basic validation
- Sample data for exploring the dashboard
- JSON and CSV export, plus print-to-PDF

## Privacy and security

SystemScope is a static frontend. It does not remotely inspect your computer. The PowerShell command runs locally and collects read-only system details; you choose whether to paste the result into the page. The pasted snapshot is processed in your browser and is not sent to a backend by this application.

Reports may contain device names, local IP addresses and MAC addresses. Review the contents before sharing them.

## Deploy on Vercel

- Framework preset: **Other**
- Build command: leave empty
- Output directory: `.`
- Install command: leave empty

Connect the GitHub repository to Vercel. Pushes to the `main` branch can trigger production deployments.
