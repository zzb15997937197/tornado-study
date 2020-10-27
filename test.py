# 将datetime时间转换为str类型格式的时间
import datetime

data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(data_time, "类型为:", type(data_time))

import tornado.web

if __name__ == "__main__":
    data = {"name": "zhangzhengbing", "age": 20}
    # 转义为Json
    data = tornado.escape.json_encode(data)
    print(data, "类型为:", type(data))
    # 将Json字符串转换python对象
    data = tornado.escape.json_decode(data)
    print(data, "类型为:", type(data))
