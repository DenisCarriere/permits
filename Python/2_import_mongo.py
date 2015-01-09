#!/usr/bin/python
# coding: utf8
import csv
import os
from pymongo import MongoClient


client = MongoClient()
if client.ottawa.permits.count():
    print 'WARNING: Any existing MongoDB data is getting deleted...'
    client.ottawa.permits.remove({})
base_path = '/home/ubuntu/Github/permits/CSV/{year}/'
base_path += 'Construction-Demolition-Pool-Enclosure-Permits-{month}-{year}.csv'
years = [2011, 2012, 2013, 2014]
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

fieldnames = [
    "ST",
    "ROAD",
    "PC",
    "WARD",
    "PLAN",
    "LOT",
    "CONTRACTOR",
    "BLG_TYPE",
    "MUNICIPALITY",
    "DESCRIPTION",
    "DU",
    "VALUE",
    "FT2",
    "PERMIT",
    "APPL_TYPE",
    "ISSUED_DATE",
]

for year in years:
    for month in months:
        file_path = base_path.format(month=month, year=year)
        filename = os.path.basename(file_path)
        if os.path.exists(file_path):

            # Read the CSV document and store each line to re-write the file with the new headers.
            container = []
            with open(file_path) as f:
                reader = csv.DictReader(f, fieldnames=fieldnames, dialect='excel')
                reader.next()

                for line in reader:
                    line['year'] = year
                    line['month'] = month
                    line['filename'] = filename
                    container.append(line)
                    
            # Load in Mongo
            for line in container:
                client.ottawa.permits.insert(line)
        else:
            print 'File Path ERROR:', file_path