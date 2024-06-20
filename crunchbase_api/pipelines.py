import logging
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem

class CrunchbaseApiPipeline(object):
    def __init__(self):
        self.seen_perma_links = set()

    def process_item(self, item, spider):
        uuid = item.get('uuid')
        if uuid in self.seen_perma_links:
            raise DropItem(f"Duplicate item found: {item}")
        else:
            self.seen_perma_links.add(uuid)
            return item
