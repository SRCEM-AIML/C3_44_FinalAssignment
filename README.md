# Web Application Assignment - Flask and Django
 This project is a web application that implements two different frameworks (Flask and Django) to serve the same functionality. The application is containerized using Docker and can be run in multiple ## environments. The project has been integrated with Docker Compose for running the Flask and Django apps in separate containers. The Jenkins pipeline has also been set up for continuous integration and deployment.

## Project Structure
plaintext

web_app_assignment/
│
├── flask_app/
│   ├── Dockerfile            # Dockerfile for Flask application
│   ├── app.py                # Main Flask application file
│   ├── requirements.txt      # Python dependencies for Flask app
│   └── templates/
│       └── form.html         # HTML template for Flask form
│
├── django_app/
│   ├── Dockerfile            # Dockerfile for Django application
│   ├── manage.py             # Django project file
│   ├── requirements.txt      # Python dependencies for Django app
│   ├── app/
│   └── templates/
│       └── home.html         # HTML template for Django home page
│
├── docker-compose.yml        # Docker Compose configuration file
├── Jenkinsfile               # Jenkins pipeline configuration file
├── Dockerfile                # Main Dockerfile for the application
├── .gitignore                # Git ignore file
├── README.md                 # This file
└── requirements.txt          # Global Python dependencies (if any)

## Table of Contents
1. Project Setup

2. Docker Setup

3. How to Run Locally

4. Jenkins Pipeline

5. Repository Information

## Project Setup
This project uses Flask and Django for the web frameworks and Docker for containerization.

## Flask App
The Flask app is a simple web application that allows users to enter their name and age and returns a greeting message. It is built with a basic HTML form.

The form takes the user’s name and age, and upon submission, the application will greet the user with the name and age.

## Django App
The Django app performs the same functionality as Flask but is built using the Django framework. It consists of basic views and templates.

## Docker Setup
This project uses Docker to containerize both the Flask and Django applications. The following steps will guide you through setting up Docker.

## Prerequisites
Docker must be installed on your machine. You can download and install Docker from here.
Docker Compose is required to manage multiple containers. You can install it here.
