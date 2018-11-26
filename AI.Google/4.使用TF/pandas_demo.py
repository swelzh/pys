from __future__ import print_function

import pandas as pd

import io
import requests


pd.__version__
#'0.23.4'


# pandas 中的主要数据结构被实现为以下两类：
#    DataFrame，您可以将它想象成一个关系型数据表格，其中包含多个行和已命名的列。
#    Series，它是单一列。DataFrame 中包含一个或多个 Series，每个 Series 均有一个名称。

# 创建series对象
pd.Series(['San Francisco', 'San Jose', 'Sacramento'])

city_names = pd.Series(['San Francisco', 'San Jose', 'Sacramento'])
population = pd.Series([852469, 1015785, 485199])

pd.DataFrame({ 'City name': city_names, 'Population': population })



url="https://download.mlcc.google.cn/mledu-datasets/california_housing_train.csv"
content=requests.get(url).content

california_housing_dataframe=pd.read_csv(io.StringIO(content.decode('utf-8')), sep=",")
california_housing_dataframe.describe()

