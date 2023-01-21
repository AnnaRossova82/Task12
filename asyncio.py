import socket
import asyncio
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.connect(('localhost', 55000))
sock.listen(11)
while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024).decode('utf-8')
        print('Message', result.decode('utf-8'))
        getinfo = str(result)
        client.close()
#take x and y from info received by server from client

x = int(input())
y = int(input())

async def adding_two_num(x, y):
    print(x + y)
    print('Running in add')
    await asyncio.sleep(2)
    print('Explicit context switch to adding_two again')

async def minus_two(x, y):
    print(x - y)
    print('Explicit context to minus_two')
    await asyncio.sleep(1)
    print('Implicit context switch back to minus_two')

async def multiply_two(x, y):
    print(x * y)
    print('Explicit context to multiply_two')
    await asyncio.sleep(2)
    print('Implicit context switch back to multiply_two')

ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(adding_two_num(x, y)), ioloop.create_task(minus_two(x, y)), ioloop.create_task(multiply_two(x, y))]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()
