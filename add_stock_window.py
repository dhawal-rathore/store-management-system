import PySimpleGUI as sg
import data

def stock_add():
    sg.theme("Dark Blue 3")
    productList=data.dataRead()
    layout=[[sg.Frame("Data",[
                [sg.Text("Product Name")],
                [sg.Input(key='product_name')],
                [sg.Text("Product ID")],
                [sg.Input(key='product_id')],
                [sg.Text("Stock")],
                [sg.Input(key='product_stock')],
                [sg.Text("Cost")],
                [sg.Input(key='product_cost')],
                [sg.Text("MRP")],
                [sg.Input(key='product_mrp')]])],
            [sg.Frame("Save",[[sg.Button("Save",key='save')]],
                      element_justification='left')]
           ]
    window=sg.Window("Add Stock",layout)
    while True:
        event,values=window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event=='save':
            newProduct=[values['product_name'],
                        int(values['product_id']),
                        int(values['product_stock']),
                        int(values['product_cost']),
                        int(values['product_mrp'])]
            
            productList.append(newProduct)
            data.dataWrite(productList)
