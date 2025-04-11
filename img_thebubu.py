from tkinter import Tk, Label
from PIL import Image, ImageTk
import random
import os

def xbyly():
    # 获取当前脚本所在目录的绝对路径
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # 随机选择图片
    img_random_bubu = random.randint(1, 2)

    # 创建主窗口
    root = Tk()

    # 设置窗口标题和图片路径
    if img_random_bubu == 1:
        root.title("小黑塔~")
        img_path = os.path.join(current_dir, "img", "2.jpg")  # 替换为你的图片路径
    elif img_random_bubu == 2:
        root.title("大安比~")
        img_path = os.path.join(current_dir, "img", "1.webp")  # 替换为你的图片路径

    # 打开并调整图片大小
    try:
        image = Image.open(img_path)
        image = image.resize((360, 360))
        tk_image = ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image: {e}")
        # 如果图片加载失败，可以显示一个默认的提示
        tk_image = None

    # 设置窗口位置和大小
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    window_width = 300
    window_height = 300
    x = random.randint(0, screen_width - window_width)
    y = random.randint(0, screen_height - window_height)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 创建标签并显示图片
    if tk_image:
        label = Label(root, image=tk_image)
        label.image = tk_image  # 保留对图片的引用，防止被垃圾回收
        label.pack()

    root.mainloop()
