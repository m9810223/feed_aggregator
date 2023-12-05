import logging
import typing as t

import httpx


logger = logging.getLogger(__name__)


def create_http_client():
    c = httpx.Client()
    return c


def fetch_url(url: str, *, client: t.Optional[httpx.Client] = None):
    if client is None:
        client = create_http_client()
    response = client.get(url)
    text = response.text
    return text


def fetch_urls(urls: t.Iterable[str], *, client: t.Optional[httpx.Client] = None):
    texts = (fetch_url(x, client=client) for x in urls)
    return texts
