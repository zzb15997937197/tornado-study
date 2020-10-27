# 将datetime时间转换为str类型格式的时间
import datetime

data_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(data_time, "类型为:", type(data_time))



