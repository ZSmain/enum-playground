# Django Enum Playground

A demonstration project showcasing different approaches to implement complex enums in Django models, with seamless integration for Django Admin and Forms.

## Installation

We are using 'uv', but you can use any virtual environment manager you want. and we are using Makefile to run the commands, but you can run them directly in the terminal.

```bash
# Create a virtual environment and install the dependencies
uv sync

# Run the migrations, create a superuser
make makemigrations
make migrate
make createsuperuser
```

## Usage

```bash
# Run the server
make runserver
```

You can either use the Django admin to create new instances of the models or the Django form in the home page: http://127.0.0.1:8000/

Select the type of Enum type you want to test, and fill the form with the data you want to test.
