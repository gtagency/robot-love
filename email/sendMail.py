import subprocess
import csv

#run in python 2, idk if python 3 works for this
#need to follow instructions in the README

baseSubject = 'Subject: Your Love Machine Match has been found'

baseMessage = 'You matched with a person using this email address '

commandStringBase = 'cat mailMessage | msmtp '

with open('addresses.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    lineCount = 0
    for row in csv_reader:
        reciever = row[0]
        match = row[1]
        print('send mail to ' + reciever + ' they matched with ' + match)
        message = open('mailMessage', 'r+')
        message.truncate(0)
        message.write(baseSubject)
        message.write('\n')
        message.write('\n')
        personalMessage = baseMessage + match
        message.write(personalMessage)
        message.close()
        commandString = commandStringBase + reciever
        subprocess.call(commandString, shell = True)
        lineCount += 1
    lineCountStr = str(lineCount)
    print('mail send to ' + lineCountStr + ' addresses')
