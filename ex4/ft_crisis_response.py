def crisis_handler(file_name) -> None:
    """Handles critical file access errors and maintains system stability."""
    try:
        with open(file_name, "r") as file:
            print(f"ROUTINE ACCESS: Attempting access to '{file_name}'...")
            content = file.read()
            print(f"SUCCESS: Archive recovered - ``{content}''")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")

    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")

    except Exception:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")
    finally:
        print("")


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    crisis_handler("lost_archive.txt")
    crisis_handler("classified_vault.txt")
    crisis_handler("standard_archive.txt")

    print("All crisis scenarios handled successfully. Archives secure.")
