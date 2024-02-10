from tkinter import *
import requests

def get_spins():
    latest = [[i['color'], i['roll']] for i in requests.get('https://blaze.com/api/roulette_games/recent').json()][:5][::-1]
    return latest

def number_color(spins):
    spin_list = []
    for spin in spins:
        if spin[0] == 1:
            spin_list.append(['#F12C4C', 'white', spin[1]])
        elif spin[0] == 2:
            spin_list.append(['#262F3C', 'white', spin[1]])
        else:
            spin_list.append(['white','white', spin[1]])
    return spin_list

def update():
    data_blaze = get_spins()
    details = number_color(data_blaze)

    n1['text'] = details[0][2]
    n2['text'] = details[1][2]
    n3['text'] = details[2][2]
    n4['text'] = details[3][2]
    n5['text'] = details[4][2]

    n1['bg'] = details[0][0]
    n2['bg'] = details[1][0]
    n3['bg'] = details[2][0]
    n4['bg'] = details[3][0]
    n5['bg'] = details[4][0]

    if sum([num[1] for num in data_blaze])%2 == 0:
        predicted_color = '#262F3C'
    else:
        predicted_color = '#F12C4C'
    forecast = Label(text='Predicted Color', fg='white', height=2, width=20, bg=predicted_color, font=('', 12))
    forecast.grid(row=2, column=3, columnspan=2)

screen = Tk()
screen.resizable(False, False)
# screen.iconbitmap('img/logo_willtubetech.ico')
screen.title('WillTube Tech - Bot for Blaze Double')

message = Label(text='Blaze Double Spins', bg='#0F1923', fg='white', height=2, width=40, font=('', 15,'bold'))
message.grid(row=0, column=0, columnspan=5)
n1 = Label(text='', bg='gray', fg='white', height=3, width=8, font=('', 12))
n2 = Label(text='', bg='gray', fg='white', height=3, width=8, font=('', 12))
n3 = Label(text='', bg='gray', fg='white', height=3, width=8, font=('', 12))
n4 = Label(text='', bg='gray', fg='white', height=3, width=8, font=('', 12))
n5 = Label(text='', bg='gray', fg='white', height=3, width=8, font=('', 12))

n1.grid(row=1, column=0)
n2.grid(row=1, column=1)
n3.grid(row=1, column=2)
n4.grid(row=1, column=3)
n5.grid(row=1, column=4)

btn = Button(text='Update spins', height=2, width=30, font=('',12), command=update)
btn.grid(row=2, column=0, columnspan=3)

screen.mainloop()
