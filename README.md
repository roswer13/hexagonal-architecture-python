# Hexagonal-architecture-python

This repository contains a simple example of a Python application that follows the principles of hexagonal architecture (also known as ports and adapters architecture). The goal is to demonstrate how to structure a Python application in a way that separates the core business logic from external concerns such as databases, web frameworks, and other I/O operations.

## Installation

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
pip install -r requirements.dev.txt
```

## Running the Application

To run the application, you can use the following command:

```bash
python src/manage.py migrate
python src/manage.py runserver
```

## Running Tests
To run the tests, you can use the following command:

```bash
python src/manage.py test
```

## Checking Code Style
To check the code style, you can use the following command:

```bash
flake8 .
````
