# get_retries [![Build Status](https://travis-ci.com/jfilter/get_retries.svg?branch=master)](https://travis-ci.com/jfilter/get_retries) [![PyPI](https://img.shields.io/pypi/v/get_retries.svg)](https://pypi.org/project/get_retries/) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/get_retries.svg)](https://pypi.org/project/get_retries/)

Adding retries to [Requests](https://github.com/requests/requests)`.get()` with [exponential backoff](https://en.wikipedia.org/wiki/Exponential_backoff).

Retry unsuccessful `GET` requests after waiting for a specific time interval. With each unsuccessful request, the time interval increases exponentially (it doubles). The undertaking is declared ultimately unsuccessful when the time interval gets bigger than a _maximum backoff_ value.

## Install

```bash
pip install get_retries
```

## Usage

```python
import get_retries

# max_backoff: maximum interval to wait in seconds
response = get_retries.get('https://wikipedia.com', max_backoff=32)

if response:
    print(response.status_code)
```

For more information check out the [code](get_retries/get.py).

## License

MIT.
