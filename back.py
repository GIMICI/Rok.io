import time
import os
import sys

def progress_bar():
    for i in range(1,101):
        print("\r",end="")
        print("加载中.....{}%:".format(i),"|" * (i//2),end="")
        sys.stdout.flush()
        time.sleep(0.05)

def aprogress_bar():
    for i in range(1,101):
        print("\r",end="")
        print("攻击.....{}%:".format(i),"|" * (i//2),end="")
        sys.stdout.flush()
        time.sleep(0.05)


print("+--------------------+")
print("|   百灵公共后台v1.0  |")
print("+--------------------+")
print("请选择要进行的操作:")
print("1.连接后台")
print("2.攻击服务器")
print("3.删库跑路[不建议尝试]")
print("输入exit退出")
while True:
    a = input(">>>")
    if a == "1":
        progress_bar()
        print("宁以为这里能连？当然不行！")        
    elif a=="2":
        aprogress_bar()
        print("攻击完成！")
    elif a=="3":
        progress_bar()
        print("Removing...")
        r=os.system("dir/s")
        print("清理完毕！")
        if r!=0:
            os.system("ls")
    elif a=="exit":
        sys.exit(0)
    else:
        print("输入错啦")


#屎山代码，勿喷

