import os
from pathlib import Path


from langchain.globals import set_verbose, set_debug

from gh_api_assistant.assistant import get_assistant

set_debug(False)
set_verbose(False)


def run_assistant():
    with open(Path(os.getcwd()) / "gh_api_assistant/api_key.txt", "r") as f:
        api_key = f.read().rstrip()

    assistant_chain = get_assistant(api_key=api_key, collection_name="rest_api_chunked_1000")
    print("Welcome to the Github REST API assistant. Please note that I can only answer questions"
          "based on the openapi specification for the API.")
    while True:
        user_input = input("Please ask your question here:\n>")
        print(assistant_chain.invoke(user_input))


if __name__ == "__main__":
    run_assistant()
