from re import A
import pyaudio
import time
import threading
import datetime
import cv2
import numpy as np

A = 0

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paFloat32,
                channels=1,
                rate=44100,
                frames_per_buffer=1024,
                output=True)
samples = np.sin(np.arange(30))/5


def worker():
    global A
    t_start = datetime.datetime.now().time()
    for  i in range(6):
        stream.write(samples.astype(np.float32).tobytes())
        time.sleep(1)
    t_end = datetime.datetime.now().time()
    A += 1
    print(A,t_start,t_end)

   
   

def schedule(interval, f, wait=True):
    global A
    base_time = time.time()
    next_time = 0
    while True:
        t = threading.Thread(target=f)
        t.start()
        if wait:
            t.join()
        next_time = ((base_time - time.time()) % interval) or interval
        time.sleep(next_time)
        if A > 29 :
            break
time.sleep(10)
schedule(6,worker)