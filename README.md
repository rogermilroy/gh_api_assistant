# Github API Assistant

The purpose of this project is to provide an easier inteface into githubs REST API than the
documentation. In this case a conversational interface.

## Getting Started

There are only a couple of steps to using the github API assistant:

1. Clone the repo
2. Add an OpenAI api key to a text file in <repo_root>/gh_api_assistant/api_key.txt.
3. Run the main file eg.

```bash
python3 main.py
```

This will prompt you to input your question. Please note that the curernt iteration only supports single questions, not conversation so each question will not reference previous questions or answers.

To stop the assistant use Ctrl + C at the prompt.
