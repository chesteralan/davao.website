import os

# Read the list of files from the temporary file
with open('temp_file_list.txt', 'r') as f:
    files = [line.strip() for line in f.readlines()]

# Iterate over the files and update the excerpt
for file_path in files:
    with open(file_path, 'r') as f:
        lines = f.readlines()

    image_index = -1
    image_line = None

    for i, line in enumerate(lines):
        if line.startswith('image:'):
            image_index = i
            image_line = line

    if image_line and 'placeholder.jpeg' in image_line:
        lines[image_index] = 'image: https://cdn.davao.website/placeholder.jpeg\n'
        with open(file_path, 'w') as f:
            f.writelines(lines)

print(f"Updated images for {len(files)} files.")