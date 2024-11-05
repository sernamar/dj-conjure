import pytest
from django.contrib.sites.models import Site

from {{ cookiecutter.project_slug }}.templatetags import (
    absolute_uri
)


@pytest.fixture
def req(rf, anonymous_user):
    req = rf.get("/")
    req.user = anonymous_user
    req.htmx = False
    req.site = Site.objects.get_current()
    return req


@pytest.fixture
def auth_req(req, user):
    req.user = user
    return req



class TestAbsoluteUri:
    @pytest.mark.django_db
    def test_plain_url(self):
        assert absolute_uri("/index/") == "http://example.com/index/"

    @pytest.mark.django_db
    def test_https(self, settings):
        settings.SECURE_SSL_REDIRECT = True
        assert absolute_uri("/index/") == "https://example.com/index/"
