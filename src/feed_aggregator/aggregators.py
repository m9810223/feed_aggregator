import itertools
import logging
import typing as t
from datetime import datetime

from . import composers
from . import fetchers
from . import parsers
from . import serializers
from . import utils


logger = logging.getLogger(__name__)


def aggregate(
    urls: t.Iterable[str],
    *,
    id: str,
    title: str,
    updated: t.Optional[datetime] = None,
    author_name: str,
    generator_name: str = 'feed_aggregator',
):
    # https://validator.w3.org/feed/#validate_by_input
    feedtexts = fetchers.fetch_urls(urls)
    feeds = parsers.parse_texts(feedtexts)
    entries = itertools.chain.from_iterable(x.entries for x in feeds)
    feed_compose = serializers.FeedCompose(
        id=id,
        title=title,
        # TODO: use latest updated
        updated=updated or utils.now(),
        author_name=author_name,
        generator_name=generator_name,
    )
    result = composers.compose(entries, feed_compose=feed_compose)
    return result
