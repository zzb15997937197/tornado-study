from tornado.httpclient import HTTPClient


# 同步I/O的操作拿到一个Url里的响应
def sync_visit():
    http_client = HTTPClient()
    print("请求开始!")
    content = http_client.fetch("http://www.baidu.com")  # 阻塞
    print(content.body.decode("utf-8"))
    print("请求结束!")


sync_visit()
