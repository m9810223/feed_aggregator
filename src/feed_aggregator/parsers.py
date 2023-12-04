import typing as t

from . import serializers


def parse_text(feedtext: str):
    feed = serializers.Feed.model_validate_feedtext(feedtext)
    return feed


def parse_texts(feedtexts: t.Iterable[str]):
    feeds = (parse_text(x) for x in feedtexts)
    return feeds
