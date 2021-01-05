import PySimpleGUI as sg

c1 = 100 # цена за завтрак
price_r1 = [100, 120, 140, 160] # цена комнат
b, r, T, s = 30, 20, 10, 40 # наценка за доп услуги

fn = ("Arial Greek", 12, "bold")
fnl = ("Arial Greek", 14, "bold")      # переменные отвечающие за дизайн меток
v = [1, 2, 3, 4]

room_str = "Выберите номер"
list_room = ["Номер для одного", "Номер для двоих", "Номер для троих", "Номер для четверых"]
list_servic = ["Бар", "Холодильник", "Телевизор", "Душевая"]
main_button = "Рассчитать стоимость"
price = 0
text_s = ""
#||||||||||||||||||||||||||||||||Функции||||||||||||||||||||||||||||||||#

room_entry = sg.Input(key="room_entry", size=(40, 1),  enable_events=True)

def bill():
    temp1=comboVine.get()
    temp2=3
    return temp1*temp2


def input__():# считываем текст с инпут полей
    temp1 = 3
    if room_entry.get() == "":
        temp2 = 1
    else:
        temp2 = int(room_entry.get())
    print(temp1, temp2)
    return temp1*temp2

def check_checkbutton(b, r, T, s): #проверяем checkbutton
    temp=0
    if values[b]:
        temp+=b
    if values[r]:
        temp += r
    if values[T]:
        temp += T
    if values[s]:
        temp += s
    return temp

def check_radiobutton(): #проверяем radiobutton
    temp=0
    if values[c1]:
        temp += c1
    return temp

def calculator(): #проводим вычисления
    temp=0
    if price == 1:
        temp = price_r1[0]
    elif price == 2:
        temp = price_r1[1]
    elif price == 3:
        temp = price_r1[2]
    elif price == 4:
        temp = price_r1[3]
    temp1=check_checkbutton(b, r, T, s)
    temp2=check_radiobutton()
    temp3=bill()
    temp4=input__()
    temp=(temp+temp1+temp2)*temp3+temp4

    # Додаємо на надпису ціну
    sss =  str(temp) + " гривень"
    window.Element("TEXT").Update(value=text_s)
    window.Element("UU").Update(value=sss)
#||||||||||||||||||||||||||||||||Функции||||||||||||||||||||||||||||||||#

but_1 = sg.Button(list_room[0], size=(20, 4), border_width=0, font=fn)
but_2 = sg.Button(list_room[1], size=(20, 4), border_width=0, font=fn)
but_3 = sg.Button(list_room[2], size=(20, 4), border_width=0, font=fn)
but_4 = sg.Button(list_room[3], size=(20, 4), border_width=0, font=fn)
but_5 = sg.Button(main_button, size=(20, 4), border_width=0, font=fn)

Rbut_1 = sg.Radio("С завтраком", "RADIO1", key=c1, font=fn)
Rbut_2 = sg.Radio("Без завтрака", "RADIO1", key=0, font=fn)

Chbut_1 = sg.Checkbox(list_servic[0], key=b, font=fn)
Chbut_2 = sg.Checkbox(list_servic[1], key=r, font=fn)
Chbut_3 = sg.Checkbox(list_servic[2], key=T, font=fn)
Chbut_4 = sg.Checkbox(list_servic[3], key=s, font=fn)

main_text = sg.Text(room_str, key="TEXT", text_color="#000000", font=fnl, size=(25, 2))
night_text = sg.Text("Введите количество номеров", text_color="#000000", font=fn)
room_text = sg.Text("Введите количество ночей", text_color="#000000", font=fn)
resalt_text = sg.Text("Всего: "+str(0),  background_color="#FF0000", text_color="#FFFFFF", font=fnl, key="UU")

main_cost = sg.Text("Стоимость билета", key="eeee", text_color="#000000", font=fn)
main_bill = sg.Text("Количество билетов", key="eeee21", text_color="#000000", font=fn)

comboVine = sg.Combo(v, size=(40, 1), key="comboVine")
ssg = sg.Slider(range=(1, 60),  orientation= "horizontal", size=(32,20))
ssgdd = sg.Slider(range=(1, 80),  orientation= "horizontal", size=(32,20))

left_side = [[but_1], [but_2], [but_3], [but_4], [but_5]]
right_side = [[main_text], [Rbut_1, Rbut_2], [Chbut_1, Chbut_2], [Chbut_3, Chbut_4], 
[night_text], [comboVine], [room_text], [ssg], [main_cost], [room_entry], [main_bill], [ssgdd], [resalt_text]]

layout = [
    [
        sg.Column(left_side, expand_x=True, expand_y=True),
        sg.Column(right_side, expand_x=True, expand_y=True)
    ]
]
window = sg.Window('Индивидуальная №1', layout)

while True:
    event, values = window.read()
    if event == 'comboVine' and values['comboVine'] and values['comboVine'][-1] not in ('0123456789'):
        window['comboVine'].update(values['comboVine'][:-1])
    if event == 'room_entry' and values['room_entry'] and values['room_entry'][-1] not in ('0123456789'):
        window['room_entry'].update(values['room_entry'][:-1])
    if event == list_room[0]:
        price = 1
        text_s = list_room[0]
    if event == list_room[1]:
        price = 2
        text_s = list_room[1]
    if event == list_room[2]:
        price = 3
        text_s = list_room[2]
    if event == list_room[3]:
        price = 4
        text_s = list_room[3]
    if event == main_button:
        calculator()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break

window.close()
