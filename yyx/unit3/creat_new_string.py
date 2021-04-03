'''
字符串生成（Creat New String）
描述
完成一个Python程序，要求由用户输入一段英文文本，程序返回由该段文本中的前两个和后两个字符组成的新的字符串。如果给定的文本长度少于2，那么返回“Empty String”
'''
str = input("")
if len(str) < 2:
    print("Empty String")
else:
    str1 = str[:2]
    str2 = str[-2:]
    print(str1+str2)
