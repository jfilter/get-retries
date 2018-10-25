"""Implementing exponential backoff for requests.get (https://en.wikipedia.org/wiki/Exponential_backoff)
"""

import time

import requests
from requests.exceptions import RequestException


def get(url, max_backoff=32, verbose=False, **kwargs):
    """Adding retries to requests.get with exponential backoff.

    Args:
        url (str): The URL to fetch
        max_backoff (int): The number of seconds to sleep at maximums
        verbose (bool): Whether to print exceptions.

    Returns:
        Response: For successful requests return requests' response. `None` otherwise.
    """
    sleep_seconds = 1
    while sleep_seconds <= max_backoff:
        try:
            # you may overwrite `timeout` via `kwargs`
            response = requests.get(url, **{**{'timeout': 30}, **kwargs})
            # for 4xx, return instantly, no hope of success
            if 400 <= response.status_code < 500:
                return None
            # successfully return 2XX and 3xx
            if 200 <= response.status_code < 400:
                return response
            # for 1xx and 5xx, retry
        except RequestException as e:
            if verbose:
                print(str(e))

        time.sleep(sleep_seconds)
        sleep_seconds *= 2
    return None
