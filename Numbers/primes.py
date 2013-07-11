#!/usr/bin/env python
from heapq import *
import sys

def prime_gen():
    yield 2
    yield 3
    heap = []
    heappush(heap, (6,2))
    heappush(heap, (6,3))
    maybe_prime = 5
    while True:
        val, add = heappop(heap)
        if val == maybe_prime:
            heappush(heap, (val+ add, add))
            maybe_prime = maybe_prime+2
        if val > maybe_prime:
            yield maybe_prime
            heappush(heap, (maybe_prime * maybe_prime, maybe_prime))
            maybe_prime = maybe_prime+2
        heappush(heap, (val+add, add))

###Better version from stack overflow
def gen_primes():
    D = {}
    q = 2

    while True:
        if q not in D:
            yield q
            D[q*q] = [q]

        else:
            for p in D[q]:
                D.setdefault(p+1, []).append(p)
                del D[q]
        q += 1

if __name__ == '__main__':
    pg = gen_primes()
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        for i in range(n):
            print pg.next()

    else:
        while True:
            print pg.next()

