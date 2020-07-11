# 数据化运营的数据来源

## 数据来源类型

- 数据文件, txt, csv, tsv, json, excel, xml, html
- 数据库, mysql, sqlserver, oracle, mongodb
- API, JSON, XML
- 流式数据, Spark, Storm, Samza 等框架
  - 用户行为数据流
  - 机器数据流
- 外部公开数据
- 其他来源

## 文本读写

### read, readline, readlines

`file object = open(name [, mode][, buffering])`

> 常用 mode:

- `r`(默认): 只读, 文件指针指向文件开头;
- `r+`: 读写, 文件指针从文件头开始;
- `w`: 只写, 如果文件已存在则覆盖, 如果文件不存在则创建新文件;
- `w+`: 读写, 存在则覆盖, 不存在则新建;
- `a`: 追加, 文件已存在则指针指向文件结尾, 追加新内容, 如果文件不存在则新建;
- `a+`: 读写, 文件指针从文件尾开始;

`r+`, `w+`, `a+` 三者的区别:
`r+` 的读写, 指针是从文件头开始进行写入和读取; `w+` 的读写, 判断如果文件存在则会覆盖原文件, 不存在则会新建一个文件, 然后写入数据; `a+` 的读写, 指针是从文件末尾开始进行写入和读取;

> 读取文件内容的方法

- `read`: 读取全部数据, 所有行合并为一个字符串;
- `readline`: 读取一行数据;
- `readlines`: 读取全部数据, 每行一个字符串, 返回所有行的字符串列表;

> 关闭文件对象

```python
with open(file_path) as fn:
  content = fn.read()
```

### Numpy loadtxt, load, fromfile

#### `loadtxt`: 读取 txt 文本数据;

`loadtxt(fname, dtype=<type 'float'>, comments='#', delimiter=None, converters=None, skiprows=0, usecols=None, unpack=False, ndmin=0)`

- [ ] `fname`: 文件名称或字符串, 支持压缩的数据文件;
- [ ] `dtype`: 数据类型, 默认 `float`;
- [ ] `comments`: 指定注释字符集开始的标志, 默认 `#`;
- [ ] `delimiter`: 分隔多个列的分隔符, 默认为空格;
- [ ] `converters`: 字典, 将特定列的数据转换为字典中对应的函数的浮点型数据;
- [ ] `skiprows`: 跳过特定行数据;
- [ ] `usecols`: 元组, 指定要读取数据的列;
- [ ] `unpack`: 布尔型, 是否转置数组;
- [ ] `nadmin`: 整数型, 指定返回的数组至少包含特定维度的数组, 取值 0/1/2

#### `load`: 读取二进制数据文件;

`load(file, mmap_mode=None, allow_pickle=True, fix_imports=True, encoding='ASCII'`

- [ ] `file`: 类文件对象或字符串格式;
- [ ] `mmap_mode`: 内存映射模式, 取值 `None`, `r+`, `r`, `w+`, `c`;
- [ ] `allow_pickle`: 布尔型, 是否允许加载存储在 npy 文件中的 pickled 对象数组;
- [ ] `fix_imports`: 布尔型, 如果为 True, pickle 将尝试将旧的 `python2` 的名称映射到 `Python3` 中使用新名称;
- [ ] `encoding`: 编码;

#### `fromfile`: 读取简单的文本文件和二进制数据;

`fromfile(file, dtype=float, count=-1, sep='')`

通用用于读取 Numpy 的 `tofile` 方法产生的数据源;

- [ ] `file`: 文件或字符串;
- [ ] `dtpye`: 数据类型;
- [ ] `count`: 读取数据的数量, -1 表示所有数据;
- [ ] `sep`: 数据间的分隔符, 如果为空(""), 意味着文件是一个二进制文件;

### Pandas read_csv, read_fwf, read_table

#### `read_csv`: 读取 csv 文件

`read_csv(filepath_or_buffer, sep=',', delimiter=None, header='infer', names=None, index_col=None, usecols=None, **kwds)`

- [ ] `filepath_or_buffer`: 读取的文件对象;
- [ ] `sep`: 分隔符, 默认`,`, 多个分隔符号 `\|\+\|`(3个符号分隔);
- [ ] `names`: 列名;
- [ ] `engine`: 解析引擎, 默认`python`, 功能更全面; `c`引擎解析速度更快, 但是无法处理上面那种多个分隔符的情况;
- [ ] `skiprows`: 跳过的行或行数;
- [ ] `nrows`: 要读取的前记录总数;
- [ ] `na_values`: `NA` 值的表现字符串;
- [ ] `thousands`: 千位符符号, 默认为空;
- [ ] `decimal`: 小数点符号, 默认为`.`;
- [ ] `encoding`: 文件编码, 默认`utf-8`;

#### `read_fwf`: 读取表格或固定宽度格式的文本行数据

`read_fwf(filepath_or_buffer, colspecs='infer', widths=None, **kwds)`

- [ ] `widths`: 整数列表, 选填, 如果间隔是连续的, 可以使用字段宽度列表;

#### `read_table`: 读取通用分隔符分隔的数据

`read_table(filepath_or_buffer, sep='\t', delimiter=None, header='infer', names=None, index_col=None, usecols=None, **kwds)`

#### 其他数据读取方法

read_clipboard, read_excel, read_hdf, read_html, read_json, read_sql, read_sql_query, read_sql_table

## Excel 文件

`xlrd`, `xlwt`

## 关系型数据库 MySQL

`pymysql`

## 非关系型数据库 MongoDB

`pymongo`

## 从 API 获取数据

**百度地图开放平台**, <http://lbsyun.baidu.com/index.php?title=首页>

```python
import requests
add = '北京市中关村软件园'
ak = 'xxxxxxx'
url = "http://api.map.baidu.com/geocoding/v3/?address=%s&output=json&ak=%s"
res = requests.get(url % (add, ak))
add_info = res.text
print(add_info)
```

返回结果

```json
{
    "status": 0,
    "result": {
        "location": {
            "lng": "116.29997298581059",
            "lat": "40.05510109128797"
        },
        "precise": 0,
        "confidence": 50,
        "comprehension": 100,
        "level": "工业园区"
    }
}
```

## 从网页中获取数据

`requests`

## 读取非结构化文本数据

日志, 一般用 Python 自带的 `readlines` 方法读取然后再进行解析;

## 读取图像数据

`Pillow`, `OpenCV`(BGR), `Matplotlib`(RGB)

## 读取视频数据

`OpenCV`

```python
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
    if k == 27: # 判断是否输入 Esc
        break
cv2.destroyAllWindows()
cap.release()
```

**帧率(FPS)**: 每秒播放的帧数, 帧率越高, 图像越连贯, 越没有卡顿现象;
**帧分辨率**: 基本决定视屏的清晰度;

## 读取音频数据

`audioop`, `aifc`, `wav`

**百度语音API**, <http://yuyin.baidu.com/app>
