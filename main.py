#!C:\Users\arana\AppData\Local\Continuum\anaconda3\python.exe

import util_function as uf
import os
from datetime import datetime


dirname = os.path.dirname(__file__)


key_file = os.path.join(dirname, 'sheet_key.json')
sheet_name = 'ARTICULOS DE LECTURA'
page_name = 'Hoja 1'


today = datetime.now()
today = today.strftime("%b %d, %Y").replace(" 0", " ")


client = uf.connect_to_sheet(key_file)
sheet = uf.open_sheet(client, sheet_name)
sheet_instance = uf.open_worksheet(sheet, page_name)


today_row = sheet_instance.find(today, in_column=1)._row
sheet_instance.update_cell(today_row, 5, "XX")