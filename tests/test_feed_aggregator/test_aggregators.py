import pytest
from feed_aggregator import aggregators


@pytest.mark.vcr()
def test_aggregate(urls):
    aggregators.aggregate(
        urls,
        id='id',
        title='title',
        author_name='author_name',
    )
