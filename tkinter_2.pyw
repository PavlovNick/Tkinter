from tkinter import *

root = Tk()
root.title("Подсчет стоимости бронирования номеров")
root.resizable(width = False, height = False)

c1 = 100 # цена за завтрак
price_r1, price_r2, price_r3, price_r4 = 100, 120, 140, 160 # цена комнат
b, r, T, s = 30, 20, 10, 40 # наценка за доп услуги

F_left = Frame(root) #рамка для левого сектора
F_right = Frame(root)#рамка для правого сектора
F_right_top = Frame(F_right)# рамки для правой части

w_but = 20                             #
h_but = 3                              #
b_padx = 10                            # переменные отвечающие за дизайн кнопок
b_pady = 8                             #
fn = ("Arial Greek", 12, "bold")       #
col1 = "#FFFFFF"                       #
col2 = "#4682B4"                       #
rel = RAISED                           #

w_lab = 45                             #
h_lab = 1                              #
fnl = ("Arial Greek", 12, "bold")      # переменные отвечающие за дизайн меток
col11 = "#000000"                      #
col12 = "#ffffff"                      #

room_str = "Выберите номер"
list_room = ["Номер для одного", "Номер для двоих", "Номер для троих", "Номер для четверых"]
main_button = "Рассчитать стоимость"
price = 0

#////////////////////////////////////Функции////////////////////////////////////////#

def button1_pressed(event, f, prc): # для отслеживания нажатий на кнопки номеров
    L_r_t1['text'] = f
    global price
    price = prc

def correct1(inp): # для валидации entry полей 
    if inp.isdigit() and int(inp) <= 1000000:
        return True
    elif inp == "":
        return True
    else:
        return False

def correct2(inp): # для валидации entry полей 
    if inp.isdigit()and int(inp) < 5:
        return True
    elif inp == "":
        return True
    else:
        return False

def check_entry(price_entry): # для считывания цифр в entry полях
    temp1 = 0
    if price_entry.get() != "":
        temp1 = int(price_entry.get())
    return temp1

def check_radiobutton(var_rb, c1): # проверка и вычисление radiobutton
    temp = 0
    if var_rb.get() == 0:
        temp = c1
    return temp

def check_checkbutton(Int_bar, Int_refrigerator, Int_TV, Int_shower, bar, refrigerator, TV, shower): # проверка и вычисление checkbutton
    temp = 0
    if Int_bar.get() == 1:
        temp += bar
    if Int_refrigerator.get() == 1:
        temp += refrigerator
    if Int_TV.get() == 1:
        temp += TV
    if Int_shower.get() == 1:
        temp += shower
    return temp

def get_num_seats_scale(): # взять количество мест
    f = num_seats_scale.get()
    return int(f)

def get_night_scale():     # взять количество ночей
    f = night_scale.get()
    return int(f)

def get_spinbox_num():     # взять количество номеров
    f = spinbox_num.get()
    return int(f)

def calculate(event): # финальный подсчет суммы
    global price
    temp1 = check_checkbutton(Int_bar, Int_refrigerator, Int_TV, Int_shower, b, r, T, s)
    temp2 = check_radiobutton(var_rb, c1)
    temp3 = get_night_scale()
    temp4 = get_spinbox_num()
    temp5 = check_entry(price_entry)
    temp6 = get_num_seats_scale()
    PRICE = price + temp1 + temp2
    PRICE = PRICE * temp3 * temp4
    PRICE = PRICE + (temp5*temp6)
    L_r_2b['text'] = str(PRICE) + " грн."
    L_r_b['text'] = "Всего: "
    
#////////////////////////////////////Функции////////////////////////////////////////#

B_f_1 = Button(F_left, text=list_room[0], width=w_but , height=h_but, font=fn, fg=col1, bg=col2, relief=rel)  #
B_f_2 = Button(F_left, text=list_room[1], width=w_but , height=h_but, font=fn, fg=col1, bg=col2, relief=rel)  #
B_f_3 = Button(F_left, text=list_room[2], width=w_but , height=h_but, font=fn, fg=col1, bg=col2, relief=rel)  # кнопки левой части
B_f_4 = Button(F_left, text=list_room[3], width=w_but , height=h_but, font=fn, fg=col1, bg=col2, relief=rel)  #
B_m = Button(F_left, text=main_button, width=w_but , height=h_but, font=fn, fg=col1, bg="#FF0000", relief=rel)#

