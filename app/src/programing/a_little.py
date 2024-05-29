# 少し難しいPython問題

# ユーザーから入力された数以下のフィボナッチ数列を表示する
# inputNum = int(input("お好きな数字からフィボナッチ数列を返却します"))

# def fibonacci(n):
#     flb_sequence = [0,1]
#     while flb_sequence[-1] + flb_sequence[-2] <= n:
#         flb_sequence.append(flb_sequence[-1] + flb_sequence[-2])
#     return flb_sequence

# result = fibonacci(inputNum)
# print(result)

# ユーザーから入力された数が素数かどうかを判定する
# inputNum = int(input("素数判断しますので好きな数字を入力してください"))

# # def is_prime(n):
# #     if n <= 1:
# #         return False
# #     elif n <= 3:
# #         return True
# #     elif n % 2 == 0 or n % 3 == 0:
# #         return False
# #     i = 5
# #     while i * i <= n:
# #         if n % i == 0 or n % (i + 2) == 0:
# #             return False
# #         i += 6
# #     return True

# # if is_prime(inputNum):
# #     print(f"素数です {inputNum}")
# # else:
# #     print(f"素数じゃない {inputNum}")

# def is_prime(n):
#     # 1や1以下は割れないので素数じゃない
#     if n <= 1:
#         return False
#     # 2以上の場合与えられた数値まで割れるか判断する
#     # nの平方根を計算し(n**0.5)、最後に1をプラスする
#     for i in range(2, int(n**0.5) + 1):
#         if n % i ==0:
#             return False
#     return True

# result = is_prime(inputNum)

# if result:
#     print(f"素数です {inputNum}")
# else:
#     print(f"素数じゃない {inputNum}")

# 複数の文字からアナグラムを生成する
# strInput = input("2つの単語を入力してください").split()

# print(strInput)

# def groupingA(strs):
#     hasMap = {}

#     for s in strs:
#         # 文字をアルファベット順にソート
#         key = "".join(sorted(s))
#         print(key)
        
#         if key not in hasMap.keys():
#             hasMap[key] = [s]
#         else:
#             hasMap[key].append(s)

#     print(f"hashMap: {hasMap}")
#     return hasMap

# print(groupingA(strInput))

# 与えられたリスト内の重複した要素を削除し、重複がない新しいリストを返す
numbers = [1, 2, 3, 4, 2, 3, 5, 6, 6, 7]

result = list(set(numbers))
print(result)