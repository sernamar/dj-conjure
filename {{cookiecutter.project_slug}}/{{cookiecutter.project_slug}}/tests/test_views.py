import pytest
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy
from pytest_django.asserts import assertTemplateUsed

from {{ cookiecutter.project_slug }}.tests.asserts import assert200


class TestErrorPages:
    @pytest.mark.parametrize(
        "template_name",
        [
            pytest.param("400.html"),
            pytest.param("403.html"),
            pytest.param("403_csrf.html"),
            pytest.param("405.html"),
            pytest.param("429.html"),
            pytest.param("500.html"),
        ],
    )
    def test_render_page(self, rf, template_name):
        response = TemplateResponse(rf.get("/"), template_name)
        assert b"Error" in response.render().content


class TestIndex:
    url = reverse_lazy("index")

    @pytest.mark.django_db
    def test_get(self, client):
        response = client.get(self.url)
        assert200(response)
        assertTemplateUsed(response, "index.html")


class TestFavicon:
    @pytest.mark.django_db
    def test_get(self, client):
        response = client.get(reverse("favicon"))
        assert200(response)


class TestRobots:
    @pytest.mark.django_db
    def test_get(self, client):
        response = client.get(reverse("robots"))
        assert200(response)


class TestSecurty:
    @pytest.mark.django_db
    def test_get(self, client):
        response = client.get(reverse("security"))
        assert200(response)


class TestAbout:
    @pytest.mark.django_db
    def test_get(self, client):
        response = client.get(reverse("about"))
        assert200(response)


class TestPrivacy:
    @pytest.mark.django_db
    def test_get(self, client):
        response = client.get(reverse("privacy"))
        assert200(response)


class TestAcceptGdprCookies:
    @pytest.mark.django_db
    def test_post(self, client):
        response = client.post(reverse("accept_gdpr_cookies"))
        assert200(response)
        assert "accept-cookies" in response.cookies


