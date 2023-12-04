from pathlib import Path

import pytest


# https://pytest-vcr.readthedocs.io/en/latest/configuration/#configuration-fixtures
@pytest.fixture(scope='module')
def vcr_cassette_dir(request):
    test_dir = request.node.fspath.dirname
    return str(Path(test_dir).parent / 'cassettes')


@pytest.fixture
def urls():
    yield [
        'https://blog.m9h8.com/rss.xml',
        'https://feeds.bbci.co.uk/zhongwen/trad/rss.xml',
        'https://feeds.feedburner.com/rsscna/intworld',
        'https://hnrss.org/newest?q=Python&points=123&comments=123',
        'https://theinitium.com/newsfeed/',
    ]
