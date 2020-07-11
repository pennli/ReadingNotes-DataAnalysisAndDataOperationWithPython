#%%
# 1. 文本文件
file_name = 'text.txt'

with open(file_name) as fn:
    print(fn.tell())
    print(fn.read())
    print(fn.tell())
    print(fn.readline())
    print(fn.tell())
    print(fn.readlines())

# %%
import numpy as np
file_name = 'numpy_data.txt'
data = np.loadtxt(file_name, dtype='float32', delimiter=' ')
print(data)

# %%
write_data = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
np.save('load_data', write_data)
read_data = np.load('load_data.npy')
print(read_data)

# %%
file_name = 'numpy_data.txt'
data = np.loadtxt(file_name, dtype='float32', delimiter=' ')
tofile_name = "binary"
data.tofile(tofile_name)
fromfile_data = np.fromfile(tofile_name, dtype='float32')
print(fromfile_data)

# %%
import pandas as pd
csv_data = pd.read_csv('csv_data.csv',
                       names=['col1', 'col2', 'col3', 'col4', 'col5'])
print(csv_data)

#%%
fwf_data = pd.read_fwf('fwf_data',
                       widths=[5, 5, 5, 5],
                       names=['col1', 'col2', 'col3', 'col4'])
print(fwf_data)

#%%
table_data = pd.read_table('table_data.txt',
                           sep=';',
                           names=['col1', 'col2', 'col3', 'col4', 'col5'])
print(table_data)

#%%
import xlrd
xlsx = xlrd.open_workbook('demo.xlsx')
print("All sheets: %s" % xlsx.sheet_names())
sheet1 = xlsx.sheets()[0]
sheet1_name = sheet1.name
sheet1_cols = sheet1.ncols
sheet1_nrows = sheet1.nrows
print("Sheet1 Name: %s\nSheet1 cols: %s\nSheet1 rows: %s" %
      (sheet1_name, sheet1_cols, sheet1_nrows))

sheet1_nrow4 = sheet1.row_values(4)
sheet1_cols2 = sheet1.col_values(2)
cell23 = sheet1.row(2)[3].value
print('Row 4: %s\nCol 2: %s\nCell 1: %s' %
      (sheet1_nrow4, sheet1_cols2, cell23))

for i in range(sheet1_nrows):
    print(sheet1.row_values(i))

#%%
import pymysql
config = {
    'host': '127.0.0.1',
    "user": 'root',
    "password": '123456',
    "port": 3306,
    "database": "cnblog",
    "charset": "utf8"
}
conn = pymysql.connect(**config)
cursor = conn.cursor()
sql = "SELECT * FROM news"
cursor.execute(sql)
data = cursor.fetchall()
for i in data[:2]:
    print(i)
cursor.close()
conn.close()

#%%
# 百度地图开放平台 API
import requests
add = '北京市中关村软件园'
ak = 'qnE4sZc4ukbuiZ0NonqZZWO66qfvtA42'
url = "http://api.map.baidu.com/geocoding/v3/?address=%s&output=json&ak=%s"
res = requests.get(url % (add, ak))
add_info = res.text
print(add_info)

import json
add_json = json.loads(add_info)
lat_lng = add_json['result']['location']
print(lat_lng)

#%%
from PIL import Image
file = 'cat.jpg'
img = Image.open(file, mode='r')
# img.show()
print("img format: ", img.format)
print("img size: ", img.size)
print("img mode: ", img.mode)

img_gray = img.convert('L')
img_gray.show()

#%%
import cv2
file = 'cat.jpg'
img = cv2.imread(file)
cv2.imshow('image', img)
cv2.waitKey(0)

# %%
# 通过 Matplotlib 显示 opencv 读取的图像
import matplotlib.pyplot as plt
import cv2
file = 'cat.jpg'

img = cv2.imread(file)
b, g, r = cv2.split(img)
img2 = cv2.merge([r, g, b])

plt.subplot(121)
plt.title('plt BGR image')
plt.imshow(img)
plt.subplot(122)
plt.title('plt RGB image')
plt.imshow(img2)

cv2.imshow('OpenCv BGR image', img)
cv2.imshow('OpenCv RGB image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# %%
# 读取视频数据
import cv2
cap = cv2.VideoCapture('tree.avi')
status = cap.isOpened()
if status:
    # 帧宽度
    frame_width = cap.get(3)
    # 帧高度
    frame_height = cap.get(4)
    # 总帧数
    frame_count = cap.get(7)
    # 帧速率
    frame_fps = cap.get(5)
    print('frame width: ', frame_width)
    print('frame height: ', frame_height)
    print('frame count: ', frame_count)
    print('frame fps: ', frame_fps)

success, frame = cap.read()
while success:
    cv2.imshow('video frame', frame)  # 展示帧图像
    success, frame = cap.read()  # 获取下一帧
    k = cv2.waitKey(int(1000 / frame_fps))  # 每次帧播放延迟一定时间, 同时等待输入指令
    if k == 27:  # 判断是否输入 Esc
        break
cv2.destroyAllWindows()
cap.release()

# %%
