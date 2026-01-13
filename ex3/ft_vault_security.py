
print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
print("Initiating secure vault access...")
print("Vault connection established with failsafe protocols\n")

# ---------- SECURE EXTRACTION ----------
print("SECURE EXTRACTION:")

# Read classified data safely
file_name = "classified_data.txt"

try:
    with open(file_name, "r") as vault:
        data = vault.read()
        print("{{[}CLASSIFIED{{]}} Quantum encryption keys recovered")
        print("{{[}CLASSIFIED{{]}} Archive integrity: 100%")
except FileNotFoundError:
    print("{[}CLASSIFIED{]} Warning:", f"{file_name} not found")

# ---------- SECURE PRESERVATION ----------
print("\nSECURE PRESERVATION:")

# Write new information safely
with open("classified_data.txt", "a") as vault:
    vault.write("{[}CLASSIFIED{]} New security protocols archived\n")
    print("{[}CLASSIFIED{]} New security protocols archived")

# Vault automatically sealed
print("Vault automatically sealed upon completion")
print("All vault operations completed with maximum security.")
