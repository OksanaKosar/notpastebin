# README for Django Paste Project

## Table of Contents

1. [Installation](#1-installation)
2. [How It Works](#2-how-it-works)
3. [Celery Integration](#3-celery-integration)

## 1. Installation

To get started with the Django PasteBin project, follow these installation steps:

### Prerequisites

Before you begin, make sure you have the following installed on your system:

- Python (3.7 or higher)
- Django (3.2 or the latest version)
- Virtual environment (optional but recommended)
- Celery

### Clone the Repository

Clone the PasteBin project repository from the source code repository:

```bash
git clone https://github.com/OksanaKosar/notpastebin
cd pasteBin
```

### Create a Virtual Environment (Optional)

It's a good practice to work in a virtual environment to isolate project dependencies. To create and activate a virtual environment, run the following commands:

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows, use myenv\Scripts\activate
```

### Install Dependencies

Install the required Python packages listed in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Database Setup

Migrate the database to create the necessary tables:

```bash
python manage.py makemigration
python manage.py migrate
```

### Create a Superuser (Admin)

You can create an admin user to access the Django admin panel:

```bash
python manage.py createsuperuser
```

### Run the Development Server

Start the Django development server:

```bash
python manage.py runserver
```

The PasteBin project should now be accessible at `http://localhost:8000/`.

## 2. How It Works

The Django PasteBin project is organized into multiple apps, including the main `pasteBin` app and the `user_management` app. Here is a brief overview of the project structure and key components:

### URL Patterns

In the main `urls.py`, the project's URL patterns are defined as follows:

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("pasteBin.urls")),
    path('user/', include("user_management.urls")),
]
```

The project includes two apps with their own URL patterns: `pasteBin` and `user_management`.

#### `user_management` App URL Patterns

The `user_management` app defines the following URL patterns:

- `/register/`: Register a user
- `/login/`: Log in a user
- `/logout/`: Log out a user

#### `pasteBin` App URL Patterns

The `pasteBin` app defines the following URL patterns:

- `/`: Home page for creating pastes
- `/mypaste`: View pastes created by the logged-in user
- `/paste/<int:pk>/`: View a specific paste by its primary key


## 3. Celery Integration

The Django PasteBin project now includes Celery for background task processing. Celery is configured to automatically remove expired paste rows every 24 hours.

Make sure to have Celery installed and running. You can start Celery with the following command:

```bash
celery -A base worker --loglevel=info
```
```bash
celery -A base beat --loglevel=info
```
The scheduled task to remove expired rows is set up in the `delete_expired_rows` Celery task located in the `pasteBin/tasks.py` file. This task runs every 24 hours and deletes paste rows with expiration dates earlier than yesterday.

Ensure that your Celery and Django environments are properly configured for seamless integration. Explore the codebase and templates for more details on the project's features and implementation.

Happy coding!