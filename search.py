
from a101 import a101_get_data
from carrefoursa import carrefoursa_get_data
from migros import migros_get_data
from sokmarket import sokmarket_get_data
import pandas as pd
from tabulate import tabulate
from datetime import datetime
# pandas export to Excel using openpyxl
# pip install openpyxl
import os
import sys
import arguments as param


search = ""
# ekmek, makarna
if param.search_words == "":
    print("Arama için ürün/ürünler yok.")
    print("No products for search.")
    print("python search.py -s <search_words>")
    print("python search.py -s pepsi ") 
    print("python search.py -s 'coca cola' ") 
    sys.exit(2)
else:
    # search = "makarna" 
    search = param.search_words

    
a101_data_frame = pd.DataFrame()
a101_data_frame = a101_get_data(search)
# print(tabulate(a101_data_frame, headers=["No", "Market", "Product", "Price"], tablefmt="simple", numalign="right"))

carrefoursa_data_frame = pd.DataFrame()
carrefoursa_data_frame = carrefoursa_get_data(search)
# print(tabulate(carrefoursa_data_frame, headers=["No", "Market", "Product", "Price"], tablefmt="simple", numalign="right"))

migros_data_frame = pd.DataFrame()
migros_data_frame = migros_get_data(search)
# print(tabulate(migros_data_frame, headers=["No", "Market", "Product", "Price"], tablefmt="simple", numalign="right"))

sokmarket_data_frame = pd.DataFrame()
sokmarket_data_frame = sokmarket_get_data(search)
# print(tabulate(sokmarket_data_frame, headers=["No", "Market", "Product", "Price"], tablefmt="simple", numalign="right"))

# all_frame = pd.concat([a101_data_frame,carrefoursa_data_frame ], axis=0)
all_frame = pd.concat([a101_data_frame, carrefoursa_data_frame, migros_data_frame, sokmarket_data_frame], axis=0)

print(tabulate(all_frame, headers=["No", "Market", "Product", "Price"], tablefmt="simple", numalign="right"))

today = datetime.today().date().__str__()
now = datetime.now()
time = now.hour.__str__() + now.minute.__str__() +  now.second.__str__() 
# creating excel writer object
excel_file = 'turkish-markets-'+ today + "_" + time + '.xlsx'
excel_writer = pd.ExcelWriter(excel_file)
# write dataframe to excel
all_frame.to_excel(excel_writer, sheet_name= today)

# save the excel
excel_writer.save()
print("")
print("Data is exported to " + excel_file + " Excel file.")
print("")

# for open excel app with file
os.system("start EXCEL.EXE " + excel_file)

