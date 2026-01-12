#!/usr/bin/python3

filename = "ancient_fragment.txt"

print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
print(f"Accessing Storage Vault: {filename}")

try:
    file = open(filename, "r")
except FileNotFoundError:
    print("ERROR: Storage vault not found. Run data generator first.")
    exit()

print("Connection established...")
print("RECOVERED DATA:")

content = file.read()
print(content, end="")

file.close()
print("Data recovery complete. Storage unit disconnected.")
