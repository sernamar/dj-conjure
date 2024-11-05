from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "{{ cookiecutter.project_slug }}.users"
    default_auto_field = "django.db.models.BigAutoField"
