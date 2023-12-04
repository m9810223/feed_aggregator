import logging

from feed_aggregator import aggregate


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    feedstr = aggregate(
        [
            'https://blog.m9h8.com/rss.xml',
            'https://feeds.bbci.co.uk/zhongwen/trad/rss.xml',
            'https://feeds.feedburner.com/rsscna/intworld',
            'https://hnrss.org/newest?q=Python&points=123&comments=123',
            'https://theinitium.com/newsfeed/',
        ],
        id='https://feed-id.com/',
        title='''m9H8's feed''',
        author_name='m9H8',
    )
    print(feedstr, file=open('_.xml', 'w'))
