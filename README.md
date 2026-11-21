# SystemScope — Lab 16 System Information & Resource Check

A static browser dashboard for the Lab 16 practical. Run the one-line PowerShell master command locally on your Windows PC, paste its JSON output into the webpage, and inspect OS, CPU, RAM, disk, network and uptime.

## Deploy to Vercel
- Framework preset: Other
- Build command: leave empty
- Output directory: `.` (repository root)
- Install command: leave empty

Connect this repository in Vercel. Every push to `main` can trigger a deployment.

## Use
1. Open `MASTER_COMMAND.txt`.
2. Copy the complete PowerShell one-liner and run it in Windows PowerShell.
3. Copy the JSON output.
4. Open the hosted webpage, paste the output and click **Analyze my system**.
5. Download JSON/CSV or use Print → Save as PDF.

## Privacy and architecture
This is a static, client-side webpage. Pasted JSON is parsed in the visitor's browser; no server endpoint receives it. The hosted webpage cannot inspect the visitor's machine directly. The master command must be run locally by the student.

The command uses read-only CIM and network queries. Avoid sharing exported reports publicly because they may contain local IP and MAC addresses.

## Lab GUI cross-checks
- OS / hostname: Settings → System → About
- CPU / RAM / uptime: Task Manager → Performance
- Disk: File Explorer → This PC
- IP: Settings → Network & Internet
