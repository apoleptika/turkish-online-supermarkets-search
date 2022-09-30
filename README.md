## Bu Python scripti Türkiye'nin dört büyük süper marketi üzerinde ürün araması yapıp sonuçları Excel dosyasına kayıt ediyor. 
## This Python script is searching any product on four big supermarkets in Turkey and saving results in Excel file.
## Supermarkets: A101, CarrefourSA, Migros, Şok Market

Before start to using this Python app, you have to install Python and pip packages. <br/>
 **download and install Python 3.10 from https://www.python.org/downloads/** <br/>
 **c:\> pip install tabulate** <br/>
 **c:\> pip install pandas** <br/>
 **c:\> pip install beautifulsoup4** <br/>
 **c:\> pip install selenium** <br/>
 **c:\> pip install openpyxl**<br/><br/>

This command search nothing because you forget to use search parameter  <br/>
 **c:\> python search.py** <br/><br/>
This command search bread (ekmek) on four supermarkets <br/>
 **c:\> python search.py -s ekmek** <br/><br/> 
This command search 'coca cola' on four supermarkets <br/>
 **c:\> python search.py -s 'coca cola'** <br/>

<picture>
    <img alt="Search product on online four Turkish supermarkets" src="https://github.com/apoleptika/turkish-online-supermarkets-search/blob/main/supermarkets-search.png">
</picture>
<br/>

When search finished Python script opens Excel file that include products <br/>

<picture>
    <img alt="Search product on online four Turkish supermarkets and save in Excel file" src="https://github.com/apoleptika/turkish-online-supermarkets-search/blob/main/supermarkets-excel.png">
</picture>

This script shows the products that are on the first page yet. <br/>
When there is a product on more than one page, it cannot reach all of them. <br/>
In the future, I will solve this problem and add it to the script. <br/>

Aldin Romanov Aldinov
