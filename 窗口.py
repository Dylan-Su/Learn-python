import tkinter as tk

window = tk.Tk()

window.title('The windows')
window.geometry('300x400')
#var = tk.StringVar()
#lab = tk.Label(window,textvariable=var,bg='red',font=('Arial',12),width=15,height=2)
#lab.pack()
#on_hit=False
#def hit_me():
 #   global on_hit
  #  if on_hit==False:
   #     on_hit=True
    #    var.set('你点我了')
   # else:
    #    on_hit=False
     #   var.set('')



e=tk.Entry(window,show=None)#当show的属性设置为*号，则所有输入内容为看不见的像密码一样的形式
e.pack()

def insert_point():
    var=e.get()
    t.insert('insert',var)

def insert_end():
    var=e.get()
    t.insert('end',var)
    
b1=tk.Button(window,text='insert point',width=15,
             heigh=2,command=insert_point)
b1.pack()
b2=tk.Button(window,text='insert end',command=insert_end)
b2.pack()
t=tk.Text(window)
t.pack()
window.mainloop()##创建的window会不断地刷新，所以的窗口文件都要有这个



