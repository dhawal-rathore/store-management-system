import PySimpleGUI as sg
from auth import authWindow
from billing_window import billingWindow
from query_stock_window import stock_table
from edit_stock_window import stock_edit
from add_stock_window import stock_add
from security_window import unblockUser,addUser 

if authWindow():
    sg.theme("Dark Blue 3")
    layout=[[sg.Text('Store Management System', font='Any 20')],
            [sg.Frame("Billing",[
                [sg.Button("Billing Window",key='bill')]]
            )],
            [sg.Frame("Stock",[
                [sg.Button("View Stock",key='view')],
                [sg.Button("Edit Stock",key='edit')],
                [sg.Button("Add Stock",key='add')]
            ])],
            [sg.Frame("Security",[
                [sg.Button('Add New User',key='adduser')],
                [sg.Button('Unblock Users',key='unblock')]
            ])]]
    window=sg.Window('Store Management System',layout=layout)
    while True:
            event,values=window.read()
            if event == sg.WIN_CLOSED or event == 'Exit':
                break
            if event=='bill':
                billingWindow()
            if event=='view':
                stock_table()
            if event=='edit':
                stock_edit()
            if event=='add':
                stock_add()
            if event=='adduser':
                if authWindow():
                    addUser()
            if event=='unblock':
                if authWindow():
                    unblockUser()