import subprocess
import csv

baseSubject = 'Subject: Your Love Machine match will be available soon!'

baseMessage = 'Lookout from an email from this address within the next day or so. Check your spam folder'

commandStringBase = 'cat mailMessage | msmtp '

with open('addresses.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    lineCount = 0
    for row in csv_reader:
        reciever = row[0]
        print('Sent mail to ' + reciever)
        message = open('mailMessage', 'r+')
        message.truncate(0)
        message.write(baseSubject)
        message.write('\n')
        message.write('\n')
        message.write(baseMessage)
        message.close()
        commandString = commandStringBase + reciever
        subprocess.call(commandString, shell = True)
        lineCount += 1
    lineCountStr = str(lineCount)
    print('mail sent to ' + lineCountStr + ' addresses')
