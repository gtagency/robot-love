import csv

#put file called addresses.csv in this directory

with open('addresses.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    lineCount = 0
    for row in csv_reader:
        reciever = row[0]
        match = row[1]
        print('send mail to ' + reciever + ' they matched with ' + match)
        lineCount += 1
    lineCountStr = str(lineCount)
    print('mail send to ' + lineCountStr + ' addresses')
