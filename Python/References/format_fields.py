import os
import csv
from datetime import datetime
from fieldnames import fieldnames


# Crawl all files within this Folder
for root, folder, files in os.walk('/home/ubuntu/Github/permits/CSV'):
    for file_name in files:
        path = os.path.join(root, file_name)

        # Empty container to store edited rows
        container = []
        modified = False

        # Open each file
        with open(path) as f:
            reader = csv.DictReader(f)

            # Read each line from CSV document
            for line in reader:
                
                # Remove [,] character (ex: 200,000 = 200000)  
                value = line.get('VALUE')
                if ',' in value:
                    line['VALUE'] = int(value.replace(',',''))
                    modified = True

                # Modify Postal Code, add a single space
                postal = line.get('PC')
                if len(postal) == 6:
                    postal = '{0} {1}'.format(postal[:3],postal[3:])
                    line['PC'] = postal
                    modified = True

                # Modify Datetime to ISO standard, 2011-Dec-01 >> 2011-12-01
                date = line.get('ISSUED DATE')
                try:
                    date = datetime.strptime(date, '%Y-%b-%d')
                    line['ISSUED DATE'] = str(date.date())
                    modified = True
                except:
                    pass
                    
                # Add line to be saved
                container.append(line)

        # Save document
        if modified:
            with open(path,'w') as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(container)
                print 'Formatted Fields:', file_name
