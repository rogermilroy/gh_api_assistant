import os
from pathlib import Path
from gh_api_assistant.assistant import get_assistant
from pytest import fixture


@fixture
def api_key():
    with open(Path(os.getcwd()) / "gh_api_assistant/api_key.txt", "r") as f:
        api_key = f.read().rstrip()
    return api_key

@fixture
def assistant_chain(api_key):
    return get_assistant(api_key=api_key, collection_name="rest_api_chunked_1000")


def test_chain_success(assistant_chain):

    # assistant_chain.invoke("How can I trigger Github Action through the API?")
    assert assistant_chain.invoke("What are the core resources exposed by the API?") != "I'm afraid I can't answer that question."
    # assistant_chain.invoke("How do I authenticate my requests?")
    # assistant_chain.invoke("What different authentication methods are accepted?")
    # assistant_chain.invoke("What parameters does the search API accept?")
    # assistant_chain.invoke("How can I create a new repository via the API? Provide a sample request/response.")
    # assert assistant_chain.invoke("How can I create a new repository via the API? Provide a sample in python that shows how to do it.") != "I'm afraid I can't answer that question."


def test_chain_unknown(assistant_chain):
    assert assistant_chain.invoke("Where is Ohio?") == "I'm afraid I can't answer that question."
    assert assistant_chain.invoke("What is your name?") == "I'm afraid I can't answer that question."
