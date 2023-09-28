import PySimpleGUI as sg
import csv
import base64

def authWindow():
    file=open('users.csv','r',newline='')
    user_data=[]
    for i in csv.reader(file):
        user_data.append(i)
    file.close()
    usernames=[]
    for i in user_data:
        usernames.append(i[0])
    layout=[[sg.Text('Username')],
            [sg.Input(key='user')],
            [sg.Text('Password')],
            [sg.Input(key='pwd',password_char='*')],
            [[sg.Button('Login',key='login',bind_return_key=True),sg.Button('Exit',key='Exit')]]]
    window=sg.Window('Login',layout=layout)
    while True:
        event,values=window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event=='login':
            if values['user'] in usernames:
                i=usernames.index(values['user'])
                if int(user_data[i][2])>0:
                    password=base64.b64decode(user_data[i][1]).decode('utf-8')
                    if password==values['pwd']:
                        user_data[i][2]=3
                        file=open('users.csv','w',newline='')
                        writer=csv.writer(file)
                        writer.writerows(user_data)
                        file.close()
                        window.close()
                        return True
                    else:
                        user_data[i][2]=int(user_data[i][2])-1
                        sg.popup(f"Wrong Password\nYou have {user_data[i][2]} attempts left")
                        window['pwd'].update('')
                        file=open('users.csv','w',newline='')
                        writer=csv.writer(file)
                        writer.writerows(user_data)
                        file.close()
                else:
                    sg.popup("This account was locked due to too many failed attempts.")
                
            else:
                sg.popup("Invalid Username")
                window['user'].update('')
                window['pwd'].update('')
    