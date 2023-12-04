import logging
import typing as t
from datetime import datetime

import feedparser
from feedgen.feed import FeedEntry
from feedgen.feed import FeedGenerator
from pydantic import BaseModel


logger = logging.getLogger(__name__)


class Entry(BaseModel):
    id: str
    title: str
    updated: t.Optional[str] = None
    published: t.Optional[str] = None
    link: str
    summary: str

    def model_dump_fe(self):
        fe = FeedEntry()
        fe.id(id=self.id)
        fe.title(title=self.title)
        if self.updated is not None:
            fe.updated(updated=self.updated)
        if self.published is not None:
            fe.published(published=self.published)
        fe.link(href=self.link)
        fe.summary(summary=self.summary)
        return fe


class Feed(BaseModel):
    entries: t.Iterable[Entry]

    @classmethod
    def model_validate_feedtext(cls, feedtext: str):
        # https://feedparser.readthedocs.io/en/latest/
        fpd: feedparser.util.FeedParserDict = feedparser.parse(feedtext)
        m = cls.model_validate(fpd)
        return m

    def _model_dump_one_entry(self):
        logging.warning('only one entry')
        m = self.model_copy()
        m.entries = list(m.entries)[:1]
        return m

    def _model_dump_json_one_entry(self):
        m = self._model_dump_one_entry()
        j = m.model_dump_json(indent=2)
        return j


class FeedCompose(BaseModel):
    id: t.Optional[str] = None
    title: t.Optional[str] = None
    updated: t.Optional[t.Union[str, datetime]] = None
    author_name: t.Optional[str] = None
    generator_name: t.Optional[str] = None

    def model_dump_atomfeed(self, entries: t.Iterable[Entry]):
        fg = self._model_dump_feedgenerator(entries=entries)
        # https://python-feedgen.readthedocs.io/en/latest/index.html#generate-the-feed
        atomfeed = str(fg.atom_str(pretty=True), encoding='utf-8')
        return atomfeed

    def _model_dump_feedgenerator(self, *, entries: t.Iterable[Entry]):
        # https://python-feedgen.readthedocs.io/en/latest/index.html#create-a-feed
        fg = FeedGenerator()
        for entry in entries:
            fg.add_entry(entry.model_dump_fe())
        if self.id is not None:
            fg.id(id=self.id)
        if self.title is not None:
            fg.title(title=self.title)
        if self.updated is not None:
            fg.updated(updated=self.updated)
        if self.author_name is not None:
            fg.author(name=self.author_name)
        if self.generator_name is not None:
            fg.generator(generator=self.generator_name)
        return fg
