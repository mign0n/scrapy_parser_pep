import re

import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://{}/'.format(domain) for domain in allowed_domains]

    def parse(self, response):
        for pep_link in response.css(
            'section#numerical-index a[href^="pep-"]'
        ):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        name = response.css('section#pep-content h1::text').get()
        yield PepParseItem(
            name=name,
            number=re.search(r'\d+', name).group(0),
            status=response.css('section#pep-content abbr::text').get(),
        )
