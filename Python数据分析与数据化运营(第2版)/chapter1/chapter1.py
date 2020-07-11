#%%
# 1. 导入库
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

#%%
# 2. 读取数据
raw_data = pd.read_csv('data.txt')

#%%
# 3. 数据预处理
num = int(raw_data.shape[0] * 0.7)
x, y = raw_data[['money']], raw_data[['amount']]
x_train, x_test = x[:num], x[num:]
y_train, y_test = y[:num], y[num:]

#%%
# 4. 探索性数据分析
# 散点图观察
plt.scatter(x_train, y_train)

# %%
# 5. 数据建模
model = linear_model.LinearRegression()
model.fit(x_train, y_train)

#%%
# 6. 模型评估
predict_test_y = model.predict(x_test)
print("Mean squared error: %.0f" % mean_squared_error(y_test, predict_test_y))
print("Variance score: %.2f" % r2_score(y_test, predict_test_y))

# %%
# 7. 线性回归参数
model_coef = model.coef_
model_intercept = model.intercept_
print("coef is: ", model_coef)
print("intercept is: ", model_intercept)

# %%
# 8. 销售预测应用
new_x = 84610
pre_y = model.predict([[new_x]])
print(pre_y)