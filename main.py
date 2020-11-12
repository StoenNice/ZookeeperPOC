from kazoo.client import KazooClient
import os
os.system("mode con cols=64 lines=20")
def Zookeeper(host):
    try:
        zk = KazooClient(hosts=host)
        print("开始检查是否存在Zookeeper未授权访问漏洞")
        zk.start()
        print(f"{host}存在该漏洞")
        for base in zk.get_children('/'):
            print(base)
        zk.stop()
    except BaseException as err:
        print(f"[ERROR] {host}", err)



while True:
    host = input("Zookeeper Address\nHost: ")
    Zookeeper(host)
    input("任意键继续")
    os.system("cls")