#!/usr/bin/env python2

import json
import argparse
import requests
import requests.exceptions

from HTMLParser import HTMLParser


class LinkImageParser(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []
        self.images = []

    def handle_starttag(self, tag, attrs):
        if tag not in ['a', 'img']:
            return
        for attr, value in attrs:
            if tag == 'a' and attr == 'href':
                self.links.append(value)
            elif tag == 'img' and attr == 'src':
                self.images.append(value)


class ImageLinks(object):

    def main(self, args):
        print self.process_urls(args.urls)

    def process_urls(self, urls):
        data = dict()
        for url in urls:
            data[url] = self.get_data_from_url(url)
        return json.dumps(data, indent=4)

    def get_data_from_url(self, url):
        src = self.get_source(url)
        if not src:
            return dict(links=[], images=[])
        parser = self.parse_source(src)
        return dict(links=parser.links, images=parser.images)

    def get_source(self, url):
        try:
            source = requests.get(url, timeout=2)
            return source.text
        except requests.exceptions.RequestException:
            return

    def parse_source(self, src):
        parser = LinkImageParser()
        parser.feed(src)
        return parser


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description='Retrieve image and links from web pages')
    arg_parser.add_argument('urls', nargs='+', help='A list of urls to process')
    script_args = arg_parser.parse_args()
    i = ImageLinks()
    i.main(script_args)