L_r_t1 = Label(F_right_top, text=room_str, width=w_lab, height=h_lab, font=("Arial Greek", 14, "bold"), fg="#FF0000", bg=col12) #
L_r_t2 = Frame(F_right_top, width=w_lab, bg=col12)                                                          #
L_r_t3 = Frame(F_right_top, width=w_lab, bg=col12)
                                                                                                            # метки для разметки 
L_r_t4 = Frame(F_right_top, width=w_lab, bg=col12)                                                          # правой части проги
L_r_t4r = Frame(L_r_t4, width=w_lab, bg=col12)                                                              
L_r_t4l = Frame(L_r_t4, width=w_lab, bg=col12)

L_r_t4_1 = Frame(F_right_top, width=w_lab, bg=col12)
L_r_t4_1r = Frame(L_r_t4_1, width=w_lab, bg=col12)                                                              
L_r_t4_1l = Frame(L_r_t4_1, width=w_lab, bg=col12)

L_r_t4_2 = Frame(F_right_top, width=w_lab, bg=col12)
L_r_t4_2r = Frame(L_r_t4_2, width=w_lab, bg=col12)                                                              
L_r_t4_2l = Frame(L_r_t4_2, width=w_lab, bg=col12)

L_r_t4_3 = Frame(F_right_top, width=w_lab, bg=col12)
L_r_t4_3r = Frame(L_r_t4_3, width=w_lab, bg=col12)                                                              
L_r_t4_3l = Frame(L_r_t4_3, width=w_lab, bg=col12)

L_r_t5 = Frame(F_right_top, width=w_lab, bg=col12)                                                          

var_rb = IntVar()                                                                                             # Radiobutton 
var_rb.set(0)                                                                                                 #
with_break =  Radiobutton(L_r_t2, text="С завтраком",  variable=var_rb, value=0, font=fnl, fg=col11, bg=col12)# с завтраком
no_break = Radiobutton(L_r_t2, text="Без завтрака",  variable=var_rb, value=1, font=fnl, fg=col11, bg=col12)  # без завтрака

Int_bar = IntVar()                                                                                                                    #
Int_refrigerator = IntVar()                                                                                                           #
Int_TV = IntVar()                                                                                                                     # checkbutton
Int_shower = IntVar()                                                                                                                 # 
bar = Checkbutton(L_r_t3, text="Бар", variable=Int_bar, onvalue=1, offvalue=0, font=fnl, fg=col11, bg=col12)                          # Бар
refrigerator = Checkbutton(L_r_t3, text="Холодильник", variable=Int_refrigerator, onvalue=1, offvalue=0, font=fnl, fg=col11, bg=col12)# Холодильник
TV = Checkbutton(L_r_t3, text="Телевизор", variable=Int_TV, onvalue=1, offvalue=0, font=fnl, fg=col11, bg=col12)                      # Телевизор
shower = Checkbutton(L_r_t3, text="Душевая", variable=Int_shower, onvalue=1, offvalue=0, font=fnl, fg=col11, bg=col12)                # Душевая

num_num = Label(L_r_t4r, text="Введите количество номеров", width=int(w_lab/1.5), font=fnl, fg=col11, bg=col12)
num_night = Label(L_r_t4l, text="Введите количество ночей", width=int(w_lab/1.5), font=fnl, fg=col11, bg=col12)
num_seats = Label(L_r_t4_2r, text="Введите количество мест", width=int(w_lab/1.5), font=fnl, fg=col11, bg=col12)
price = Label(L_r_t4_2l, text="Цена билета", width=int(w_lab/1.5), font=fnl, fg=col11, bg=col12)

price_seats = StringVar()                                                           # текстовые поля для ввода цены билета
price_entry = Entry(L_r_t4_3l, textvariable=price_seats, font=fnl, bd=2, width=30)  #

scale_seats = IntVar()
num_seats_scale = Scale(L_r_t4_3r, from_=0, to=80, variable=scale_seats, orient=HORIZONTAL, width=w_but, length=270, # количество мест
                        font=fn, fg=col1, bg=col2, bd=0, relief=FLAT, highlightbackground=col12, troughcolor=col12)
scale_night = IntVar()
night_scale = Scale(L_r_t4_1l, from_=1, to=50, variable=scale_night, orient=HORIZONTAL, width=w_but, length=270,     # количество ночей
                        font=fn, fg=col1, bg=col2, bd=0, relief=FLAT, highlightbackground=col12, troughcolor=col12)

