import os
import re

# Crawl all files within this Folder
for root, folder, files in os.walk('/home/ubuntu/Github/permits/CSV'):
    for file_name in files:
        path = os.path.join(root, file_name)

        # Replace spelling mistake in filename words
        if 'Demoilition' in path:
            os.rename(path, path.replace('Demoilition', 'Demolition'))
            print 'Replace:',file_name

        # Add Start Metatags to filename
        start = 'Construction-Demolition-Pool-Enclosure-Permits-'
        if not start in file_name:
            os.rename(path, os.path.join(root, start + file_name))
            print 'Added Start:', file_name

        # Check Month & Year are consistent (ex: Sep-2014)
        # Make Full months instead of 3 characters
        months = {
            'Jan': 'January',
            'Feb': 'February',
            'Mar': 'March',
            'Apr': 'April',
            'May': 'May',
            'Jun': 'June',
            'Jul': 'July',
            'Aug': 'August',
            'Sep': 'September',
            'Oct': 'October',
            'Nov': 'November',
            'Dec': 'December',
        }
        expression = r"([A-Z][a)-z]{2})-\d{4}"
        pattern = re.compile(expression)
        match = pattern.search(file_name)
        if match:
            short_month = match.group(1)
            os.rename(path, path.replace(short_month, months[short_month]))
            print 'Added Full Month:', file_name