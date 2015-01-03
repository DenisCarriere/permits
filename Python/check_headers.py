import os
import csv
from fieldnames import fieldnames


# Crawl all files within this Folder
for root, folder, files in os.walk('/home/ubuntu/Github/permits/CSV'):
    for file_name in files:
        path = os.path.join(root, file_name)

        change_header = False
        container = []

        # Open each file
        with open(path) as f:
            reader = csv.reader(f)

            # Detect if header is in the correct format
            if not reader.next() == fieldnames:
                
                # Add all lines in empty container to re-write header
                for line in reader:
                    container.append(line)

        # Re-write header fieldnames
        if container:
            with open(path, 'w') as f:
                writer = csv.writer(f)
                writer.writerow(fieldnames)
                writer.writerows(container)
                print 'Change Headers:', file_name