spinbox_num = Spinbox(L_r_t4_1r, from_=1, to=4, width=int(w_but*1.5)-1,                                              # количество номеров
                        font=fn, fg=col1, bg=col2, bd=0, relief=FLAT, disabledbackground=col12)

L_r_b = Label(L_r_t5, text="Всего: ", height=h_lab, font=fnl, fg=col11, bg=col12)
L_r_2b = Label(L_r_t5, text="", height=h_lab, font=fnl, fg="#FF0000", bg=col12)

B_f_1.bind('<Button-1>', lambda e, f=list_room[0], prc=price_r1: button1_pressed(e, f, prc)) #
B_f_2.bind('<Button-1>', lambda e, f=list_room[1], prc=price_r2: button1_pressed(e, f, prc)) # отслеживаем нажатия на кнопки
B_f_3.bind('<Button-1>', lambda e, f=list_room[2], prc=price_r3: button1_pressed(e, f, prc)) #
B_f_4.bind('<Button-1>', lambda e, f=list_room[3], prc=price_r4: button1_pressed(e, f, prc)) #
B_m.bind('<Button-1>', calculate)

reg = root.register(correct1)                                  # валидация для Entry, Spinbox можно вводить только "int"
rep = root.register(correct2)                                  # есть ограничения на числа
price_entry.config(validate="key", validatecommand=(reg, '%P'))# не более милиона 
spinbox_num.config(validate="key", validatecommand=(rep, '%P'))# не более 4
#////////////////////////////////////////////////////////////////////////////#
#Bookman Old Style
#Arial Greek
#////////////////////////////////////////////////////////////////////////////#

F_right.pack(side=RIGHT ,fill=BOTH)
F_right_top.pack(side=TOP, fill=BOTH)

F_left.pack(side=LEFT ,fill=BOTH)
B_f_1.pack(side=TOP, fill=BOTH)
B_f_2.pack(side=TOP, fill=BOTH)
B_f_3.pack(side=TOP, fill=BOTH)
B_f_4.pack(side=TOP, fill=BOTH)
B_m.pack(side=TOP, fill=BOTH)

L_r_t1.pack(side=TOP, fill=BOTH)
L_r_t2.pack(side=TOP, fill=BOTH)
L_r_t3.pack(side=TOP, fill=BOTH)

L_r_t4.pack(side=TOP, fill=BOTH)
L_r_t4r.pack(side=RIGHT, fill=BOTH)
L_r_t4l.pack(side=LEFT, fill=BOTH)

L_r_t4_1.pack(side=TOP, fill=BOTH)
L_r_t4_1r.pack(side=RIGHT, fill=BOTH)                                                              
L_r_t4_1l.pack(side=LEFT, fill=BOTH)

L_r_t4_2.pack(side=TOP, fill=BOTH)
L_r_t4_2r.pack(side=RIGHT, fill=BOTH)                                                              
L_r_t4_2l.pack(side=LEFT, fill=BOTH)

L_r_t4_3.pack(side=TOP, fill=BOTH)
L_r_t4_3r.pack(side=RIGHT, fill=BOTH)                                                              
L_r_t4_3l.pack(side=LEFT, fill=BOTH)

L_r_t5.pack(side=TOP, fill=BOTH)

L_r_b.pack(side=LEFT ,fill=X)
L_r_2b.pack(side=LEFT ,fill=X)

with_break.pack(side=LEFT, expand=1, fill=X, pady=b_pady)
no_break.pack(side=LEFT, expand=1, fill=X, pady=b_pady)

bar.pack(side=LEFT, expand=1, fill=X, pady=b_pady)
refrigerator.pack(side=LEFT, expand=1, fill=X, pady=b_pady)
TV.pack(side=LEFT, expand=1, fill=X, pady=b_pady)
shower.pack(side=LEFT, expand=1, fill=X, pady=b_pady)

num_num.pack(side=TOP, expand=1, fill=X, pady=b_pady)
num_night.pack(side=TOP, expand=1, fill=X, pady=b_pady)

night_scale.pack(side=TOP, expand=1, fill=X, padx=b_padx, pady=b_pady)
spinbox_num.pack(side=TOP, expand=1, fill=X, padx=b_padx, pady=b_pady)

num_seats.pack(side=TOP, expand=1, fill=X, pady=b_pady)
price.pack(side=TOP, expand=1, fill=X, pady=b_pady)

num_seats_scale.pack(side=TOP, expand=1, fill=X, padx=b_padx, pady=b_pady)

price_entry.pack(side=TOP, expand=1, fill=X, padx=b_padx, pady=b_pady)
root.mainloop()
