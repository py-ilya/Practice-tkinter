from tkinter import*
from tkinter import messagebox

#Создается основное окно с параметрами
top = Tk()
top.title('Window for tests Tk-interface')

#Функции, которые вызываются кнопками
def helloCallBack():
    msg=messagebox.showinfo( "Hello", "Hello Python")

def closeWindow():
    return quit()

def askOpen():
    msg=askopenfilename.showinfo("Save file", "Save")

def showKeys():
    B['text'] = 'h'
    B2['text'] = 'q'
    btn_openFile['text'] = 'c'
    btn_show['text'] = 's'

def btnPic_click():
    frm_01.destroy()
    bgcolor = "#34495E"
    btncolor = "#95A5A6"

    # Фреймы, разделы
    frm_02 = Frame(top, bg = bgcolor)
    frm_1 = LabelFrame(frm_02, text = "Hello", width = 100, height = 100, bg = bgcolor)
    frm_2 = LabelFrame(frm_02, text = 'Other', bg = bgcolor)
    frm_3 = LabelFrame(frm_02, text = "Radio buttons", bg = bgcolor)
    frm_bottom = Frame(frm_02, height = 50, bg = bgcolor)

    frm_02.pack(fill = 'both')
    frm_1.pack(fill = 'both', padx = 2)
    frm_2.pack(fill = 'both', padx = 2)
    frm_3.pack(fill = 'both', padx = 2) #как сделать что б была привязка и к нижней части?"""
    frm_bottom.pack(side = BOTTOM, fill = 'both')
    
    #Чекбаттон (кнопка с отметкой)
    videoVar = IntVar()
    musicVar = IntVar()
    chbtn_video = Checkbutton(frm_1, text = "Video", variable = videoVar,
                              onvalue = 1, offvalue = 0, bg = bgcolor)
    chbtn_music = Checkbutton(frm_1, text = "Music", variable = musicVar,
                              onvalue = 1, offvalue = 0, bg = bgcolor)
    
    chbtn_video.pack(anchor = 'nw')
    chbtn_music.pack(anchor = 'nw')
    
    # Надписи
    lbl_url = Label(frm_1, text = "URL")
    
    lbl_url.pack(anchor = 'nw')
    
    #lbl_url.bind("<B1-Motion>", event)
    
    #Создаем кнопочки и присваиваем им разные параметры
    btn_show = Button(frm_2, text = 'Show hot keys', command = showKeys)
    B = Button(frm_1, text ="Hello", command = helloCallBack,
               activebackground = "white")
    btn_cancel = Button(frm_bottom, text = "Cancel", command = closeWindow)
    btn_ok = Button(frm_bottom, text = "OK", command = closeWindow)
    btn_openFile = Button(frm_2, text = 'Choose file', command = askOpen)
    B['relief'] = GROOVE
    
    B.pack(anchor = 'se')
    btn_show.pack(side=TOP)
    btn_cancel.pack(side=RIGHT, padx = 5, pady = 5)
    btn_ok.pack(side=RIGHT, padx = 0, pady = 5)
    btn_openFile.pack(side=LEFT)
    
    #Поле для ввода информации
    lbl_userName = Label(frm_2, text="User Name")
    ent_userName = Entry(frm_2)
    
    lbl_userName.pack(side = LEFT)
    ent_userName.pack(side = LEFT)
    
    # Радиокнопки
    rbt_var = IntVar()
    rbtn_1 = Radiobutton(frm_3, text = 'Option 1', variable = rbt_var, value = 1,
                         command = rbtn)
    rbtn_2 = Radiobutton(frm_3, text = 'Option 2', variable = rbt_var, value = 2)
    rbtn_3 = Radiobutton(frm_3, text = 'Option 3', variable = rbt_var, value = 3)
    
    rbtn_1.pack(anchor = 'w')
    rbtn_2.pack(anchor = 'w')
    rbtn_3.pack(anchor = 'w')
    
    
# Пока не работает, надо узнать причину.
def rbtn():
    while rbtn_1['variable'] is 0:
        chbtn_video['state']=DISABLED
        
bgcolor = "#34495E"
btncolor = "#95A5A6"

# Фреймы, разделы
frm_01 = Frame(top, bg = bgcolor)
frm_lmenu = Frame(top, width = 30, bg = bgcolor)
frm_1 = LabelFrame(frm_01, text = "Hello", width = 100, height = 100, bg = bgcolor)
frm_2 = LabelFrame(frm_01, text = 'Other', bg = bgcolor)
frm_3 = LabelFrame(frm_01, text = "Radio buttons", bg = bgcolor)
frm_bottom = Frame(frm_01, height = 50, bg = bgcolor)

frm_lmenu.pack(side = LEFT, fill = 'both')
frm_01.pack(fill = 'both')
frm_1.pack(fill = 'both', padx = 2)
frm_2.pack(fill = 'both', padx = 2)
frm_3.pack(fill = 'both', padx = 2) #как сделать что б была привязка и к нижней части?"""
frm_bottom.pack(side = BOTTOM, fill = 'both')

#Чекбаттон (кнопка с отметкой)
videoVar = IntVar()
musicVar = IntVar()
chbtn_video = Checkbutton(frm_1, text = "Video", variable = videoVar,
                          onvalue = 1, offvalue = 0, bg = bgcolor)
chbtn_music = Checkbutton(frm_1, text = "Music", variable = musicVar,
                          onvalue = 1, offvalue = 0, bg = bgcolor)

chbtn_video.pack(anchor = 'nw')
chbtn_music.pack(anchor = 'nw')

# Надписи
lbl_url = Label(frm_1, text = "URL")

lbl_url.pack(anchor = 'nw')

#lbl_url.bind("<B1-Motion>", event)

#Создаем кнопочки и присваиваем им разные параметры
btn_home = Button(frm_lmenu, text = "Home", bg = btncolor, fg = "white",
                  relief = FLAT)
btn_pic = Button(frm_lmenu, text = "Picture", bg = btncolor, fg = "white",
                  relief = FLAT, command = btnPic_click)
btn_show = Button(frm_2, text = 'Show hot keys', command = showKeys)
B = Button(frm_1, text ="Hello", command = helloCallBack,
           activebackground = "white")
btn_cancel = Button(frm_bottom, text = "Cancel", command = closeWindow)
btn_ok = Button(frm_bottom, text = "OK", command = closeWindow)
btn_openFile = Button(frm_2, text = 'Choose file', command = askOpen)
B['relief'] = GROOVE

btn_home.pack(padx = 5, pady = 5)
btn_pic.pack(padx = 5, pady = 0)
B.pack(anchor = 'se')
btn_show.pack(side=TOP)
btn_cancel.pack(side=RIGHT, padx = 5, pady = 5)
btn_ok.pack(side=RIGHT, padx = 0, pady = 5)
btn_openFile.pack(side=LEFT)

#Поле для ввода информации
lbl_userName = Label(frm_2, text="User Name")
ent_userName = Entry(frm_2)

lbl_userName.pack(side = LEFT)
ent_userName.pack(side = LEFT)

# Радиокнопки
rbt_var = IntVar()
rbtn_1 = Radiobutton(frm_3, text = 'Option 1', variable = rbt_var, value = 1,
                     command = rbtn)
rbtn_2 = Radiobutton(frm_3, text = 'Option 2', variable = rbt_var, value = 2)
rbtn_3 = Radiobutton(frm_3, text = 'Option 3', variable = rbt_var, value = 3)

rbtn_1.pack(anchor = 'w')
rbtn_2.pack(anchor = 'w')
rbtn_3.pack(anchor = 'w')


top.mainloop()
