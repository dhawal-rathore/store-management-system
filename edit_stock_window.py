import PySimpleGUI as sg
import autofill
import data

def stock_edit():
    productList=data.dataRead()
    productList_name=[]

    for i in range(1,len(productList)):
        productList_name.append(productList[i][0])
    
    sg.theme("Dark Blue 3")
    
    layout=[[[sg.Frame('',[
            [sg.Text("Enter Product Name")],
            [sg.Input(key='entered',enable_events=True),sg.Button("Get Data",key='getdata')],
            [sg.Input(key='option1',readonly=True),sg.Button("Autofill",key='Auto1')],
            [sg.Input(key='option2',readonly=True),sg.Button("Autofill",key='Auto2')],
            [sg.Input(key='option3',readonly=True),sg.Button("Autofill",key='Auto3')]])],
            [sg.Frame("Data",[
                [sg.Text("Product ID")],
                [sg.Input(key='product_id')],
                [sg.Text("Stock")],
                [sg.Input(key='product_stock')],
                [sg.Text("Cost")],
                [sg.Input(key='product_cost')],
                [sg.Text("MRP")],
                [sg.Input(key='product_mrp')]])],
            [sg.Frame("Save",[[sg.Button("Save",key='save'),sg.Button("Undo",key="undo")]],
            element_justification='left')]
           ]]

    window=sg.Window("Edit Stock",layout)

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
        if event=='getdata' or "undo":
            if values['entered'] in productList_name:
                for i in range(1,len(productList)):
                    if values['entered']==productList[i][0]:
                        productIndex=i
                        window['product_id'].update(productList[i][1])
                        window['product_stock'].update(productList[i][2])
                        window['product_cost'].update(productList[i][3])
                        window['product_mrp'].update(productList[i][4])
                        break    
        if event=='Auto1':
            window['entered'].update(values['option1'])
        if event=='Auto2':
            window['entered'].update(values['option2'])
        if event=='Auto3':
            window['entered'].update(values['option3'])
        if event=='save':
            for i in range(1,len(productList)):
                    if values['entered']==productList[i][0]:
                        productIndex=i
                        try:    
                            productList[productIndex][1]=int(values['product_id'])
                        except ValueError:
                            window['product_id'].update(productList[i][1])
                            sg.popup('Product ID should be a number')
                        try:    
                            productList[productIndex][2]=int(values['product_stock'])
                        except ValueError:
                            window['product_stock'].update(productList[i][2])
                            sg.popup('Product Stock should be a number')
                        try:    
                            productList[productIndex][3]=int(values['product_cost'])
                        except ValueError:
                            window['product_cost'].update(productList[i][3])
                            sg.popup('Product Cost should be a number')
                        try:    
                            productList[productIndex][4]=int(values['product_mrp'])
                        except ValueError:
                            window['product_mrp'].update(productList[i][4])
                            sg.popup('Product MRP should be a number')                      
                        break
            data.dataWrite(productList)
