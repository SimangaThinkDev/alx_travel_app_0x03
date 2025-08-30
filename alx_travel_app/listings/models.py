from django.db import models
from django.conf import settings # Import settings to reference AUTH_USER_MODEL
from django.core.validators import MinValueValidator, MaxValueValidator

class Listing(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    # Assuming a listing is created by a user
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings')


    def __str__(self):
        return self.title

class Booking(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='bookings')
    booker = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings_made')
    start_date = models.DateField()
    end_date = models.DateField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False) # Calculated field
    created_at = models.DateTimeField(auto_now_add=True)
    is_confirmed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('listing', 'start_date', 'end_date') # Prevent duplicate bookings for the same listing and dates

    def save(self, *args, **kwargs):
        # Calculate total price before saving
        if not self.total_price: # Only calculate if not already set (e.g., during creation)
            if self.start_date and self.end_date and self.listing.price:
                duration_days = (self.end_date - self.start_date).days + 1 # Include both start and end day
                self.total_price = self.listing.price * duration_days
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking for {self.listing.title} by {self.booker.username} from {self.start_date} to {self.end_date}"


class Review(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews_given')
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text="Rating must be between 1 and 5."
    )
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('listing', 'reviewer') # One review per listing per user
        ordering = ['-created_at'] # Order reviews by most recent first

    def __str__(self):
        return f"Review for {self.listing.title} by {self.reviewer.username} - Rating: {self.rating}"