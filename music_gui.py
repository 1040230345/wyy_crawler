import tkinter as tk
from tkinter import ttk
from music import wyy_music as wyy
import pygame
import os
from music import open_music as op

# 搜索音乐
def file_music():
    # 清除
    delButton(treeview)
    print(inputText.get())
    if inputText.get() != "":
        global data
        data = wyy.find_music(inputText.get())
        # 计数器归零
        i = 0
        for music in data:
            # print(i)
            treeview.insert('', i, values=(i, music['b'], music['c'], music['time']))
            i += 1


# 清空表单
def delButton(treeview):
    x = treeview.get_children()
    for item in x:
        treeview.delete(item)


# 绑定事件
def treeviewClick(event):
    # print('单击')
    for item in treeview.selection():
        item_text = treeview.item(item, "values")
        print(item_text[0])  # 输出所选行的第一列的值
        # 获取歌曲id
        music_id = data[int(item_text[0])]['a'][9:]
        # print(byte_obj)
        # 对id进行判断，是否已经下载
        find_mp3 = os.path.exists(r"my_music/"+music_id+'.mp3')
        if find_mp3:
            print('文件已经存在不用下载')
        else:
            print('正在下载...')
            op.login_music(music_id)
        pygame.mixer.music.load(r"my_music/"+music_id+".mp3")
        # 播放音乐
        pygame.mixer.music.play()


# 初始化播放器
pygame.mixer.init()
# 启动浏览器
wyy.open_chrome()
# 查找后的歌曲存放
data = {}
# 初始化Tk()
root = tk.Tk()
root.title("音乐播放器V1.0")  # 设置窗口标题
root.geometry("1100x600")  # 设置窗口大小 注意：是x 不是*
root.resizable(width=False, height=False)  # 设置窗口是否可以变化长/宽，False不可变，True可变，默认为True
# 设置输入框
inputText = tk.Entry(root, show=None, foreground='black', font=('Helvetica', '15', 'bold'), insertbackground='green',
                     width=20)
inputText.place(x=400, y=10,)
# 设置按钮，以及放置的位置
searchBtn = tk.Button(root, text="搜索", fg="blue", bd=2, width=10, command=file_music)  # command中的方法带括号是直接执行，不带括号才是点击执行
searchBtn.place(x=650, y=8, anchor='nw')

update_progress = tk.StringVar()

# 创建滚动条
scroll = tk.Scrollbar()

columns = ("编号", "歌曲", "演唱者", "时长")
treeview = ttk.Treeview(root, height=18, show="headings", columns=columns)  # 表格

treeview.column("编号", width=100, anchor='center')  # 表示列,不显示
treeview.column("歌曲", width=300, anchor='center')
treeview.column("演唱者", width=300, anchor='center')
treeview.column("时长", width=300, anchor='center')

treeview.heading("编号", text="编号")  # 显示表头
treeview.heading("歌曲", text="歌曲")
treeview.heading("演唱者", text="演唱者")
treeview.heading("时长", text="时长")

# side放到窗体的哪一侧,  fill填充
scroll.pack(side=tk.RIGHT, fill=tk.Y)
treeview.pack(side=tk.LEFT, fill=tk.Y)
# 关联
scroll.config(command=treeview.yview)
treeview.config(yscrollcommand=scroll.set)

treeview.pack()
treeview.place(x=45, y=120,)
# 双击触发
treeview.bind('<Double-Button-1>', treeviewClick)
# 进入消息循环
root.mainloop()
