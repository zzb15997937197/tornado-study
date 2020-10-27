import tornado.web

'''
tornado的 escape用法
'''

if __name__ == "__main__":
    data = {"name": "bingbing", "age": 20}
    # 1. python对象与json互相转换
    # 转义为Json
    data = tornado.escape.json_encode(data)
    print(data, "类型为:", type(data))
    # 将Json字符串转换python对象
    data = tornado.escape.json_decode(data)
    print(data, "类型为:", type(data))
    # 2. 转义字符串或者方法，以便在xml或者HTML中生效
    # 转义字符串
    name = tornado.escape.xhtml_escape("<123>")
    print(name)
    # 打印结果: &lt;123&gt;
    # 取消字符串的转义
    name = tornado.escape.xhtml_unescape(name)
    print(name)

    # 3. byte 与unicode之间的转换
    # 1)将字符串转换为字节字符串
    s = "bingbing"
    s = tornado.escape.utf8(s)
    print(s, "类型为:", type(s))
    # 打印结果: b'bingbing' 类型为: <class 'bytes'>
    # 2) 将字符串或者字节字符串转换为unicode字符串, tornado.escape.to_unicode()
    s2 = "bingbing"
    s2 = tornado.escape.to_unicode(s2)
    print(s2, "类型为:", type(s2))
    # 打印结果: bingbing 类型为: <class 'str'>, 如果to_unicode是字符串或者""，那么返回原样
    s = tornado.escape.to_unicode(s)
    print(s, type(s))
    # 打印结果: bingbing <class 'str'>,可以发现将字节字符串转换为了字符串。
    # 3) 将字节字符串转换字符串
    s = tornado.escape.recursive_unicode(s)
    print(s, type(s))
    # 打印结果: bingbing <class 'str'>, tornado.escape.recursive_unicode(obj),支持列表元组和字典。
    s = [1, 2, 3]
    s = tornado.escape.recursive_unicode(s)
    print(s, type(s))
    # 打印结果: [1, 2, 3] <class 'list'>
    s = ("1", "<2", "3")
    s = tornado.escape.recursive_unicode(s)
    print(s, type(s))
    s = tornado.escape.json_encode(s)
    print(s, type(s))
    s = tornado.escape.utf8(s)
    print(s, type(s))
    s = tornado.escape.recursive_unicode(s)
    print(s, type(s))
    # 转成python对象
    s = tornado.escape.json_decode(s)
    print(s, type(s))
    # 转换成元组
    s = tuple(s)
    print(s)
    # 4. tornado.escape.linkify(
    # text,
    # shorten=False,
    # extra_params='',
    # require_protocol=False,
    # permitted_protocols=['http', 'https'])
    # 将使用的http或者https链接转换为html标签进行返回
    url = tornado.escape.linkify("hello https://www.baidu.com", shorten=True, permitted_protocols=['http', 'https'])
    print(url)

    # 5. tornado.escape.squeeze(value),去掉前后空格，中间的空格使用一个空格替代,相当于将字符串进行挤压
    name = "  Anastasia     Cassandra   tom "
    name = tornado.escape.squeeze(name)
    print(name)
    # 打印结果: Anastasia Cassandra tom
