import datetime
from typing import Final

from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.cache import cache_control, cache_page
from django.views.decorators.http import require_POST, require_safe

from {{ cookiecutter.project_slug }}.manifest import get_assetlinks, get_manifest

_CACHE_TIMEOUT: Final = 60 * 60 * 24 * 365


_cache_control = cache_control(max_age=_CACHE_TIMEOUT, immutable=True, public=True)
_cache_page = cache_page(_CACHE_TIMEOUT)


@require_safe
def index(request) -> HttpResponse:
    """Landing page of site."""

    return render(request, "index.html")


@require_safe
def about(request: HttpRequest) -> HttpResponse:
    """Renders About page."""
    return render(
        request,
        "about.html",
        {
            "contact_email": settings.CONTACT_EMAIL,
        },
    )

@require_safe
def privacy(request: HttpRequest) -> HttpResponse:
    """Renders Privacy  page."""
    return render(request, "privacy.html")


@require_POST
def accept_gdpr_cookies(_) -> HttpResponse:
    """Handles "accept" action on GDPR cookie banner."""
    response = HttpResponse()
    response.set_cookie(
        settings.GDPR_COOKIE_NAME,
        value="true",
        expires=timezone.now() + datetime.timedelta(days=365),
        secure=True,
        httponly=True,
        samesite="Lax",
    )

    return response


@require_safe
@_cache_control
@_cache_page
def favicon(_) -> HttpResponse:
    """Generates favicon file."""
    return HttpResponse(
        (
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
            + '<text y=".9em" font-size="90">🦊</text>'
            + "</svg>"
        ),
        content_type="image/svg+xml",
    )

@require_safe
@_cache_control
@_cache_page
def robots(_) -> HttpResponse:
    """Generates robots.txt file."""
    return HttpResponse(
        "\n".join(
            [
                "User-Agent: *",
            ]
        ),
        content_type="text/plain",
    )


@require_safe
@_cache_control
@_cache_page
def security(_) -> HttpResponse:
    """Generates security.txt file containing contact details etc."""
    return HttpResponse(
        "\n".join(
            [
                f"Contact: mailto:{settings.CONTACT_EMAIL}",
            ]
        ),
        content_type="text/plain",
    )

