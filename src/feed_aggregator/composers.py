import typing as t

from . import serializers


def compose(
    entries: t.Iterable[serializers.Entry],
    *,
    feed_compose: serializers.FeedCompose,
):
    atomfeed = feed_compose.model_dump_atomfeed(entries)
    return atomfeed
