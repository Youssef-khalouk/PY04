import sys

print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

archivist_id = input("Input Stream active. Enter archivist ID: ")
status_report = input("Input Stream active. Enter status report: ")

str = "\n{{[}STANDARD{{]}} Archive status from "
str += f"{archivist_id}: {status_report}\n"

sys.stdout.write(str)

sys.stderr.write(
    "{[}ALERT{]} System diagnostic: Communication channels verified\n"
)

sys.stdout.write("{[}STANDARD{]} Data transmission complete\n")
print("\nThree-channel communication test successful.")
