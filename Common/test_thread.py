import threading
from threading import Thread
from time import sleep, ctime
import requests
url = "http://127.0.0.1:5000/api/v1.0/upload"
class Person(object):
	age = 18

	def __init__(self,age):
		self.age = age


def thr_fn():
    print('..%s...' % threading.current_thread().name)
    sleep(3)

loops = [4, 2]
nloops = range(len(loops))


def main():
    threads = []
    for i in nloops:
        t = Thread(target=thr_fn)
        threads.append(t)

    for j in nloops:
        threads[j].start()

if __name__ == '__main__':
    files = {'file': open('/Users/daniel/Downloads/jl.pdf','rb')}
    r = requests.post(url, files=files)
    