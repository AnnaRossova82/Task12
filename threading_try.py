import threading
import time


def handler(started=0, finished=0):
    result = 0
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    res = factorial(111)
    results.append(res)
params = {'finished': 111}

print(1, threading.active_count())
# Start with threading
results = []

task1 = threading.Thread(
    target=handler,
    kwargs=params
)
print(2, threading.active_count())
task2 = threading.Thread(
    target=handler,
    kwargs=params
)
print(3, threading.active_count())
task3 = threading.Thread(
    target=handler,
    kwargs=params
)
started_at = time.time()

task1.start()
task2.start()
task3.start()
print(4, threading.active_count())
task1.join()
task2.join()
task3.join()

print('RESULTS 1')
print(f'Time: {time.time() - started_at}')
print('Value: ', sum(results))

print(5, threading.active_count())
# Start without threading
results = []
started_at = time.time()
handler(finished=111)
print('RESULTS 2')
print(f'Time: {time.time() - started_at}')


