import os
import logging

logger = logging.getLogger("tle_fetcher." + __name__)


class TleFetcherLogger:
    @staticmethod
    def get_logger() -> logging.Logger:
        log = logging.getLogger("tle_fetcher")
        log.setLevel(logging.INFO)

        time_string = "%m/%d/%Y %H:%M:%S %Z"
        formatter = logging.Formatter(
            fmt="{asctime} [{module}] {message}", datefmt=time_string, style="{"
        )

        log_path = os.path.join(os.path.expanduser("~"), "log/tle_fetcher.log")
        f_handler = logging.FileHandler(log_path, mode="a")
        f_handler.setLevel(logging.INFO)
        f_handler.setFormatter(formatter)
        log.addHandler(f_handler)

        c_handler = logging.StreamHandler()
        c_handler.setLevel(logging.INFO)
        c_handler.setFormatter(formatter)
        log.addHandler(c_handler)

        return log
