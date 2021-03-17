import time

def begin():
    print("loop started")

def midden():
    for i in range(1, 10):
        print("loop ", i)
        time.sleep(1)

def eind():
    print("loop finished")

begin()
midden()
eind()
