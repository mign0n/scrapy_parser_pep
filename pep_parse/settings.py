from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

BASE_DIR = Path(__file__).parent.parent
RESULTS_DIR = 'results'

FEEDS = {
    Path(RESULTS_DIR).joinpath('pep_%(time)s.csv'): {
        'fields': ['number', 'name', 'status'],
        'format': 'csv',
        'overwrite': True,
    },
}
