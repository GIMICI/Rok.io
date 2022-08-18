import time
import re
import random
import sys

# permission denied
__motd__ = """Linux VM-0-8-fuckos 5.10.0-nvidia64 #1 SMP fuckos 11.45.14 (2022-06-09) *nvidia86_64")

The programs included with the GNU/Linux not system are free software;
the exact distribution terms for each program are described in the individual files in (Actually I don't know)
individual files in (I don't know where it is, either).

Fuckos GNU/Linux comes with ABSOLUTELY NO WARNTY, to the extent
permitted by applicable law.
Last login: Fri Aug 12 22:16:13 2022 from {ip}
"""

__files_storage__ = {
    '/': [
        {
            "type": "directory",
            "name": "usr",
            "owner": "root",
            "permission": 755
        },
        {
            "type": "link",
            "name": "bin",
            "link": {
                "to": "/usr/bin"
            },
            "owner": "root",
            "permission": 755
        },
        {
            "type": "directory",
            "name": "opt",
            "owner": "root",
            "permission": 755
        },
        {
            "type": "link",
            "name": "lib",
            "link": {
                "to": "/usr/lib"
            },
            "owner": "root",
            "permission": 755
        },
        {
            "type": "directory",
            "name": "root",
            "owner": "root",
            "permission": 755
        },
    ]
}

__permissions_flags__ = {
    0: '---',
    1: '--x',
    2: '-w-',
    3: '-wx',
    4: 'r--',
    5: 'r-x',
    6: 'rw-',
    7: 'rwx'
}


def random_ip():
    """

    :return:
    """
    ip = ''
    for i in range(4):
        ip += str(random.randint(0, 255))
        if i >= 3:
            break
        ip += '.'

    return ip


def file_type_processor(name: str) -> str:
    """

    :param name:
    :return:
    """
    if name == 'file':
        return '-'
    else:
        return name[0]


def permission_processor(code: int) -> str:
    """

    :param code:
    :return:
    """
    full_permission = ""
    code_str = str(code)
    for each_byte in code_str:
        full_permission += __permissions_flags__[int(each_byte)]
    return full_permission


def command_ls(pwd: str) -> str:
    """

    :param pwd:
    :return:
    """
    if pwd in __files_storage__.keys():
        result = ''
        result += 'Total NaN\n'
        for each_file in __files_storage__[pwd]:
            if each_file['type'] != 'link':
                result += "{type}{permission}   <爷不知道这是啥> {owner} {owner}   <爷不知道这是啥> <爷懒得写时间> {name}".format(
                    type=file_type_processor(each_file['type']),
                    permission=permission_processor(each_file['permission']),
                    owner=each_file['owner'], name=each_file['name']
                )
            else:
                result += "{type}{permission}   <爷不知道这是啥> {owner} {owner}   <爷不知道这是啥> <爷懒得写时间> {name} " \
                          "-> {link_to}".format(
                                                    type=file_type_processor(each_file['type']),
                                                    permission=permission_processor(each_file['permission']),
                                                    owner=each_file['owner'], name=each_file['name'],
                                                    link_to=each_file['link']['to']
                )
            result += '\n'
        return result
    else:
        return "dude, that's not answer directiony! (%s)" % pwd


class Shell(object):
    def __init__(self, ps1: str = "root@VM-0-8-debian:~# ", delay: float = 0.2, default_pwd: str = '/'):
        """

        :param ps1:
        :param delay:
        :param default_pwd:
        """
        self.ps1 = ps1
        self.delay = delay
        self.default_pwd = default_pwd

    def run(self):
        """

        :return:
        """
        envs = {
            'PWD': self.default_pwd
        }

        print(__motd__.format(ip=random_ip()))
        time.sleep(self.delay)

        while True:
            command = input(self.ps1)
            time.sleep(self.delay)
            if re.search(r'^ls', command):
                selected_pwd = re.match(r'^ls ?(.*)', command).group(1)
                if selected_pwd == '':
                    print(command_ls(envs['PWD']))
                else:
                    print(command_ls(selected_pwd))
            elif re.search(r'^exit', command):
                sys.exit(0)


if __name__ == '__main__':
    shell = Shell()
    shell.run()
