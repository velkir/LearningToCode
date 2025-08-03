import requests
import json

class Trello:
    def __init__(self, public_key, token):
        self.public_key = public_key
        self.token = token

    def _get_json_cards_from_list(self, list_id):
        url = f"https://api.trello.com/1/lists/{list_id}/cards"
        headers = {
            "Accept": "application/json"
        }
        query = {
            'key': self.public_key,
            'token': self.token
        }
        response = requests.request(
            "GET",
            url,
            headers=headers,
            params=query
        )
        return json.loads(response.text)

    def get_card_names_from_list(self, list_id):
        json_str = self._get_json_cards_from_list(list_id)
        card_names = [card["name"] for card in json_str]
        return card_names