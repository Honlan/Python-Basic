def find_and_remove(s1, s2, flag):
    pos = s1.find(s2)
    if pos == -1:
        return s1

    if flag:
        # 全部删除
        while True:
            pos = s1.find(s2)
            if pos == -1:
                break
            s1 = s1[:pos] + s1[pos + len(s2):]
        return s1
    else:
        # 只删一次
        return s1[:pos] + s1[pos + len(s2):]

print(find_and_remove('你好啊你好啊', '我不好', True))
print(find_and_remove('今天天气非常非常非常的好', '非常', False))
print(find_and_remove('今天天气非常非常非常的好', '非常', True))
print('=' * 10)
print('今天天气非常非常非常的好'.replace('非常', ''))
print('今天天气非常非常非常的好'.replace('非常', '', 1))







