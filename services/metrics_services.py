import psutil
def get_system_metrics():
    """
    This API checks the metrics of CPU and Memory usage.
    It returns the current CPU and Memory usage percentages.
    It also checks if the CPU usage is above a certain threshold and returns a status message accordingly.
    """
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    memory_usage = memory_info.percent

    cpu_threshold = 10

    status = "High CPU Usage" if cpu_usage > cpu_threshold else "Normal CPU Usage"
    
    return {
        "cpu_usage_percent": cpu_usage,
        "memory_usage_percent": memory_usage,
        "cpu_threshold_percent": cpu_threshold,
        "status": status
    }