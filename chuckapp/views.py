from .models import Joke
from .serializer import JokeSerializer
from rest_framework import viewsets

class JokeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows jokes to be viewed.
    """
    queryset = Joke.objects.all()
    serializer_class = JokeSerializer