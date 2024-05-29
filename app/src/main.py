from module.index import MyClass, addFunc
from module.sample import hello, HelloClass

def main():
    obj = MyClass("Tom")
    obj.greet()

    result = addFunc(1,3)
    print(f"関数の結果 {result}")

# hello()

# このメインファイルが python main.pyのスクリプトで直接実行された場合のみif以下が実行される
# __main__にはモジュール名が入る
if __name__ == "__main__":
    print("__name__", __name__)
    main()
    print(hello.__name__)
    print(HelloClass.__name__)
else:
    print("このファイルがモジュールとして読み込まれるときの処理")
