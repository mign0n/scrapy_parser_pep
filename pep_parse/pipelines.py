import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT, RESULTS_DIR


class PepParsePipeline:
    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.counter = defaultdict(int)
        now_formatted = dt.now().strftime(DATETIME_FORMAT)
        self.file_path = (
            f'{self.results_dir}/status_summary_{now_formatted}.csv'
        )

    def process_item(self, item, spider):
        self.counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(self.file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f,
                dialect=csv.unix_dialect(),
                quoting=csv.QUOTE_MINIMAL,
            ).writerows(
                [
                    ('Статус', 'Количество'),
                    *self.counter.items(),
                    ('Всего:', sum(self.counter.values())),
                ]
            )
