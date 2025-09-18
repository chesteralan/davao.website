import os

# Read the list of files from the temporary file
with open('temp_file_list.txt', 'r') as f:
    files = [line.strip() for line in f.readlines()]

# Iterate over the files and update the excerpt
for file_path in files:
    with open(file_path, 'r') as f:
        lines = f.readlines()

    title = None
    excerpt_index = -1
    excerpt_line = None

    for i, line in enumerate(lines):
        if line.startswith('title:'):
            title = line.split('title:')[1].strip()
        if line.startswith('excerpt:'):
            excerpt_index = i
            excerpt_line = line

    if excerpt_line and 'Content for ' in excerpt_line:
        if title:
            lines[excerpt_index] = f'excerpt: --no-excerpt--\n'
            with open(file_path, 'w') as f:
                f.writelines(lines)

print(f"Updated excerpts for {len(files)} files.")