from bs4 import BeautifulSoup
import json

class JsonResponseInterpreter:

    def __init__(self, requestResponse):
        self.requestResponseText = requestResponse.text
        self.parse_json_response()

    def parse_json_response(self):
        self.jsonDict = json.loads(self.requestResponseText)

    def query_json(self, key, value):
        target_records = filter(lambda x: x[key] == value, self.jsonDict)
        return target_records

    def json_tree_traverse(self, tree_traverse_keys):
        tree_traverse_keys = iter(tree_traverse_keys)
        localTree = self.jsonDict.copy()

        def get_next_level(remaining_keys, tree):

            next_level_key = next(remaining_keys, None)
            if next_level_key is None:
                return tree
            else:
                tree = tree[next_level_key]
                return get_next_level(remaining_keys, tree)

        return get_next_level(tree_traverse_keys,localTree)
