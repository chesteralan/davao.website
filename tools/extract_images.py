import os
import re
import glob


def extract_image_urls_from_text(text: str) -> set[str]:
    """
    Extract image URLs from a block of MDX/Markdown/HTML text.
    - Markdown images: ![alt](url "title")
    - HTML <img src="url"> tags
    - Frontmatter line: image: <url>
    """
    urls: set[str] = set()

    # Markdown image syntax
    md_img_pattern = re.compile(r"!\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
    urls.update(md_img_pattern.findall(text))

    # HTML <img> tags
    html_img_pattern = re.compile(r"<img[^>]+src=[\"']([^\"'>]+)[\"']", re.IGNORECASE)
    urls.update(html_img_pattern.findall(text))

    # Frontmatter image field (naive; no YAML parser needed)
    # Consider only the first frontmatter block delimited by --- at the top
    frontmatter_match = re.match(r"^---\n(.*?)\n---\n", text, flags=re.DOTALL)
    if frontmatter_match:
        frontmatter = frontmatter_match.group(1)
        image_line_pattern = re.compile(r"^image:\s*(.+)$", flags=re.MULTILINE)
        for m in image_line_pattern.finditer(frontmatter):
            # Strip quotes if present
            val = m.group(1).strip().strip('"').strip("'")
            # If YAML list or object, skip (we expect a single URL string)
            if not val.startswith('[') and not val.startswith('{'):
                urls.add(val)

    return urls


def collect_image_urls(search_dir: str) -> list[str]:
    pattern = os.path.join(search_dir, "**", "*.mdx")
    files = glob.glob(pattern, recursive=True)
    all_urls: set[str] = set()

    for file_path in files:
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
            urls = extract_image_urls_from_text(content)
            all_urls.update(urls)
        except Exception as e:
            # Skip unreadable files but continue processing
            print(f"Warning: failed to read {file_path}: {e}")

    return sorted(all_urls)


def write_urls_to_file(urls: list[str], output_file: str) -> None:
    with open(output_file, "w", encoding="utf-8") as f:
        for url in urls:
            f.write(f"{url}\n")


def main() -> None:
    # Script directory and project root
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.abspath(os.path.join(script_dir, ".."))

    posts_dir = os.path.join(project_root, "src", "data", "post")
    output_file = os.path.join(project_root, "images.txt")

    urls = collect_image_urls(posts_dir)
    write_urls_to_file(urls, output_file)

    print(f"Extracted {len(urls)} unique image URL(s). Saved to {output_file}")


if __name__ == "__main__":
    main()

