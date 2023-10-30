# to retrieve data that we will insert into the vectordb
from itertools import islice
import json
from typing import Dict, Tuple
import requests


def get_rest_api_data(url: str):
    # very simple function that just returns the test found at a
    # webpage.
    response = requests.get(url=url)
    return json.dumps(response.json())


def split_api_data(rest_api_data: dict) -> Tuple[Dict, Dict]:
    # specific to openapi rest API documentation structure
    metadata = {"openapi":rest_api_data["openapi"], "info": rest_api_data["info"], "tags": rest_api_data["tags"], "servers": rest_api_data["servers"], "externalDocs": rest_api_data["externalDocs"]}

    resources = {"paths": rest_api_data["paths"], "x-webhooks": rest_api_data["x-webhooks"], "components": rest_api_data["components"]}

    return metadata, resources


if __name__ == "__main__":
    rest_api_data = get_rest_api_data("https://raw.githubusercontent.com/github/rest-api-description/main/descriptions/api.github.com/api.github.com.json")



    print(f"total length {len(rest_api_data)}")
