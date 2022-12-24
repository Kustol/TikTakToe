from logger import *

def play():
    menu = Tk()
    menu.geometry('300x300')
    menu.title('Крестики-Нолики')
    wpc = partial(withpc, menu)

    head = Button(menu, text='Крестики - Нолики',
                  activeforeground='violet',
                  activebackground='yellow', bg='maroon1',
                  fg='yellow', width=500, font='Symbol', bd=10)

    B1 = Button(menu, text='Одиночная игра', command=wpc,
                activeforeground='blue',
                activebackground='yellow', bg='sky blue',
                fg='yellow', width=500, font='Symbol', bd=10)

    B2 = Button(menu, text='Выход', command=menu.quit, activeforeground='violet',
                activebackground='yellow', bg='steel blue', fg='yellow',
                width=500, font='Symbol', bd=10)
    head.pack(side='top')
    B1.pack(side='top')
    B2.pack(side='top')
    menu.mainloop()
