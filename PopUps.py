import tkinter as tk
import random
import time

def create_window():
    win = tk.Tk()
    win.title("重要消息")
    win.geometry("400x200")
    win.configure(bg="white")
    
    # 设置窗口初始随机位置
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = random.randint(0, screen_width - 400)
    y = random.randint(0, screen_height - 200)
    win.geometry(f"+{x}+{y}")
    
    # 创建文字标签
    label = tk.Label(win, 
                    text="你的电脑被UP主破坏了!!!\n你就别想着玩电脑了!!!", 
                    font=("Microsoft YaHei", 24, "bold"),
                    fg="black",
                    bg="white",
                    justify="center",
                    padx=20,
                    pady=40)
    label.pack(expand=True, fill=tk.BOTH)
    
    return win

def move_window(window):
    # 获取屏幕尺寸
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    
    # 生成随机位置
    new_x = random.randint(0, screen_width - 400)
    new_y = random.randint(0, screen_height - 200)
    
    # 移动窗口
    window.geometry(f"+{new_x}+{new_y}")
    
    # 设置下一次移动(200毫秒后)
    window.after(200, move_window, window)

# 创建20个窗口
windows = []
for _ in range(20):
    w = create_window()
    windows.append(w)
    # 设置窗口移动(200毫秒后开始移动)
    w.after(200, move_window, w)

# 启动主循环
tk.mainloop()
