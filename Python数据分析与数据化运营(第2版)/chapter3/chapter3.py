#%%
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

#%%
df = pd.DataFrame(np.random.randn(6, 4),
                  columns=['col1', 'col2', 'col3', 'col4'])
df.iloc[1:2, 1] = np.nan
df.iloc[4, 3] = np.nan
print(df)

# %%
nan_all = df.isnull()
print(nan_all)
nan_col1 = df.isnull().any()
nan_col2 = df.isnull().all()
print(nan_col1)
print(nan_col2)

#%%
df2 = df.dropna()
print(df2)

#%%
nan_model = SimpleImputer(missing_values=np.nan, strategy='mean')
nan_result = nan_model.fit_transform(df)
print(nan_result)

#%%
# 用后面的值替换缺失值
nan_result_pd1 = df.fillna(method='backfill')
# 用后面的值替换缺失值, 限制每列只能替换一个缺失值
nan_result_pd2 = df.fillna(method='bfill', limit=1)
# 用前面的值替换缺失值
nan_result_pd3 = df.fillna(method='pad')
nan_result_pd4 = df.fillna(0)
# 不同列用不同的值替换缺失值
nan_result_pd5 = df.fillna({'col2': 1.1, 'col4': 1.2})
# 用各自列的平均数替换缺失值
nan_result_pd6 = df.fillna(df.mean()['col2':'col4'])
print(nan_result_pd1)
print(nan_result_pd2)
print(nan_result_pd3)
print(nan_result_pd4)
print(nan_result_pd5)
print(nan_result_pd6)

#%%
# 异常值的处理
import pandas as pd
df = pd.DataFrame({
    'col1': [1, 120, 2, 5, 2, 12, 13],
    'col2': [12, 17, 31, 53, 22, 32, 43]
})
print(df)

#%%
# 通过 z-score 方法判断异常值
df_zscore = df.copy()
cols = df.columns
for col in cols:
    df_col = df[col]
    z_score = (df_col - df_col.mean()) / df_col.std()
    df_zscore[col] = z_score.abs() > 2.2
print(df_zscore)

#%%
# 删除异常值所在行
df_drop_outlier = df[df_zscore['col1'] == False]
print(df_drop_outlier)

#%%
# 重复值处理
import pandas as pd
data1, data2, data3, data4 = ['a', 3], ['b', 2], ['a', 3], ['c', 2]
df = pd.DataFrame([data1, data2, data3, data4], columns=['col1', 'col2'])
print(df)

#%%
isDuplicated = df.duplicated()
print(isDuplicated)

#%%
print(df.drop_duplicates())
print(df.drop_duplicates(['col1']))
print(df.drop_duplicates(['col2']))
print(df.drop_duplicates(['col1', 'col2']))

#%%
# 标志转换
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

#%%
df = pd.DataFrame({
    'id': [3566841, 6541227, 3512441],
    'sex': ['male', 'Female', 'Female'],
    'level': ['hight', 'low', 'middle'],
    'score': ['1', '2', '3']
})
print(df)

#%%
id_data = df[['id']]
raw_convert_data = df.iloc[:, 1:]
print(raw_convert_data)

#%%
model_enc = OneHotEncoder()
df_new2 = model_enc.fit_transform(raw_convert_data).toarray()
print(df_new2)

#%%
df_all = pd.concat((id_data, pd.DataFrame(df_new2)), axis=1)
print(df_all)

#%%
df_new3 = pd.get_dummies(raw_convert_data)
df_all2 = pd.concat((id_data, pd.DataFrame(df_new3)), axis=1)
print(df_all2)