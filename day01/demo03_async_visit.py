from tornado.httpclient import AsyncHTTPClient


def handle_response(response):
    print("回调处理！")
    print(response.body)


# 异步I/O的操作拿到一个Url里的响应
def sync_visit():
    for i in range(0, 10000):
        print("请求开始")
        http_client = AsyncHTTPClient()
        future = http_client.fetch("http://www.baidu.com", callback=handle_response)  # 异步
        print(future)
        print("请求结束")


sync_visit()
