# バブルソート
# リストの隣り合ったデータを比較して、順番を変えていく
# numbers = [64, 34, 25, 12, 22, 11, 90]

# def bubble(data):
#     n = len(data)
#     for i in range(n):
#         print(n-i+1)
#         for j in range(0, n-i-1):
#             if data[j] > data[j+1]:
#                 data[j], data[j + 1] = data[j+1], data[j]
#     return data

# print(f"これはどうなる？？{bubble(numbers)}")

# 再起関数　自分自身を呼び出す
# forループなどを使用せずループ処理できる
# def total(n):
#     if n < 1:
#         return 0
    
#     return n + total(n - 1)

# print(total(10))

# def double_list(lst):
#     if lst == []:
#         return []

# マージソート(昇順)
# 分割してから統合する

# パリンドローム
# 前から呼んでも後ろから呼んでも同じ
# def is_palindrome(s):
#     s = ''.join(e for e in s if e.isalnum()).lower()
#     return s == s[::-1]

# string = input("Enter a string: ")
# if is_palindrome(string):
#     print(f"palindrome!! {string}")
# else:
#     print(f"not a palindrome... {string}")

import time

start = time.perf_counter()

def fizzbuzz():
    for i in range(1, 101):
        if(i % 15 == 0):
            print("fizzbuzz!!")
        elif(i % 3 == 0):
            print("fizz")
        elif(i % 5 == 0):
            print("buzz")
        else:
            print(i)        

fizzbuzz()
end = time.perf_counter()

start_recursive = time.perf_counter()
# 再帰関数に書き直し
def recursive(num):
    if num == 0:
        return
    recursive(num - 1)
    if num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    elif num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    else:
        print(num)
recursive(100)

end_recursive = time.perf_counter()

resultTime = (end - start) * 1000
recursive_time = (end_recursive - start_recursive) * 1000
    
print(f"速度: {resultTime}")
print(f"速度(再帰): {recursive_time}")