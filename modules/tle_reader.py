import urllib.request
import sys
import logging

logger = logging.getLogger("tle_fetcher." + __name__)


class TleReader:
    def __init__(self, url_root: str):
        self.url_root = url_root

    def get_tles(self) -> list:
        url = self.url_root + "active.txt"
        tles = []

        try:
            with urllib.request.urlopen(url) as txt:
                i = 0
                sat = ""
                tle = ""
                for line in txt:
                    line = line.strip().decode("utf-8")
                    if i % 3 == 0:
                        sat = line
                    elif i % 3 == 1:
                        tle = line
                    else:
                        tle += "\n" + line
                        tles.append((sat, line.split()[1], tle))
                    i += 1

        except Exception as ex:
            logger.error("Error getting TLEs: %s", ex)
            sys.exit(1)

        return tles

    def get_group(self, group_name: str) -> list:
        url = self.url_root + group_name + ".txt"
        group = []

        try:
            with urllib.request.urlopen(url) as txt:
                i = 0
                for line in txt:
                    line = line.strip().decode("utf-8")
                    if i % 3 == 2:
                        group.append((line.split()[1], group_name))
                    i += 1

        except Exception as ex:
            logger.error("Error getting groups: %s", ex)
            sys.exit(1)

        return group
