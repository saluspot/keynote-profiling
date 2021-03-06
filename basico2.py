#!/usr/bin/python2

import time
import profile

def myfunc1():
	time.sleep(0.01)

def myfunc2():
	time.sleep(0.001)

def myapp():
	for i in range(100):
		myfunc1()

	for i in range(100):
		myfunc2()

if __name__ == '__main__':
	profiler = profile.Profile()
	profiler.runcall(myapp)
	profiler.dump_stats('basico2.profile')
