# Github API Assistant

The purpose of this project is to provide an easier inteface into githubs REST API than the
documentation. In this case a conversational interface.

## Getting Started

There are only a couple of steps to using the github API assistant:

1. Clone the repo
2. cd into project root ```cd gh_api_assistant```
3. Install the dependencies.
    1. If using poetry: ```poetry install```
    2. If using pip: ```python -m venv env; source env/bin/activate; pip install -r requirements.txt```
4. cd into sources root ```cd gh_api_assistant```
5. Add an OpenAI api key to <repo_root>/gh_api_assistant/api_key.txt.
6. Run the main file: ```poetry run python main.py``` or ```python main.py```

Please note that you may need to use ```python3``` and ```pip3``` in place of ```python``` and ```pip``` depending on your OS and python setup.

This will prompt you to input your question. Please note that the curernt iteration only supports single questions, not conversation so each question will not reference previous questions or answers.

To stop the assistant use Ctrl + C at the prompt.

## Feedback and Issues

Please feel free to leave problems and issues (or recommnendations and ideas) in the Issues section. No guarantees that I will see and respond but I will do my best to take a look and help when I can.
