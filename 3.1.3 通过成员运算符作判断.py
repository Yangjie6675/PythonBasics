print('''请根据对应的号码选择一个路由协议：
1. RIP
2. IGRP
3. EIGRP
4. OSPF
5. ISIS
6. BGP''')

option = input('请输入你的选项（数字1-6）：')  # input()：它的作用是提示用户输入数据与Python程序互动；input()的返回值是字符串。

if option.isdigit() and int(option) in list(range(1, 7)): # 使用字符串isdigit()方法，判断输入的字符串是否为整数。使用int()函数将字符串转换成整数类型，再通过比较运算符判断条件是否成立。将这两个判断条件通过逻辑运算符and来判断它俩是否同时成立（两者都满足条件）
    if int(option) in list(range(1, 4)):
        print('该路由协议属于距离矢量路由协议。')
    elif int(option) in list(range(4, 6)): # 使用成员运算符来判断用户输入的选项号码是否在该整数列表中。
        print('该路由协议属于链路状态路由协议。')
    else:
        print('该路由协议属于路径适量路由协议。')
else:
    print('选项无效，程序终止。')
