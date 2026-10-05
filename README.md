# Django Web Management System

A full-stack web application built with Django for managing user accounts, profiles, authentication, and contact messages through a structured user and administration system.

## Project Team

## Project Team

| Team Member     | Responsibility                                      |
| --------------- | --------------------------------------------------- |
| **Kayo Ketama** | Backend & Django Development                        |
| **Habib Jemal** | Frontend Development & UI Design                    |
| **Hamza**       | Database Management & Testing                       |
| **Abdulaziz**   | Documentation, Deployment Support & Project Testing |


## The Problem

Managing user accounts and communication becomes increasingly difficult when registration, profile information, authentication, and messages are handled separately.

The goal of this project was to build a single web application that brings these activities together. Users have a dedicated space for managing their accounts, while administrators have the tools needed to oversee users and contact messages.

The result is a practical management system designed around two main areas: **user account management** and **administrative management**.

## What It Does

### User Side

The application provides users with the following functionality:

* Account registration and activation
* Secure login and logout
* Personal dashboard
* Profile viewing and editing
* Password change
* Password reset
* Contact form for sending messages

### Administration Side

Administrators can manage the application through a dedicated administration area:

* Custom admin dashboard
* View registered users
* Search users
* View individual user information
* Delete user accounts
* View contact messages
* Search messages
* Delete messages
* Django built-in administration panel
* Protected administrative access

## How to Run It

### Prerequisites

Make sure the following are installed:

* Python 3.13+
* Git
* A modern web browser

### 1. Clone the repository

```bash
git clone https://github.com/kayoketama/django-web-management-system.git
```

### 2. Enter the project directory

```bash
cd django-web-management-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

On Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

If PowerShell blocks the script:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
```

Then activate the environment:

```powershell
venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply database migrations

```bash
python manage.py migrate
```

### 7. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the prompts to create the administrator account.

### 8. Start the development server

```bash
python manage.py runserver
```

The application will then be available at:

```text
http://localhost:8000/
```

## Built With

| Technology                    | Purpose                               |
| ----------------------------- | ------------------------------------- |
| **Python**                    | Core programming language             |
| **Django 6.1.1**              | Web application framework             |
| **django-registration-redux** | Registration and account activation   |
| **HTML5**                     | Page structure                        |
| **CSS3**                      | Styling                               |
| **Bootstrap**                 | Responsive interface components       |
| **SQLite**                    | Local development database            |
| **PostgreSQL**                | Production database                   |
| **Gunicorn**                  | Production application server         |
| **WhiteNoise**                | Static file serving                   |
| **dj-database-url**           | Database URL configuration            |
| **Git & GitHub**              | Version control and source management |
| **Render**                    | Application deployment                |

## Demo

### Live Application

**https://django-web-management-system.onrender.com**

### Project Recording

**[Watch the Project Demo](PASTE-YOUR-RECORDING-LINK-HERE)**

The recording demonstrates the main user workflow and administrative features of the application.

## Contributions

### Kayo Ketama

Responsible for the core Django development and backend functionality, including:

* Project configuration and Django architecture
* User registration and authentication
* Account activation
* User dashboard
* Profile management
* Password management
* Custom admin dashboard
* User management
* Contact message management
* Database configuration
* Production deployment

### Habib Jemal

Responsible for the frontend and user interface, including:

* Designing and organizing web pages
* HTML and CSS implementation
* Bootstrap-based responsive layouts
* Navigation and page structure
* User-facing forms and interface elements
* Improving the overall usability of the application

### Hamza

Responsible for database-related tasks and application testing, including:

* Database structure and configuration
* Working with Django models and migrations
* Testing user registration and authentication workflows
* Testing administrative features
* Identifying and reporting application issues
* Verifying that major features work as expected

### Abdulaziz

Responsible for documentation, testing support, and deployment-related tasks, including:

* Project documentation
* README preparation and updates
* Testing application workflows
* Supporting deployment configuration
* Reviewing the application before submission
* Helping verify that the deployed application works correctly


## What We Would Build Next

The current version provides the core functionality required for user and administrative management. With additional development time, we would extend it in the following areas:

### 1. Production Email Service

Integrate a dedicated email service to handle account activation, password-reset requests, and contact-message notifications reliably in production.

### 2. More Powerful Administration

Expand the admin dashboard with user statistics, pagination, advanced search, filtering, and activity summaries to make the system more useful as the amount of data grows.

### 3. Improved User Experience

Further improve the interface with stronger mobile responsiveness, clearer form feedback, smoother navigation, and a more consistent design across the application.
