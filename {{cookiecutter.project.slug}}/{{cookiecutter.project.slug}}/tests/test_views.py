import pytest
from django.conf import settings
from django.template.response import TemplateResponse
from django.urls import reverse, reverse_lazy
from pytest_django.asserts import assertTemplateUsed

from {{ project_slug }}.tests.asserts import assert200


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
    def test_anonymous(self, client):
        response = client.get(self.url)
        assert200(response)
        assertTemplateUsed(response, "index.html")

    @pytest.mark.django_db
    def test_authenticated(self, client, auth_user):
        response = client.get(self.url)
        assert response.url == settings.LOGIN_REDIRECT_URL


class TestManifest:
    @pytest.mark.django_db
    def test_get(self, client):
        response = client.get(reverse("manifest"))
        assert200(response)


class TestAssetlinks:
    @pytest.mark.django_db
    def test_get(self, client):
        response = client.get(reverse("assetlinks"))
        assert200(response)


class TestServiceWorker:
    @pytest.mark.django_db
    def test_get(self, client):
        response = client.get(reverse("service_worker"))
        assert200(response)


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



