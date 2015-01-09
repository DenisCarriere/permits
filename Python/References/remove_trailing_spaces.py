import os
import csv

# Crawl all files within this Folder
for root, folder, files in os.walk('/home/ubuntu/Github/permits/CSV'):
    for file_name in files:
        path = os.path.join(root, file_name)

        # Store rows to save file later
        container = []
        
        # Open each file 
        with open(path) as f:
            reader = csv.reader(f)

            # Read each row and Remove trailing white spaces
            for line in reader:
                temp_line = []
                for row in line:
                    temp_line.append(row.strip())
                container.append(temp_line)

        # Overwrite file with new lines without trailing spaces
        with open(path, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(container)
            print 'Overwrite File:', file_name
