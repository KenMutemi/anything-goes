#coding: utf8
from urlparse import urlparse
from requests import ConnectionError
from main.helpers import remove_non_ascii
import requests
import lxml
from lxml import html


hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Connection': 'keep-alive'}

def update_summaries(summary):
    try:
        response = requests.get(summary.url, headers=hdr)
    except ConnectionError:
        print "Could not connect to %s" % summary.url
    tree = html.fromstring(response.content)
    try:
        summary.title = tree.xpath(remove_non_ascii('//title/text()'))[0].encode('utf-8').replace('Â', '')
    except IndexError:
        summary.title = '[title not available]'
    for noscript in tree.xpath(".//noscript"):
        noscript.getparent().remove(noscript)
    paragraphs = tree.xpath('.//p')
    summary.paragraphs = [remove_non_ascii(paragraph.text_content()) for paragraph in paragraphs]
    parsed_uri = urlparse(summary.url)
    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    images = tree.xpath('.//img/@src')
    summary.images = [domain+image if not image.startswith(domain) and not image.startswith('http') else image for image in images]
    summary.save()
