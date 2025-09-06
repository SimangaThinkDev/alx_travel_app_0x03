# listings/views.py
from rest_framework import viewsets
from .models import Listing, Booking, Review
from .serializers import ListingSerializer, BookingSerializer, ReviewSerializer
from rest_framework.response import Response
from . import tasks

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
        from_email = request.POST.get("from_email", "")
        tasks.send_confirmation_email.delay( from_email )
        return Response( serializer.data )

class ReviewViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = Review.objects.all()
        serializer = ReviewSerializer(queryset, many=True)
        return Response(serializer.data)