from multiprocessing import Pool
from multiprocessing import Process
import time
import os

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
res = factorial(99)
print(res)

if __name__ == '__main__':
    cpu = os.cpu_count()
    print(f"Your PC has {cpu} cores(((")

started_at = time.time()
print([factorial(n) for n in range(1, 15)])
print([factorial(n) for n in range(1, 30)])
print("searching for time1 just experiment")
print(f"Time1: {time.time() - started_at}")
FirstTime=(f"Time1: {time.time() - started_at}")

if __name__ == '__main__':
    with Pool(cpu) as p:
        started_at = time.time()
        print(p.map(factorial, range(1, 30)))
        print("searching for Time2 for check")
        print(f'Time2:{time.time() - started_at}')
        SecondTime=(f'Time2:{time.time() - started_at}')

def info(title):
    print(title)
    print('module name', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

if __name__ == '__main__':
    info('main line')
    print("searching for time 3")
    p = Process(target=factorial, args=(14,))
    p.start()
    p.join()
    print(f'Time3:{time.time() - started_at}')
    ThirdTime=(f'Time3:{time.time() - started_at}')

"""
SimpleCheck = 0.000997781753540039
PoolCheck = 0.20687174797058105
ProcessCheck = 0.4966926574707031
List = [0.000997781753540039, 0.20687174797058105, 0.4966926574707031]
min = List[0]
for i in range(1, len(List)):
    if i[List] < min:
        min = i[list]
        print(min)
#simpe check without ThreadPool and ProcessPool is the faster

"""
