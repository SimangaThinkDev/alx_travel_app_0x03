# listings/management/commands/seed.py

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing
import random
from faker import Faker

# Initialize Faker for generating fake data
fake = Faker()
User = get_user_model() # Get the currently active user model

class Command(BaseCommand):
    help = 'Seeds the database with sample Listing data.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--num_listings',
            type=int,
            default=20,
            help='The number of sample listings to create.'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear all existing listings before seeding.'
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database seeding...'))

        num_listings = options['num_listings']
        clear_data = options['clear']

        if clear_data:
            self.stdout.write(self.style.WARNING('Clearing existing listings...'))
            Listing.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('All existing listings cleared.'))

        # Ensure there's at least one user to assign as an owner
        # In a real scenario, you might want to create a dedicated test user
        # or handle cases where no users exist more robustly.
        try:
            owner_user = User.objects.first()
            if not owner_user:
                self.stdout.write(self.style.WARNING('No existing users found. Creating a default owner user.'))
                owner_user = User.objects.create_user(username='seeder_user', email='seeder@example.com', password='seedpassword123')
                self.stdout.write(self.style.SUCCESS(f'Created user: {owner_user.username}'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error getting or creating a user: {e}'))
            self.stderr.write(self.style.ERROR('Seeding aborted. Please ensure you have run makemigrations/migrate for your auth app.'))
            return


        if not owner_user:
            self.stderr.write(self.style.ERROR('Could not find or create an owner user. Aborting seeding.'))
            return

        listings_to_create = []
        for _ in range(num_listings):
            title = fake.sentence(nb_words=random.randint(3, 7)).replace('.', '')
            description = fake.paragraph(nb_sentences=random.randint(3, 7))
            price = round(random.uniform(50.00, 5000.00), 2)

            listing = Listing(
                title=title,
                description=description,
                price=price,
                owner=owner_user, # Assign the owner
            )
            listings_to_create.append(listing)

        Listing.objects.bulk_create(listings_to_create)

        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {len(listings_to_create)} listings.'))
