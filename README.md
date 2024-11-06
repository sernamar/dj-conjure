Cookiecutter for generating an opinionated Django project.

## Installation

```bash
pip install cookiecutter
cookiecutter https://github.com/danjac/dj-conjure
cd my-project
git init
just install
```

## Features

* [HTMX](https://htmx.org/)
* [TailwindCSS](https://tailwindcss.com/)
* [AlpineJS](https://alpinejs.dev/)
* [Django Cotton](https://django-cotton.com/)
* [Django Template Partials](https://github.com/carltongibson/django-template-partials)
* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)

This template is intended for quick prototyping and small side projects, while providing a solid base for larger and more complex applications.

A Dockerfile is provided for deployment to a number of platforms, e.g. a PAAS like Heroku or a VPS like Digital Ocean. A `docker-compose.yml` file is also provided to bootstrap local development using PostgreSQL and Redis.

