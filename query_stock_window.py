import PySimpleGUI as sg
import data

def stock_table():
    productList=data.dataRead()
    headings=productList[0]

    layout = [[sg.Table(values=productList[1:][:], headings=headings,
                    def_col_width=10,
                    auto_size_columns=False,
                    display_row_numbers=False,
                    justification='left',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=35,
                    tooltip='This is a table')],
         ]
    window=sg.Window("Query stock",layout)
    while True:
        event,values=window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
  
