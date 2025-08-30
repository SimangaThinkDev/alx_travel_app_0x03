# listings/views.py

from rest_framework import viewsets
from .models import Listing, Booking
from .serializers import ListingSerializer, BookingSerializer
from rest_framework.response import Response

class ListingViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing listings.
    """
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer

    def list_all(self, request):
        serializer = ListingSerializer( self.queryset, many=True )
        return Response( serializer.data )
    

class BookingViewSet( viewsets.ModelViewSet ):
    """
    A simple viewset for viewing bookings
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def booking_view( self, request ):
        serializer = BookingSerializer( self.queryset )
        return Response( serializer.data )

"""
class UserViewSet(viewsets.ViewSet):
    \"""
    A simple ViewSet for listing or retrieving users.
    \"""
    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
"""