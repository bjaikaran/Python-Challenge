
import numpy as np
import pandas as pd

#csv = input("Enter the full path of the first Budget Data file for your CSV: ")
#csv_path = str(csv)
csv_path ="resources/budget_data_a.csv"
wFile = str(csv_path[:-3]+"txt")

bf = pd.read_csv(csv_path, encoding="utf-8")

bf["Date"] = bf["Date"].str.replace("20","")
months = bf["Date"].nunique()
bd_trev = bf["Revenue"].sum()
avg_rev= int(bf["Revenue"].mean())
bd_maxrev = bf["Revenue"].max()   
max_rev=bf.loc[bf["Revenue"] == bd_maxrev,:]
mxdate=str(max_rev.iloc[0]["Date"])
mxval=str(bd_maxrev)
bd_minrev = bf["Revenue"].min()
min_rev=bf.loc[bf["Revenue"] == bd_minrev,:]
mndate=str(min_rev.iloc[0]["Date"])
mnval=str(bd_minrev)
f= open(wFile,"w+")
print("Total Months: "+'{:,}'.format(months))
f.write("Total Months: "+'{:,}'.format(months)+"\n")
print("Total Revenue: $"+'{:,}'.format(bd_trev))
f.write("Total Revenue: $"+'{:,}'.format(bd_trev)+"\n")
print("Average Revenue Change: $"+'{:,}'.format(avg_rev))
f.write("Average Revenue Change: $"+'{:,}'.format(avg_rev)+"\n")
print("Greatest Increase in Revenue: "+mxdate+" ("+mxval+")")
f.write("Greatest Increase in Revenue: "+mxdate+" ("+mxval+")"+"\n")
print("Greatest Decrease in Revenue: "+mndate+" ("+mnval+")")
f.write("Greatest Decrease in Revenue: "+mndate+" ("+mnval+")"+"\n")
f.close()

