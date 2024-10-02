# NexusWash - Car Wash Management System

## Project Overview

NexusWash is a web-based car wash management system built using Django. It allows users to book car wash services, purchase detailing products, and manage their profiles. The system also includes an admin interface for managing bookings, products, and user accounts.

## Features

### User Features
- **User Registration & Authentication**: Users can register for an account, log in, and log out.
- **Profile Management**: Users can view and edit their profile information.
- **Service Booking**: Users can book car wash services, ensuring no double bookings occur.
- **Cart Functionality**: Users can add products to their cart, view the cart, update quantities, and proceed to checkout.
- **Responsive Design**: The website is fully responsive, ensuring a seamless experience across devices.

### Admin Features
- **Manage Bookings**: Admins can view, update, and mark bookings as complete.
- **Manage Products**: Admins can add, update, and remove detailing products available for purchase.
- **User Management**: Admins can view and manage user accounts.

## Technology Stack

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3 (Bootstrap), JavaScript (jQuery, Flatpickr)
- **Database**: PostgreSQL (or SQLite for development)
- **Deployment**: Gunicorn, Nginx, Heroku/AWS (or local development server)
- **Version Control**: Git & GitHub

## Installation

### Prerequisites

-
 Python 3.8+
- pip (Python package manager)
- PostgreSQL (optional, for production)

### Setup

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/ChristianChun/nexuswash.git
    cd nexuswash
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up the Database**:
    - For SQLite (default):
        ```bash
        python manage.py migrate
        ```
    - For PostgreSQL:
        - Update `DATABASES` in `settings.py` with your PostgreSQL credentials.
        - Run migrations:
            ```bash
            python manage.py migrate
            ```

5. **Create a Superuser**:
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

7. **Access the Application**:
    - Open your web browser and go to `http://127.0.0.1:8000/`.

## Project Structure
nexuswash/
├── carWashMng/ # Main application directory
│ ├── migrations/ # Database migrations
│ ├── templates/ # HTML templates
│ │ ├── base.html # Base template
│ │ ├── index.html # Home page template
│ │ ├── services.html # Service booking page
│ │ ├── ... # Other templates
│ ├── static/ # Static files (CSS, JS, images)
│ ├── views.py # View functions and classes
│ ├── models.py # Database models
│ ├── urls.py # URL routing
│ ├── forms.py # Django forms
│ └── ... # Other app-specific files
├── nexuswash/ # Project configuration
│ ├── settings.py # Project settings
│ ├── urls.py # Project URL configuration
│ ├── wsgi.py # WSGI configuration for deployment
│ └── ...
├── manage.py # Django management script
└── README.md # Project documentation


## Deployment

To deploy this project to a production server, follow these steps:

1. **Set Up a Production Database**: Configure PostgreSQL or another production database.
2. **Configure the Server**: Set up Gunicorn and Nginx for serving the Django application.
3. **Static and Media Files**: Collect static files and configure media file storage.
    ```bash
    python manage.py collectstatic
    ```
4. **Environment Variables**: Securely manage environment variables for sensitive data.

## Usage

- **User Registration**: Users can sign up using the registration page.
- **Service Booking**: Book services from the services page after logging in.
- **Product Purchase**: Add products to the cart and proceed to checkout.
- **Admin Management**: Log in as an admin to manage bookings, products, and users.

## Contributing

Contributions are welcome! Please submit a pull request or create an issue for any bugs or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact the project maintainer at christian.chunn02@gmail.com.

