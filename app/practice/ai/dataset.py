from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# print(sns)

# dataset
from sklearn.datasets import fetch_california_housing

# 国勢調査のブロックグループごとにまとめた値
housing = fetch_california_housing()
df = pd.DataFrame(housing.data, columns=housing.feature_names)
df["Price"] = housing.target
df.head()
df.info()

# 統計値の読み込み
df.describe()
df.hist(bins=50, figsize=(15, 13))
# plt.show()

df.corr()
print(f"データタイプ\n {df}")

# 築年数, 住宅価格の最大値に不自然なデータがあるので修正
df = df[df["HouseAge"] < df["HouseAge"].max()]
df = df[df["Price"] < df["Price"].max()]

df.info()

df.hist(bins=50, figsize=(15,13))
plt.show()

# 説明変数・目的変数に分割
# 説明変数...結果に影響を与える要因 今回のカリフォルニア住宅価格の例だと、MedInc〜Longitudeが説明変数
# 目的変数...要因から影響を受けて起きた結果

# 説明変数
x = df.drop(["Price"], axis=1)
# 目的変数
y = df["Price"]

scaler = StandardScaler()
#標準化
x = scaler.fit_transform(x)