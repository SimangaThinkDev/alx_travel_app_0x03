## Django Listing & Booking API

This project is a web application built using Django and Django REST Framework, designed to manage property or service listings, facilitate user bookings for these listings, and enable a review system. It provides a comprehensive set of API endpoints for creating, retrieving, updating, and deleting listings, as well as managing associated bookings and user reviews, making it a flexible backend for a marketplace or booking platform.

---

### **Key Features**

* **User Authentication**: Secure user registration, login, and authentication using Django's built-in user model and Django REST Framework's token-based authentication.
* **Listing Management**: Users can create, view, edit, and delete their own listings. This includes details like title, description, location, price, and availability.
* **Booking System**: A robust booking system allows users to reserve listings for specific dates. The API handles booking creation, management, and status updates (e.g., pending, confirmed, canceled).
* **Review and Rating System**: Users can leave reviews and ratings for listings they have booked. This system helps build trust and provides valuable feedback for both listing owners and prospective users.
* **Permissions**: Granular permission control ensures that only authenticated users can create bookings or reviews, and only listing owners can modify their own listings.
* **API Documentation**: The project includes automatically generated API documentation using a tool like `drf-spectacular`, making it easy for developers to understand and interact with the endpoints.

---

### **Technologies Used**

* **Backend**: Django, Django REST Framework (DRF)
* **Database**: PostgreSQL is the recommended database for production environments, but the project can also use SQLite for local development.
* **API Docs**: `drf-spectacular` for generating OpenAPI/Swagger documentation.
* **Environment Management**: `python-dotenv` for managing environment variables.
* **Testing**: Django's built-in testing framework for unit and integration tests.

---

### **Getting Started**

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

#### **Prerequisites**

You'll need the following installed on your machine:
* **Python**: Version 3.10 or higher.
* **Git**: For cloning the repository.

#### **Installation**

1.  **Clone the repository**:
    ```
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create and activate a virtual environment**:
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

3.  **Install the required packages**:
    ```
    pip install -r requirements.txt
    ```

4.  **Set up environment variables**:
    Create a `.env` file in the root directory and add the following:
    ```
    SECRET_KEY='your-secret-key'
    DEBUG=True
    # Database configuration for PostgreSQL (example)
    # DATABASE_URL=postgres://user:password@host:port/dbname
    ```
    
    *For local development with SQLite, you can omit the database URL.*

5.  **Run migrations**:
    ```
    python manage.py migrate
    ```

6.  **Create a superuser**:
    ```
    python manage.py createsuperuser
    ```

7.  **Run the development server**:
    ```
    python manage.py runserver
    ```

The API will now be running on `http://127.0.0.1:8000`. You can access the browsable API and documentation at this address.

---

### **API Endpoints**

The API follows a RESTful design. Here's a quick overview of the main endpoints.

* **`/api/listings/`**:
    * `GET`: Retrieve a list of all listings.
    * `POST`: Create a new listing (requires authentication).

* **`/api/listings/<id>/`**:
    * `GET`: Retrieve details for a specific listing.
    * `PUT`/`PATCH`: Update a listing (requires ownership).
    * `DELETE`: Delete a listing (requires ownership).

* **`/api/bookings/`**:
    * `GET`: View your own bookings (requires authentication).
    * `POST`: Create a new booking (requires authentication).

* **`/api/reviews/`**:
    * `POST`: Create a new review for a listing (requires authentication and a completed booking).

* **`/api/auth/register/`**:
    * `POST`: Register a new user.

* **`/api/auth/token/`**:
    * `POST`: Obtain an authentication token.

* **`/api/schema/swagger-ui/`**:
    * `GET`: View the interactive API documentation. 

For a full list of endpoints and their request/response schemas, please refer to the OpenAPI documentation.
# alx_travel_app_0x03
