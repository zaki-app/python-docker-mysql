"""
並列処理のサンプル
"""

import threading

# 通常のマルチスレッド
def print_number():
    for i in range(10):
        print(f" {i}")

def print_letters():
    for letter in "abcdefghijk":
        print(f" {letter}")

t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

# マルチプロセッシング
# スレッドの代わりにプロセスを作成するが、GILの制約がなくなるが消費リソースが高くなる
from multiprocessing import Process

def processing_numbers():
    for i in range(10):
        print(f" {i}")

def processing_letters():
    for letter in "abcdefghijk":
        print(f" {letter}")

p1 = Process(target=processing_numbers)
p2 = Process(target=processing_letters)

p1.start()
p2.start()

p1.join()
p2.join()

# 非同期
import asyncio

async def async_numbers():
    for i in range(10):
        print(f" {i}")

async def async_letters():
    for letter in "abcdefghijk":
        print(f" {letter}")

async def async_main():
    task1 = asyncio.create_task(async_numbers)
    task2 = asyncio.create_task(async_letters)

    await task1
    await task2

asyncio.run(async_main())