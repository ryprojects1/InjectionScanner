import datetime
def log_security(file_scanned, score, threats):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #saves a permanent record of the scan with a timestamp

    with open("security_audit.log", "a") as log_file:
        log_file.write(f"[{timestamp}] SCAN COMPLETED: {file_scanned}\n")
        log_file.write(f"RISK SCORE: {score}\n")
        log_file.write(f"THREATS: {', '.join(threats) if threats else 'None'}\n")
        log_file.write("-" * 30 + "\n")
    print(f" Event logged to security_audit.log")