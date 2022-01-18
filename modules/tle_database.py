import sys
import logging
import mariadb

logger = logging.getLogger("tle_fetcher." + __name__)


class TleDatabase:
    def __init__(self):
        self.conn = None

    def connect_db(self):

        # Connect to MariaDB
        try:
            conn = mariadb.connect(
                user="tle_fetcher",
                host="localhost",
                port=3306,
                database="celestrak_tles",
            )
        except mariadb.Error as err:
            logger.error("Error connecting to MariaDB Platform: %s", err.msg)
            sys.exit(1)

        self.conn = conn

    def delete_rows(self):
        cur = self.conn.cursor()

        try:
            cur.execute("delete from sat_groups")
            cur.execute("delete from tles")
        except mariadb.Error as err:
            logger.error("Error clearing tables: %s", err.msg)
        self.conn.commit()

    def update_tles(self, tles: list):
        cur = self.conn.cursor()

        try:
            cur.executemany(
                "insert into tles (sat, sat_cat_num, tle) values (?,?,?)", tles
            )
        except mariadb.Error as err:
            logger.error("Error updating TLEs: %s", err.msg)
        self.conn.commit()

    def update_sat_group(self, group: list):
        cur = self.conn.cursor()

        try:
            cur.executemany(
                "insert ignore into sat_groups (sat_cat_num, group_name) values (?,?)",
                group,
            )
        except mariadb.Error as err:
            logger.error("Error updating groups: %s", err.msg)
        self.conn.commit()

    def close_db(self):
        self.conn.close()
