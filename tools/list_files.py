
import os
import sys
import glob

def find_files_with_no_excerpt(output_file):
    # Get the absolute path of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Get the absolute path of the project root
    project_root = os.path.abspath(os.path.join(script_dir, '..'))
    # Construct the search path for the mdx files
    search_path = os.path.join(project_root, 'src', 'data', 'post', '**', '*.mdx')

    # Find all mdx files recursively
    files = glob.glob(search_path, recursive=True)

    # Filter files that contain '--no-excerpt--'
    files_with_no_excerpt = []
    for file_path in files:
        with open(file_path, 'r') as f:
            if '--no-excerpt--' in f.read():
                files_with_no_excerpt.append(file_path)

    # Write the list of files to the output file
    with open(output_file, 'w') as f:
        for file_path in files_with_no_excerpt:
            f.write(f"{file_path}\n")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        output_file = sys.argv[1]
        find_files_with_no_excerpt(output_file)
        print(f"Found {len(open(output_file).readlines())} files with no excerpt. The list of files is saved in {output_file}")
    else:
        print("Please provide an output file name as a command-line argument.")
