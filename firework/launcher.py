from subprocess import run
from os import getuid

banner = r'''
 _____ _                             _
|  ___(_)_ __ _____      _____  _ __| | __
| |_  | | '__/ _ \ \ /\ / / _ \| '__| |/ /
|  _| | | | |  __/\ V  V / (_) | |  |   <
|_|   |_|_|  \___| \_/\_/ \___/|_|  |_|\_\

'''


def firework():
    run(['sudo', 'python3', 'main.py'])
    return '[*] Queue unbinded'


def firemodule(mode):
    if mode == 'insmod':
        insert = run(['sudo', 'insmod', 'kernel_module/firemodule.ko'], capture_output=True, text=True).stderr
        if insert == '':
            return '[*] Kernel module inserted'
        elif 'File exists' in insert:
            return '[!] Kernel module has already been inserted'
        else:
            return f'[!] {insert}'

    elif mode == 'rmmod':
        insert = run(['sudo', 'rmmod', 'firemodule'], capture_output=True, text=True).stderr
        if insert == '':
            return '[*] Kernel module removed'
        else:
            return f'[!] {insert}'


def main():
    print(banner)
    if getuid() == 0:
        print('[!] Running from root can cause security issues')
        print('[!] Run Firework not as root\n')
    try:
        print(firemodule('insmod'))
        print(firework())
        print(firemodule('rmmod'))
    except KeyboardInterrupt:
        print(firemodule('rmmod'))


if __name__ == '__main__':
    main()
