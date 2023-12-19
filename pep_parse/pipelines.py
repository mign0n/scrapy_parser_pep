import csv
from collections import defaultdict
from datetime import datetime as dt

from pep_parse.settings import BASE_DIR, DATETIME_FORMAT, RESULTS_DIR


class PepParsePipeline:
    def __init__(self):
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        now_formatted = dt.now().strftime(DATETIME_FORMAT)
        self.file_path = f'{results_dir}/status_summary_{now_formatted}.csv'
        self.counter = defaultdict(int)
        self.results = [('Статус', 'Количество')]

    def open_spider(self, spider):
        ...

    def process_item(self, item, spider):
        self.counter[item['status']] += 1
        return item

    def close_spider(self, spider):
        self.results.extend(self.counter.items())
        self.results.append(('Всего:', sum(self.counter.values())))

        with open(self.file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f,
                dialect=csv.unix_dialect(),
            ).writerows(
                self.results,
            )
