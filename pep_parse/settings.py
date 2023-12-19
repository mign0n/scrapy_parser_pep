BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"

FEEDS = {
    'results/pep_%(time)s.csv': {
        'fields': ['number', 'name', 'status'],
        'format': 'csv',
        'overwrite': True
    },
}
