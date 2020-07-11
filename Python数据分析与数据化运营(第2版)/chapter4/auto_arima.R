# 加载库
if (!require('forecast'))
  install.packages('forecast')
library(forecast)
if (!require('Metrics'))
  install.packages('Metrics')
library(Metrics)

# 读取数据
raw_data <- read.csv("time_series.txt",header = TRUE, sep=',')

# 数据预处理
ts_data <- ts(raw_data$Orders) # 转换为时间序列格式
# 拆分数据
train_ts <- ts_data[1:100]
test_ts <- ts_data[101:nrow(raw_data)]

# 模型训练和校验
model <- auto.arima(train_ts,ic=c('aic'),trace=T) # 训练模型
summary(model) # 查看模型
in_ts_predict <- predict(model,(nrow(raw_data)-100)) # 检验数据
rmse(test_ts, in_ts_predict$pred) # 评估结果

# 重新训练模型并预测
model <- auto.arima(ts_data,ic=c('aic'),trace=T)
summary(model)
out_ts_predict <- forecast(model,10,levels=c(95)) # 预测未来10天数据
out_ts_predict$mean
#plot(forecast(model, h=10, level = c(95)),xlab="Time steps",ylab="Orders")
