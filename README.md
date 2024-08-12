# Django Authentication and Authorization

## Overview

This project demonstrates a basic implementation of Django's authentication and authorization features. It includes user registration, login functionality, and access control for protected views.

## Features

- User registration
- User login
- Protected views requiring authentication
- Custom error messages for login failures

## Prerequisites

- Python 3.x
- pip (Python package installer)
- Django

## Setup

### 1. Clone the Repository

```bash
git clone <https://github.com/jasjeet774/DjangoAuthenticationAuthorization>
cd <DjangoAuthenticationAuthorization>

```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv myenv
```

### Windows:

```bash
myenv\Scripts\activate
```
### macOS/Linux:

```bash
source myenv/bin/activate
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Create a Superuser

```bash
python manage.py createsuperuser
```
### 6. Run the Development Server

```bash
python manage.py runserver

```
## Usage
### Register a New User:
Navigate to http://127.0.0.1:8000/accounts/register/ to create a new user account.

### Login:
Navigate to http://127.0.0.1:8000/accounts/login/ to log in with the created user account.

### Access Protected Views:
After logging in, you will be redirected to http://127.0.0.1:8000/home/, a protected view that requires authentication.

## Project Structure
- myproject/ - Project directory
- accounts/ - App directory with user authentication views and templates
- migrations/ - Database migrations
- templates/accounts/ - HTML templates for registration and login
- views.py - Views for user authentication
- forms.py - Forms for user registration
- urls.py - URL routing for the accounts app
- myproject/ - Main project directory
- settings.py - Project settings
- urls.py - Project URL routing
- manage.py - Django management script
- requirements.txt - List of project dependencies

## Requirements
Add your project dependencies to requirements.txt using:
```bash
pip freeze > requirements.txt
```
## Contact
For any questions or issues, please contact jasjeet774


**Explanation:**

- **Overview:** Provides a brief description of the project and its features.
- **Prerequisites:** Lists the software and tools required to run the project.
- **Setup:** Step-by-step instructions to clone the repo, set up a virtual environment, install dependencies, and run the project.
- **Usage:** How to use the application, including registering and logging in.
- **Project Structure:** Describes the directory structure and key components of the project.
- **Requirements:** How to manage project dependencies. project.
- **Contact:** Contact information for further questions or issues.

Feel free to customize this template based on your project specifics!
