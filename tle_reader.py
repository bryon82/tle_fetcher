import urllib.request
import sys
import logging

logger = logging.getLogger('tle_fetcher.' + __name__)

class TleReader():
    def __init__(self, url_root: str):
        self.url_root = url_root   

    def get_tles(self) -> dict:
        url = self.url_root + 'active.txt'
        tles = {}

        try:
            with urllib.request.urlopen(url) as txt:
                i = 0  
                key = ""
                value = ""
                for line in txt:
                    line = line.strip().decode('utf-8')
                    if i % 3 == 0:
                        key = line
                    elif i % 3 == 1:
                        value = line
                    else:
                        value += "\n" + line
                        tles[key] = value
                    i += 1
        except Exception as ex:
            logger.error("Error getting TLEs: %s", ex.msg)
            sys.exit(1)
        
        return tles

    def get_group(self, group_name: str) -> list:
        url = self.url_root + group_name + '.txt'
        group = []
        
        try:    
            with urllib.request.urlopen(url) as txt:
                i = 0  
                for line in txt:
                    line = line.strip().decode('utf-8')
                    if i % 3 == 0:
                        group.append((line, group_name))
                    i += 1
        except Exception as ex:
            logger.error("Error getting groups: %s", ex.msg)
            sys.exit(1)
        
        return group