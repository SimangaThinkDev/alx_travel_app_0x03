from rest_framework import serializers
from .models import Listing, Booking, Review

class ListingSerializer(serializers.ModelSerializer):
    owner_username = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price', 'created_at', 'owner', 'owner_username']
        read_only_fields = ['owner'] # Owner is set by the request.user, not directly by user input

class BookingSerializer(serializers.ModelSerializer):
    listing_title = serializers.ReadOnlyField(source='listing.title')
    booker_username = serializers.ReadOnlyField(source='booker.username')

    class Meta:
        model = Booking
        fields = ['id', 'listing', 'listing_title', 'booker', 'booker_username', 'start_date', 'end_date', 'total_price', 'created_at', 'is_confirmed']
        read_only_fields = ['booker', 'total_price', 'is_confirmed'] # Booker set by request.user, total_price is calculated

    def validate(self, data):
        """
        Check that the start date is before the end date.
        """
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data

    def create(self, validated_data):
        # Automatically set the booker to the current authenticated user
        # This assumes the view is passing the 'request.user' to the serializer context
        if 'request' in self.context and hasattr(self.context['request'], 'user'):
            validated_data['booker'] = self.context['request'].user
        else:
            raise serializers.ValidationError("User not provided for booking creation.")

        # total_price is calculated in the model's save method, no need to set here
        return super().create(validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'listing', 'reviewer', 'rating', 'comment', 'created_at']
        read_only_fields = ['reviewer', 'created_at']