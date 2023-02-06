import time

from caching import cache_lru


@cache_lru(20)
def simple_cache(limit: int):
    arr = []
    for i in range(0, limit):
        arr.append(i)
        print(i)
        time.sleep(2)
    return arr


def test_cache_lru():
    print()
    start_time = time.time()
    simple_cache(limit=3)
    finish_time = time.time() - start_time
    print(f"Finish: {finish_time}")

    start_time2 = time.time()
    simple_cache(limit=3)
    finish_time2 = time.time() - start_time2
    print(f"Finish: {finish_time2}")

    assert finish_time2 < finish_time
    assert finish_time2 == 0

    start_time = time.time()
    simple_cache(limit=2)
    print(f"Finish: {time.time() - start_time}")
