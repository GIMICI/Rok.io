import time
import os
import sys
import linux

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

def ssh():
    print("Linux VM-0-8-debian 5.10.0-amd64 #1 SMP Debian 5.10.120-1 (2022-06-09) *86_64")
    print(" ")
    print("The programs included with the Debian GNU/Linux system are free software;")
    print("the exact distribution terms for each program are described in the individual files in /usr/shar/doc/*/copyright")
    print("individual files in /usr/share/doc/*/copyright.")
    print(" ")
    print("Debian GNU/Linux comes with ABSOLUTELY NO WARNTY, to the extent")
    print("permitted by applicable law.")
    print("Last login: Fri Aug 12 22:16:13 2022 from 36.152.44.96")
    while True:
        linux.qw()



print("+--------------------+")
print("|   百灵公共后台v3.0  |")
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
        ssh()       
    elif a=="2":
        aprogress_bar()
        qwp = input("宁确定要攻击吗？(Yes/No)")
        if qwp =="Yes" or "yes":
            os.system("ping -l 65500 127.0.0.1 -t")
        elif qwp == "No" or "no":
            break
        else:
            print("宁在说什么呢？爷听不懂！")
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

