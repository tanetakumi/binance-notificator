import time
from multiprocessing import Process

import discord
from multiprocessing import Manager
from concurrent.futures import ProcessPoolExecutor
import asyncio

class TestClass():
    def test_f(self):
        ctr = 0
        while True:
            ctr += 1
            print("     ", ctr)
            time.sleep(1.0)
 
if __name__ == '__main__':
    ## run function in the background
    ## will not exit if function finishes, only when
    ## "q" is entered, but this is just a simple exampleq
    CT = TestClass()
    p = Process(target=CT.test_f)
    p.start()


    stop_char=""
    while stop_char.lower() != "q":
        stop_char=input("Enter 'q' to quit ")
        if stop_char.lower() == "u":
            print("Hello")
            ## do something else

    print("terminate process")
    if p.is_alive():
        p.terminate()