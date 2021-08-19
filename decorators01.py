""" Decorators in Python """


import time

import requests


def timeit(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"It took {end - start} seconds!")

    return wrapper


@timeit
def func1():
    n = 10_000_000
    while n > 0:
        n -= 1


@timeit
def func2():
    requests.get("https://httpbin.org/get")


@timeit
def func3():
    time.sleep(2)


func1()
func2()
func3()
