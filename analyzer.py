import re
import sys
from collections import Counter

if len(sys.argv) < 2:
    print("Usage: python analyzer.py <logfile>")
    sys.exit(1)

log_file = sys.argv[1]

log_levels = {"INFO": 0, "WARNING": 0, "ERROR": 0}
error_messages = []

with open(log_file, "r") as file:
    for line in file:
        if line.startswith("INFO"):
            log_levels["INFO"] += 1
        elif line.startswith("WARNING"):
            log_levels["WARNING"] += 1
        elif line.startswith("ERROR"):
            log_levels["ERROR"] += 1
            message = re.sub(r"ERROR \d{4}-\d{2}-\d{2} ", "", line).strip()
            error_messages.append(message)

most_common_errors = Counter(error_messages).most_common(3)

with open("report.txt", "w") as report:
    report.write("Log File Analysis Report\n")
    report.write("========================\n\n")
    report.write(f"Analyzed file: {log_file}\n\n")
    report.write(f"INFO messages: {log_levels['INFO']}\n")
    report.write(f"WARNING messages: {log_levels['WARNING']}\n")
    report.write(f"ERROR messages: {log_levels['ERROR']}\n\n")

    report.write("Most Frequent Errors:\n")
    for error, count in most_common_errors:
        report.write(f"- {error} ({count} times)\n")

print("Log analysis completed. Report generated.")
