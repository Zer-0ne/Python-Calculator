from tkinter import *
import math
root = Tk()
root.title('Sahil khan - Calculator')
root.configure(bg='black')
# root.resizable(False,False)
expression = ''
def click_btn(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)
def clear():
    global expression
    expression = ''
    input_text.set(expression)
def result():
    global expression
    result = str(eval(expression))
    input_text.set(f' = {result}')
    # expression = ''
# def cal():
#     if click_btn('+'):


input_text = StringVar()
entry_flied =Frame(root, bg = "black")
entry_flied.pack(fill='x')
entry = Entry(entry_flied,textvariable=input_text,bg='black',highlightcolor='red',fg='red', font='arial 50 bold',highlightbackground='black',insertbackground='red')
btns_frame = Frame(root, width = 312, height = 272.5, bg = "black")
btns_frame.pack()
b1 = Button(btns_frame,text='C',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: clear())
b2 = Button(btns_frame,text='()',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('()'))
b3 = Button(btns_frame,text='%',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('%'))
b4 = Button(btns_frame,text='/',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('/'))

b5 = Button(btns_frame,text='7',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('7'))
b6 = Button(btns_frame,text='8',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('8'))
b7 = Button(btns_frame,text='9',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('9'))
b8 = Button(btns_frame,text='x',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('*'))

b9 = Button(btns_frame,text='4',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('4'))
b10 = Button(btns_frame,text='5',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('5'))
b11 = Button(btns_frame,text='6',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('6'))
b12 = Button(btns_frame,text='-',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('-'))

b13 = Button(btns_frame,text='1',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('1'))
b14 = Button(btns_frame,text='2',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('2'))
b15 = Button(btns_frame,text='3',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('3'))
b16 = Button(btns_frame,text='+',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('+'))

b17 = Button(btns_frame,text='+/-',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('-'))
b18 = Button(btns_frame,text='0',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('0'))
b19 = Button(btns_frame,text='.',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: click_btn('.'))
b20 = Button(btns_frame,text='=',font='helvetica 18 bold ',height=4,width=14,bg='black',fg='red',command=lambda: result())

entry.grid(row=0,column=0)
entry.pack(ipady=50,fill='x')

b1.grid(row=0,column=0)
b2.grid(row=0,column=1)
b3.grid(row=0,column=2)
b4.grid(row=0,column=3)

b5.grid(row=1,column=0)
b6.grid(row=1,column=1)
b7.grid(row=1,column=2)
b8.grid(row=1,column=3)

b9.grid(row=2,column=0)
b10.grid(row=2,column=1)
b11.grid(row=2,column=2)
b12.grid(row=2,column=3)


b13.grid(row=3,column=0)
b14.grid(row=3,column=1)
b15.grid(row=3,column=2)
b16.grid(row=3,column=3)

b17.grid(row=4,column=0)
b18.grid(row=4,column=1)
b19.grid(row=4,column=2)
b20.grid(row=4,column=3)

root.bind('7',click_btn)
root.mainloop()