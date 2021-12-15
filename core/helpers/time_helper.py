import functools

import time


def time_execution(f):
    @functools.wraps(f)
    def timed(*args, **kw):
        start_t = time.time()

        result = f(*args, **kw)

        end_t = time.time()

        print('%r - %2.2f seconds' % (f.__name__, abs(start_t - end_t)))

        return result

    return timed
