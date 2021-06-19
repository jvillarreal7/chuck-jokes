from .models import Quote
from .serializer import QuoteSerializer
from rest_framework import viewsets

class QuoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows quotes to be viewed.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer