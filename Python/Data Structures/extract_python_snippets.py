import re
import textwrap


def extract_python_code_from_md_with_summary(file_path):
    """
    Extracts all Python code snippets from a Markdown file with their <summary> fields.

    Args:
        file_path (str): Path to the Markdown (.md) file.

    Returns:
        List[Tuple[str, str]]: A list of tuples where each tuple contains the summary (if present)
        and the Python code snippet.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Regular expression to match <summary> fields and Python code snippets
    pattern = r"<summary>(.*?)</summary>\s*```python\n(.*?)```"
    matches = re.findall(pattern, content, re.DOTALL)

    # Remove extra indentations for each snippet
    cleaned_snippets = [
        (textwrap.dedent(summary.strip()), textwrap.dedent(snippet))
        for summary, snippet in matches
    ]
    return cleaned_snippets


def save_snippets_with_summary(snippets, output_file="all_snippets.py"):
    """
    Saves all extracted Python snippets with their summaries as comments into a single Python file.

    Args:
        snippets (List[Tuple[str, str]]): List of tuples with summaries and Python code snippets.
        output_file (str): File name where all snippets will be saved.
    """
    with open(output_file, "w", encoding="utf-8") as f:
        for idx, (summary, snippet) in enumerate(snippets, start=1):
            f.write(f"# Snippet {idx}\n")
            if summary:
                f.write(f"# Summary: {summary}\n")
            else:
                f.write("# Summary: None\n")
            f.write(snippet)
            f.write("\n\n")
        print(f"All snippets with summaries saved to: {output_file}")


# Example usage
md_file = "Python_Data_Structures_Algorithms_expanded_V7.md"  # Replace with your .md file path
python_snippets_with_summaries = extract_python_code_from_md_with_summary(md_file)

print(f"Found {len(python_snippets_with_summaries)} Python code snippets.")
for idx, (summary, snippet) in enumerate(python_snippets_with_summaries, start=1):
    print(f"Snippet {idx} Summary: {summary}\nCode:\n{snippet}\n{'-'*40}")

# Save all snippets with summaries to a single Python file
save_snippets_with_summary(python_snippets_with_summaries)
