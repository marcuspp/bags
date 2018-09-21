#!/usr/bin/env python2

import json
import mock
import unittest
import answer_4
import requests.exceptions


HTML_SOURCE = "<html><body>" \
              "<a href='http://test.com/home/' class=''>" \
              "<img src='http://test.com/1.jpg'><img src='http://test.com/2.jpg'>" \
              "<a href='http://test.com/logout/' class=''>" \
              "</body></html>"


class FakeRequestResponse(object):

    @property
    def text(self):
        return '<html></html>'


class TestAnswer4(unittest.TestCase):

    def test_parse_html_source_for_image(self):
        html = '<img src="http://test.com/1.jpg">'
        image_links = answer_4.ImageLinks()
        actual_parser = image_links.parse_source(html)
        self.assertEquals(actual_parser.images, ["http://test.com/1.jpg"])
        self.assertEquals(actual_parser.links, [])

    def test_parse_html_source_for_links(self):
        html = '<a href="http://test.com/inbox/">'
        image_links = answer_4.ImageLinks()
        actual_parser = image_links.parse_source(html)
        self.assertEquals(actual_parser.images, [])
        self.assertEquals(actual_parser.links, ["http://test.com/inbox/"])

    @mock.patch('answer_4.ImageLinks.get_source')
    def test_get_data_for_url_returns_no_source(self, mock_get_source):
        mock_get_source.return_value = None
        image_links = answer_4.ImageLinks()
        result = image_links.get_data_from_url('http://www.madeupthis.com')
        self.assertEquals(result['images'], [])
        self.assertEquals(result['links'], [])

    @mock.patch('answer_4.ImageLinks.get_source')
    def test_get_data_for_url_returns_data(self, mock_get_source):
        mock_get_source.return_value = HTML_SOURCE
        image_links = answer_4.ImageLinks()
        result = image_links.get_data_from_url('http://www.madeupthis.com')
        self.assertEquals(result['images'], ['http://test.com/1.jpg', 'http://test.com/2.jpg'])
        self.assertEquals(result['links'], ['http://test.com/home/', 'http://test.com/logout/'])

    @mock.patch('answer_4.ImageLinks.get_data_from_url')
    def test_process_urls_with_more_than_one_url(self, mock_get_data_from_url):
        mock_get_data_from_url.side_effect = [{'images': ['hello-image.jpg'], 'links': ['http://hello.com/home/']},
                                              {'images': ['goodbye-image.jpg'], 'links': []}]
        image_links = answer_4.ImageLinks()
        result = image_links.process_urls(['http://hello.com', 'http://goodbye.com'])
        dict_result = json.loads(result)
        self.assertDictEqual(
            dict_result, {
                'http://hello.com': {'images': ['hello-image.jpg'], 'links': ['http://hello.com/home/']},
                'http://goodbye.com': {'images': ['goodbye-image.jpg'], 'links': []}
            }
        )
        self.assertEquals(mock_get_data_from_url.call_count, 2)

    @mock.patch('requests.get')
    def test_get_source_returns_html_source(self, mock_get_request):
        mock_get_request.return_value = FakeRequestResponse()
        image_links = answer_4.ImageLinks()
        response = image_links.get_source('')
        self.assertEquals(response, '<html></html>')

    @mock.patch('requests.get')
    def test_get_source_handles_exception(self, mock_get_request):
        mock_get_request.side_effect = requests.exceptions.ConnectTimeout()
        image_links = answer_4.ImageLinks()
        response = image_links.get_source('')
        self.assertIsNone(response)


if __name__ == '__main__':
    unittest.main()
