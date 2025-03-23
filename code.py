import sys

def process_log():
    total_uploads = 0
    total_deletions = 0
    storage_used = 0
    largest_file = ("", 0)
    uploaded_files = {}

    # Read input from stdin
    lines = sys.stdin.read().strip().split("\n")

    for line in lines:
        parts = line.strip().split()

        # Skip empty lines
        if not parts or len(parts) < 3:
            continue

        action = parts[2]

        if action == "UPLOAD" and len(parts) == 5:
            filename, size = parts[3], int(parts[4])
            uploaded_files[filename] = size
            storage_used += size
            total_uploads += 1

            if size > largest_file[1]:
                largest_file = (filename, size)

        elif action == "DELETE" and len(parts) == 4:
            filename = parts[3]
            if filename in uploaded_files:
                storage_used -= uploaded_files[filename]
                del uploaded_files[filename]
            total_deletions += 1

    # Print output in the required format
    print(f"Total Uploads: {total_uploads}")
    print(f"Total Deletions: {total_deletions}")
    print(f"Largest File Uploaded: {largest_file[0]} ({largest_file[1]} MB)")
    print(f"Total Storage Used: {storage_used} MB")

# Execute function
process_log()
