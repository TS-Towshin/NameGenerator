import nameGenerator
import time
import os

i = input('Press Enter to start')
os.system('cls')
time1 = time.time()
while True:
    nameGenerator.NameGeneration()
    print(f'Time: {time.time()-time1} s')
