import PySimpleGUI as sg
import autofill
import data
from printBill import printBill

def billingWindow():
    productList=data.dataRead()
    productList_name=[]
    cust_products=[]
    for i in range(1,len(productList)):
        productList_name.append(productList[i][0])
    
    sg.theme("Dark Blue 3")

    layout=[[sg.Frame('Product',[
            [sg.Input(key='entered',enable_events=True)],
            [sg.Input(key='option1',readonly=True),sg.Button("Autofill",key='Auto1')],
            [sg.Input(key='option2',readonly=True),sg.Button("Autofill",key='Auto2')],
            [sg.Input(key='option3',readonly=True),sg.Button("Autofill",key='Auto3')]]),
            sg.Frame('Quantity',[[sg.Input(key='prod_num',s=(4))]],vertical_alignment='top'),
            sg.Frame('Cost',[
                [sg.Input(key='prod_mrp',readonly=True,s=(6))]],vertical_alignment='top'),
            sg.Frame('',[
                [sg.Button('Add Item',key='add',s=(7,3))],
                [sg.Button('Print Bill',key='print',s=(7,3))]],vertical_alignment='top')],
            [sg.Multiline(default_text='Product\t\t\tQuantity',disabled=True,
                          key='display_items',
                          s=(50,30),no_scrollbar=True)]]
    window=sg.Window("Billing Window",layout)
    while True:
        event,values=window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event=='entered':
            l=autofill.search(str(values["entered"]),productList_name)
            try:
                window['option1'].update(l[0])
            except IndexError:
                window['option1'].update('')
            try:
                window['option2'].update(l[1])
            except IndexError:
                window['option2'].update('')
            try:
                window['option3'].update(l[2])
            except IndexError:
                window['option3'].update('')
        if event=='Auto1':
            window['entered'].update(values['option1'])
            i=productList_name.index(values['option1'])+1
            window['prod_mrp'].update(f"{productList[i][4]} Rs")
            continue
        if event=='Auto2':
            window['entered'].update(values['option2'])
            i=productList_name.index(values['option2'])+1
            window['prod_mrp'].update(f"{productList[i][4]} Rs")
            continue
        if event=='Auto3':
            window['entered'].update(values['option3'])
            i=productList_name.index(values['option3'])+1
            window['prod_mrp'].update(f"{productList[i][4]} Rs")
            continue
        if event=='add':
            if values['entered'] in productList_name:
                try:
                    i=productList_name.index(values['entered'])+1
                    prod_mrp=productList[i][4]
                    prod_num=int(values['prod_num'])
                    cust_products.append([values['entered'],prod_num,prod_mrp])
                    l=values['display_items']
                    window['display_items'].update(l+f"\n{values['entered']}\t\t\t{prod_num}")
                    window['entered'].update('')
                    window['prod_num'].update('')
                    

                except ValueError:
                    sg.popup("Invalid Quantity")
                    window['prod_num'].update('')
        if event=='print':
            printBill(cust_products)
            for i in cust_products:
                prod_index=productList_name.index(i[0])+1
                productList[prod_index][2]=int(productList[prod_index][2])-int(i[1])
            data.dataWrite(productList)
            window['entered'].update('')
            window['prod_num'].update('')
            window['prod_mrp'].update('')
            cust_products=[]
        if values['entered'] in productList_name:
            i=productList_name.index(values['entered'])+1
            window['prod_mrp'].update(f"{productList[i][4]} Rs")
