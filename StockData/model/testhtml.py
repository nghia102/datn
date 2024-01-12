import pandas as pd
url = """https://finance.vietstock.vn/doanh-nghiep-a-z/danh-sach-niem-yet?page=1"""
tables = pd.read_html(url) # Returns list of all tables on page
sp500_table = tables[0] # Select table of interest
print(sp500_table)