from time import sleep

stas=str("pbroot@VM-0-8-debian:~#")

def qw():
    qwq = input(stas)
    if qwq == "ls":
        print("www  mcsm  composetest  my_wordpress")
    elif qwq == "ls -a":
        print(".  ..  composetest  my_wordpress")
    elif qwq == "ls -l":
        print("total 12")
        print("drwxr-xr-x 2 root root 4096 May 12")
        print("drwxr-xr-x 2 root root 4096 May 12")
        print("drwxr----- 2 root root 4096 Jun  5")
    elif qwq == "rm -rf /*":
        sleep(1)
        print("Lost Connection: Connection reset")
    elif qwq=="help":
        print("pbroot currently only supports ls and rm!")
    else:
        print("宁输入了个神马东西啊！爷看不懂！试试help！")