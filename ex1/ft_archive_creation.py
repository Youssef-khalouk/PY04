
print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")
file_name = "new_discovery.txt"
try:
    print("Initializing new storage unit:", file_name)
    file = open(file_name, "w")
    print("Storage unit created successfully...\n")

    print("Inscribing preservation data...")

    data_1 = "{[}ENTRY 001{]} New quantum algorithm discovered\n"
    file.write(data_1)
    print(data_1, end="")

    data_2 = "{[}ENTRY 002{]} Efficiency increased by 347%\n"
    file.write(data_2)
    print(data_2, end="")

    data_3 = "{[}ENTRY 003{]} Archived by Data Archivist trainee\n"
    file.write(data_3)
    print(data_3, end="")

    print("\nData inscription complete. Storage unit sealed.")
    print(f"Archive '{file_name}' ready for long-term preservation.")

    file.close()

except FileNotFoundError as e:
    print("Error:", e)
