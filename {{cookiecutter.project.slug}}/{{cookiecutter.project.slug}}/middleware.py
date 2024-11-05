from collections.abc import Callable
from typing import Final

from django.contrib.messages import get_messages
from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string
from django.utils.cache import patch_vary_headers
from django_htmx.http import HttpResponseLocation


class BaseMiddleware:
    """Base middleware class."""

    def __init__(self, get_response: Callable[[HttpRequest], HttpResponse]) -> None:
        self.get_response = get_response


class HtmxRestoreMiddleware(BaseMiddleware):
    """Workarounds for https://github.com/bigskysoftware/htmx/issues/497.

    Sets Cache-Control and Vary headers to ensure full page is rendered.

    Place after HtmxMiddleware.
    """

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """Middleware implementation."""
        response = self.get_response(request)
        if request.htmx:
            patch_vary_headers(response, ("HX-Request",))
            response.setdefault("Cache-Control", "no-store, max-age=0")
        return response


class HtmxMessagesMiddleware(BaseMiddleware):
    """Adds messages to HTMX response"""

    _hx_redirect_headers: Final = frozenset(
        {
            "HX-Location",
            "HX-Redirect",
            "HX-Refresh",
        }
    )

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """Middleware implementation"""
        response = self.get_response(request)

        if not request.htmx:
            return response

        if set(response.headers) & self._hx_redirect_headers:
            return response

        if messages := get_messages(request):
            response.write(
                render_to_string(
                    "components/messages.html",
                    {
                        "messages": messages,
                    },
                    request=request,
                )
            )

        return response


class HtmxRedirectMiddleware(BaseMiddleware):
    """If HTMX request will send HX-Location response header if HTTP redirect."""

    # HTMX 2.0.3: must provide explicit target if not `document.body`
    _target: str = "#content"

    def __call__(self, request: HttpRequest) -> HttpResponse:
        """Middleware implementation"""
        response = self.get_response(request)
        if request.htmx and "Location" in response:
            return HttpResponseLocation(response["Location"], target=self._target)
        return response
