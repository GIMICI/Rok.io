# -*- coding: utf-8 -*-
import time
import os
from awesome_progress_bar import ProgressBar
import sys
import fake_shell

__menu__ = """+--------------------+
|   百灵公共后台v3.0  |
+--------------------+
请选择要进行的操作:
1.连接后台
2.攻击服务器
3.删库跑路[不建议尝试]
输入exit退出
"""

print(__menu__)

while True:
    answer = input(">>>")
    if answer == "1":
        bar = ProgressBar(100, "连接后台中...", use_thread=False, use_eta=True)
        for nul in range(100):
            time.sleep(0.05)
            bar.iter()
        shell = fake_shell.Shell()
        shell.run()
    elif answer == "2":
        qwp = input("宁确定要攻击吗？(Yes/No)")
        if qwp == "Yes" or "yes":
            os.system("ping -l 65500 127.0.0.1 -t")
        elif qwp == "No" or "no":
            break
        else:
            print("宁在说什么呢？爷听不懂！")
    elif answer == "3":
        print("Removing...")
        r = os.system("dir/s")
        print("清理完毕！")
        if r != 0:
            os.system("ls")
    elif answer == "exit":
        sys.exit(0)
    else:
        print("输入错啦")

# 屎山代码，勿喷
# 雀氏
