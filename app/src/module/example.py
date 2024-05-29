import sys
import os

# 親ディレクトリをモジュールとして読み込むとき
# 現在のディレクトリ
current_dir = os.path.dirname(os.path.abspath(__file__))
# 一つ上
parent_dir = os.path.dirname(current_dir)
# sys.pathに追加
sys.path.append(parent_dir)

from main import main

if __name__ == "__main__":
    main()