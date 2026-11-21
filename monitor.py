"""Read-only, cross-platform system metrics using psutil."""
import platform
import socket
import time
import psutil

BOOT_TIME = psutil.boot_time()

def get_system_info():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")
    return {
        "cpu_percent": psutil.cpu_percent(interval=0.1),
        "memory_percent": memory.percent,
        "memory_total": memory.total,
        "memory_used": memory.used,
        "memory_available": memory.available,
        "disk_percent": disk.percent,
        "uptime_seconds": max(0, int(time.time() - BOOT_TIME)),
        "os": f"{platform.system()} {platform.release()}",
        "hostname": socket.gethostname(),
        "cpu_cores": psutil.cpu_count(logical=True) or 0,
        "python_version": platform.python_version(),
    }

def get_processes():
    result = []
    attrs = ["pid", "name", "username", "status", "memory_percent", "cpu_percent"]
    for proc in psutil.process_iter(attrs=attrs, ad_value=None):
        try:
            info = proc.info
            result.append({
                "pid": info.get("pid"),
                "name": info.get("name") or "Unknown",
                "status": info.get("status") or "Unknown",
                "cpu_percent": round(info.get("cpu_percent") or 0.0, 1),
                "memory_percent": round(info.get("memory_percent") or 0.0, 2),
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    result.sort(key=lambda item: item["memory_percent"], reverse=True)
    return result

def get_performance():
    return {
        "cpu_percent": psutil.cpu_percent(interval=None),
        "memory_percent": psutil.virtual_memory().percent,
        "timestamp": int(time.time()),
    }
