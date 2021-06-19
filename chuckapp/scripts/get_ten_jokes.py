from chuckapp.models import Joke
from chuckapp.data_sources.chucknorris import ChuckNorris

def get_ten_jokes():
    Joke.objects.all().delete()
    for x in range(10):
        joke = ChuckNorris().get_random_joke()
        joke_instance = Joke()
        joke_instance.content = joke
        joke_instance.save()

def run():
    get_ten_jokes()