# Full Stack Learning

## Overview

This project is a Django-based web application with additional configurations for TypeScript and VS Code extensions. The project includes multiple apps and configurations to enhance development and deployment processes.

## Project Structure

- `first_tutorial_project/`: Contains the main Django project.
    - `first_app/`: A Django app within the project.
        - `views.py`: Defines the view functions for the app.
        - `templates/first_app/index.html`: Template for rendering the index view.
    - `settings.py`: Configuration settings for the Django project.

- `level_two/`: Another Django project with similar structure.
    - `first_app/`: A Django app within the project.
        - `views.py`: Defines the view functions for the app.
        - `templates/first_app/index.html`: Template for rendering the index view.
    - `settings.py`: Configuration settings for the Django project.

- `django_project/trial/`: Contains configurations for a VS Code extension.
    - `tsconfig.json`: TypeScript configuration file.
    - `.vscode/`: VS Code specific settings.
        - `settings.json`: Custom settings for the VS Code workspace.
    - `package.json`: Defines the dependencies and scripts for the VS Code extension.
    - `README.md`: Documentation for the VS Code extension.
    - `CHANGELOG.md`: Change log for the VS Code extension.
    - `vsc-extension-quickstart.md`: Quickstart guide for the VS Code extension.

## Requirements

- Python 3.10
- Django 5.1.5
- TypeScript 5.7.3
- Node.js and npm

## Setup

1. **Clone the repository:**
     ```sh
     git clone https://github.com/lapislui/full_stack_development
     cd Codage_Heritage
     ```

2. **Set up the Python environment:**
     ```sh
     conda create -n my_env python=3.10 -y
     conda activate my_env
     pip install -r requirements.txt
     ```

3. **Set up the TypeScript environment:**
     ```sh
     npm install
     ```

## Running the Project

1. **Run the Django development server:**
     ```sh
     python manage.py runserver
     ```

2. **Build the TypeScript files:**
     ```sh
     npm run compile
     ```

## Features

- **Django Apps:** Two separate Django projects with their own apps and configurations.
- **VS Code Extension:** Custom VS Code extension with TypeScript support.
- **Automated Workflows:** GitHub Actions workflows for CI/CD and code quality checks.

## Known Issues

- Ensure all dependencies are correctly installed.
- Check the configuration files for any environment-specific settings.

## Contributing

Feel free to open issues or submit pull requests for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

**Enjoy coding!**

## Django Working

### Overview

The project consists of two Django applications: `first_tutorial_project` and `level_two`. Each application has its own set of models, views, templates, and URLs.

### Models

Models define the structure of the database. For example, in `level_two/first_app/models.py`, there are three models: `Topic`, `Webpage`, and `AccessRecord`. These models are used to store information about different topics, webpages, and access records.

### Views

Views handle the logic for processing requests and returning responses. For example, in `level_two/first_app/views.py`, the `index` view retrieves access records from the database and renders them using the `index.html` template.

### Templates

Templates define the HTML structure of the web pages. For example, in `level_two/first_app/templates/first_app/index.html`, the template displays a list of access records.

### URLs

URLs map requests to views. For example, in `level_two/first_app/urls.py`, the URL pattern `path('', views.index, name='index')` maps the root URL to the `index` view.

### Static Files

Static files such as CSS and JavaScript are served from the `static` directory. The settings for static files are defined in `settings.py`.

### Running the Server

To run the Django development server, use the command:
```sh
python manage.py runserver
```
This will start the server and make the application accessible at `http://127.0.0.1:8000/`.

### Database Migrations

To apply database migrations, use the commands:
```sh
python manage.py makemigrations
python manage.py migrate
```
These commands will create and apply the necessary database tables based on the models defined in the application.

### Admin Interface

Django provides an admin interface for managing the application. To access the admin interface, create a superuser using the command:
```sh
python manage.py createsuperuser
```
Then, navigate to `http://127.0.0.1:8000/admin/` and log in with the superuser credentials.

### Additional Configurations

The project also includes configurations for TypeScript and VS Code extensions, which are defined in the `django_project/trial` directory.
