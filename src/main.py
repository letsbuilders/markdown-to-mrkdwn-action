import os
import uuid

from markdown_to_mrkdwn import SlackMarkdownConverter


def remove_comments(line: str) -> str:
    if line.startswith("<!--") and line.endswith("-->"):
        return ""
    return line


def convert(text: str) -> str:
    """convert markdown to mrkdwn and apply all extensions"""
    converter = SlackMarkdownConverter()
    converter.register_plugin(
        name="remove_comments",
        converter_func=remove_comments,
        priority=10,
        scope="line",
        timing="before"
    )
    return converter.convert(text)


def github_output(key, message) -> None:
    """
    save a message to GITHUB_OUTPUT
    use unique delimiters as supported by GitHub
    https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-commands#multiline-strings
    """
    delimiter = str(uuid.uuid4())
    with open(os.environ['GITHUB_OUTPUT'], mode='a', encoding='UTF-8') as fh:
        # the output is going to be reused in a JSON payload so we're encoding it to simplify that
        message_encoded = message.encode("unicode_escape").decode("utf-8")
        print(f'{key}<<{delimiter}', file=fh)
        print(message_encoded, file=fh)
        print(delimiter, file=fh)


def main():
    input_text = os.environ["INPUT_TEXT"]
    output_text = convert(input_text)
    github_output(key='text', message=output_text)


if __name__ == "__main__":
    main()
