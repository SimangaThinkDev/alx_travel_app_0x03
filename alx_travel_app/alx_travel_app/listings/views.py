# listings/views.py

from rest_framework import viewsets
from .models import Listing
from .serializers import ListingSerializer

class ListingViewSet(viewsets.ModelViewSet): # <--- This class name
    """
    A simple ViewSet for viewing and editing listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

