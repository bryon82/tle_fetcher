#!/usr/bin/python3

from modules.tle_fetcher_logging import TleFetcherLogger
from modules.tle_database import TleDatabase
from modules.tle_reader import TleReader

CELESTRAK_ROOT = "https://www.celestrak.com/NORAD/elements/"

groups = [
    "stations",
    "weather",
    "noaa",
    "goes",
    "resource",
    "sarsat",
    "dmc",
    "tdrss",
    "argos",
    "planet",
    "spire",
    "geo",
    "intelsat",
    "ses",
    "iridium",
    "iridium-NEXT",
    "starlink",
    "oneweb",
    "orbcomm",
    "globalstar",
    "swarm",
    "amateur",
    "x-comm",
    "other-comm",
    "satnogs",
    "gorizont",
    "raduga",
    "molniya",
    "gnss",
    "gps-ops",
    "glo-ops",
    "galileo",
    "beidou",
    "sbas",
    "nnss",
    "musson",
    "science",
    "geodetic",
    "engineering",
    "education",
    "military",
    "radar",
    "cubesat",
    "other",
]

log = TleFetcherLogger.get_logger()
log.info("TLE fetcher started")


def main(tle_rd: TleReader, tle_db: TleDatabase) -> None:

    tles = tle_rd.get_tles()

    tle_db.connect_db()
    tle_db.delete_rows()
    tle_db.update_tles(tles)

    for group in groups:
        gp = tle_rd.get_group(group)
        tle_db.update_sat_group(gp)

    tle_db.close_db()

    log.info("TLE fetcher completed")


if __name__ == "__main__":
    main(TleReader(CELESTRAK_ROOT), TleDatabase())
