# ZADANIE 7.6 (ITERATORY)
# Stworzyć następujące iteratory nieskończone:
# (a) zwracający 0, 1, 0, 1, 0, 1, ...,
# (b) zwracający przypadkowo jedną wartość z ("N", "E", "S", "W") [błądzenie przypadkowe na sieci kwadratowej 2D],
# (c) zwracający 0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6, ... [numery dni tygodnia].

import itertools
import random

iterator_a = itertools.cycle([0, 1])
iterator_b = iter((lambda: random.choice(("N", "E", "S", "W"))), 1)
iterator_c = itertools.cycle([_ for _ in range(7)])

for _ in range(10):
    print("{0} \n{1} \n{2}\n----------------------------".format(next(iterator_a), next(iterator_b), next(iterator_c)))