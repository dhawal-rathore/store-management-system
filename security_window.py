import PySimpleGUI as sg
import csv
import base64


def getUserData():
    file=open('users.csv','r',newline='')
    user_data=[]
    for i in csv.reader(file):
        user_data.append(i)
    file.close()
    return user_data
    
def addUser():
    user_data=getUserData()
    usernames=[]
    for i in user_data:
        usernames.append(i[0])
    layout=[[[sg.Text('New Username')],
            [sg.Input(key='user')],
            [sg.Text('New Password')],
            [sg.Input(key='pwd',password_char='*')],
            [sg.Text('Reenter Password')],
            [sg.Input(key='pwd_conf',password_char='*')],
            [[sg.Button('Create New User',key='newuser',bind_return_key=True),
              sg.Button('Exit',key='Exit')]]]]
    window=sg.Window("Add User",layout=layout)
    while True:
        event,values=window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event=='newuser':
            if values['user'] not in usernames:
                if values['pwd']==values['pwd_conf']:
                    newpass=base64.b64encode(values['pwd'].encode('utf-8')).decode('utf-8')
                    user_data.append([values['user'],newpass,3])
                    file=open('users.csv','w',newline='')
                    writer=csv.writer(file)
                    writer.writerows(user_data)
                    file.close()
                else:
                    sg.popup("Passwords do not match")
                    window['pwd'].update('')
                    window['pwd_conf'].update('')
            else:
                sg.popup("Username already exists.")
                window['user'].update('')
                window['pwd'].update('')
                window['pwd_conf'].update('')
def unblockUser():
    user_data=getUserData()
    blocked_users=[]
    for i in user_data:
        if int(i[2])==0:
            blocked_users.append(i[0])
    layout=[[[sg.Text('Blocked Users')],
            [sg.Listbox(values=blocked_users,s=(40,7),key='selected_users')]],
            [[sg.Button('Unblock Selected User',key='unblock')]]]
    window=sg.Window("Unblock Users",layout=layout,size=(400,200))
    while True:
        event,values=window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event=='unblock':
            for j in user_data:
                if values['selected_users']!=[]:
                    if values['selected_users'][0]==j[0]:
                        j[2]=3
            file=open('users.csv','w',newline='')
            writer=csv.writer(file)
            writer.writerows(user_data)
            file.close()
            blocked_users.remove(values['selected_users'][0])
            window['selected_users'].update(blocked_users)
            sg.popup(f"{values['selected_users'][0]} has been unblocked")
