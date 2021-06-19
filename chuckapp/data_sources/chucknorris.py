import requests, json

class ChuckNorris:
    @property
    def base_url(self):
        return "https://api.chucknorris.io/"

    def get_random_joke(self):
        request = requests.get(self.base_url + "jokes/random")
        return request.json()['value']
