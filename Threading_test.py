# coding=utf-8

import threading
import time
import urllib.request

# 线程停止变量
isrunning = True


# 工作线程体函数
def workthread_body():
    # 创建当前线程对象
    while isrunning:
        print('工作线程执行下载任务……')
        download()
        time.sleep(5)
    print("工作线程结束……")


# 控制线程体函数
def controlthread_body():
    global isrunning  # 因为要修改isrunning的值，所以将isrunning声明为global
    # 创建当前线程对象
    while isrunning:
        command = input("请输入停止指令（exit）：")
        if command == "exit":
            isrunning = False
            print('控制线程结束')

def download():
    url = 'https://img2.woyaogexing.com/2021/03/22/346bf6c38fb340329370c6937d9d64f7!400x400.jpeg'
    req = urllib.request.Request
    with urllib.request.urlopen(url) as response:
        data = response.read()
        f_name = 'dowanload.png'
        with open(f_name,'wb') as f:
            f.write(data)
            print("文件下载成功")

# 创建工作线程对象
t1 = threading.Thread(target=workthread_body)
# 启动线程t1
t1.start()
# 创建控制线程对象
t2 = threading.Thread(target=controlthread_body)
t2.start()
