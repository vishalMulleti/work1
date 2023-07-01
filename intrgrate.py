import threading
import subprocess

def run_server():
    subprocess.call(["python", "server3.py"])  # 启动gradio脚本

def run_client3():
    subprocess.call(["python", "client3.py"])  # 启动Discord bot脚本


# 创建并启动三个线程
server_thread = threading.Thread(target=run_server)
client3_thread = threading.Thread(target=run_client3)


server_thread.start()
client3_thread.start()

