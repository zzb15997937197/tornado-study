# 自定义一个生成器
# yield的作用是将yield定义的结果作为迭代返回元素。
# 在python中使用yield 定义的迭代器称为生成器。
def demoIterator():
    print("first next()")
    yield 1
    print("second next()")
    yield 2
    print("third next()")
    yield 3


for i in demoIterator():
    print(i)
