#!/usr/bin/python
# coding: utf8
import csv
import os
from datetime import datetime

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

def convert_to_date(string):
    string = string.strip()
    try:
        date = datetime.strptime(string, '%Y-%m-%d')
        return str(date.date())  
    except:
        date = None
    try:
        date = datetime.strptime(string, '%Y-%b-%d')
        return str(date.date())
    except:
        date = None

    if not date:
        print 'Date ERROR:', string
        return string

def convert_to_int(string):
    if string:
        try:
            string = string.replace(',','').strip()
            return int(string)
        except:
            print 'Int ERROR:', string
            return string

def convert_to_postal(string):
    if string:
        string = string.strip()
        if len(string) == 6:
            string = '{0} {1}'.format(string[:3],string[3:])
            return string
        else:
            return string

for year in years:
    for month in months:
        file_path = base_path.format(month=month, year=year)

        if os.path.exists(file_path):

            # Read the CSV document and store each line to re-write the file with the new headers.
            container = []
            with open(file_path) as f:
                reader = csv.DictReader(f, fieldnames=fieldnames, dialect='excel')
                reader.next()

                for line in reader:
                    # Strip all values - Remove white trailing spaces
                    for key, values in line.items():
                        line[key] = values.strip()

                    # Convert attributes to Integers
                    line['VALUE'] = convert_to_int(line.get('VALUE'))
                    line['FT2'] = convert_to_int(line.get('FT2'))
                    line['DU'] = convert_to_int(line.get('DU'))
                    line['PERMIT'] = convert_to_int(line.get('PERMIT'))
                    line['ISSUED_DATE'] = convert_to_date(line.get('ISSUED_DATE'))
                    line['PC'] = convert_to_postal(line.get('PC'))
                    
                    if not line['ISSUED_DATE']:
                        print file_path, line
                        exit()
                    container.append(line)

            with open(file_path, 'w') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames, dialect='excel')
                writer.writeheader()
                writer.writerows(container)
        else:
            print 'File Path ERROR:', file_path