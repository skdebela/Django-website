# Dynamic Website with Django

## Overview

This project utilizes Django, a high-level Python web framework, to create a dynamic website with the following features:

- Multiple dynamic pages (home, about, new_music, chart)
- Database integration for storing and retrieving data
- Admin panel for managing database content
- Media file handling for images
- Contacts page with a form for users to submit messages, which are stored in the database


## Installation

To try out the project locally, follow these steps:

1. Clone this repository to your local machine:

```bash
git clone https://github.com/samuelmideksa/Django-website
```

2. Navigate to the project directory:


3. Set up a virtual environment to isolate project dependencies (optional but recommended):

```bash
python -m venv .venv
```

4. Activate the virtual environment:

```bash
source .venv/bin/activate  # For Mac/Linux
.venv\Scripts\activate      # For Windows
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

Once you've installed the project dependencies, you can run the development server and explore the website:

```bash
python manage.py runserver
```

Access the website in your browser at the Django provided url, `http://127.0.0.1:8000/`,  and navigate to different pages (e.g., Home, About, Contact, Chart) to see the dynamic content.

To access the admin panel and manage database content, create a superuser account:

```bash
python manage.py createsuperuser
```

Then, log in to the admin panel at `http://127.0.0.1:8000/admin` using your superuser credentials.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.



## Acknowledgements

- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Bootstrap](https://getbootstrap.com/)
