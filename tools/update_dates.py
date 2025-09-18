import os
from datetime import datetime, timedelta

# Read the list of files from the temporary file
with open('temp_file_list.txt', 'r') as f:
    files = [line.strip() for line in f.readlines()]

# Starting date
start_date = datetime(2025, 9, 18)

# Iterate over the files and update the publishDate
for i, file_path in enumerate(files):
    # Calculate the new date
    new_date = start_date + timedelta(days=i * 5)
    new_date_str = new_date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')

    # Read the file content
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Find and replace the publishDate
    for j, line in enumerate(lines):
        if line.startswith('publishDate:'):
            lines[j] = f"publishDate: {new_date_str}\n"
            break

    # Write the updated content back to the file
    with open(file_path, 'w') as f:
        f.writelines(lines)

print(f"Updated {len(files)} files.")
