from timeit import default_timer as timer

import get_retries


def test_200():
    res = get_retries.get('https://httpbin.org/status/200')
    assert(res.status_code == 200)


def test_500():
    start = timer()
    res = get_retries.get('https://httpbin.org/status/500', max_backoff=8)
    assert(res is None)
    assert(timer() - start > 15)


def test_400():
    start = timer()
    res = get_retries.get('https://httpbin.org/status/400', max_backoff=8)
    assert(res is None)
    assert(timer() - start < 15)


def test_timeout():
    res = get_retries.get('https://httpbin.org/delay/10', timeout=5)
    assert(res is None)


def test_timeout_success():
    res = get_retries.get('https://httpbin.org/delay/10', timeout=11)
    assert(not res is None)


def test_verbose_true(capsys):
    get_retries.get('https://httpbin.org/delay/10',
                    timeout=5, verbose=True, max_backoff=4)
    out, _ = capsys.readouterr()
    print(out)
    assert(len(out) != 0)


def test_verbose_false(capsys):
    get_retries.get('https://httpbin.org/delay/10',
                    timeout=5, verbose=False, max_backoff=4)
    out, _ = capsys.readouterr()
    print(out)
    assert(len(out) == 0)
