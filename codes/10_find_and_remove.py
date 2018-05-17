s1 = '今天天气非常非常的好'
s2 = '非常的'

while True:
    pos = s1.find(s2)
    if pos == -1:
       break 
    
    s_before = s1[:pos]
    s_after = s1[pos + len(s2):]
    s1 = s_before + s_after
    print(s1)
