from markdown_to_mrkdwn import SlackMarkdownConverter
import os


def remove_comments(line):
    if line.startswith("<!--"):
        return ""
    return line


def convert(text: str) -> str:
    converter = SlackMarkdownConverter()
    converter.register_plugin(
        name="remove_comments",
        converter_func=remove_comments,
        priority=10,
        scope="line",
        timing="before"
    )
    return converter.convert(text)

def main():
    input_text = os.environ["INPUT_TEXT"]
    output_text = convert(input_text)

    github_output = os.environ["GITHUB_OUTPUT"]

    with open(github_output, "w") as f:
        f.write(f'text={output_text}')


if __name__ == "__main__":
    main()