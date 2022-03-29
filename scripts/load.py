import csv
from stocks.models import Stockval

#To import data from csv file to database
def run():
    file = open('C:/Users/Hp/project/stockmarket/scripts/AAPL.csv')
    read_file=csv.reader(file)
    Stockval.objects.all().delete()
    count=1
    for record in read_file:
        if count==1:
            pass #for header record
        else:
            Stockval.objects.create(date=record[0],open=record[1],high=record[2],low=record[3],close=record[4],adj_close=record[5],volume=record[6])
        count+=1
#command="python mange.py runscript load"  to imort data from csv file to database