#!/usr/bin/python3

import time
import timeit

def myfunc1():
	time.sleep(0.01)

def myfunc2():
	time.sleep(0.001)

if __name__ == '__main__':
	print({
		'myfunc1': timeit.timeit(myfunc1, number=100),
		'myfunc2': timeit.timeit(myfunc2, number=100)
		})
