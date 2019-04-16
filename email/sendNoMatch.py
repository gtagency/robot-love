import subprocess
import csv

#run in python 2, idk if python 3 works for this
#need to follow instructions in the README

baseSubject = 'Subject: Love Machine Results'

baseMessage = "We are sorry to inform you that we were unable to find a match for you. This was due to a couple different factors including the ratios of students who filled out the survey and the nature of the responses we received. We apologize but we believe that you can find love on your own, so dont give up!"

commandStringBase = 'cat mailMessage | msmtp '

with open('NoMatch.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    lineCount = 0
    for row in csv_reader:
        reciever = row[0]
        match = row[1]
        if match == 'Nobody':
            print('sent mail to ' + reciever)
            message = open('mailMessage', 'r+')
            message.truncate(0)
            message.write(baseSubject)
            message.write('\n')
            message.write('\n')
            personalMessage = baseMessage
            message.write(personalMessage)
            message.close()
            commandString = commandStringBase + reciever
            subprocess.call(commandString, shell = True)
            lineCount += 1
        else:
            print('did not send ' + reciever)
    lineCountStr = str(lineCount)
    print('mail sent to ' + lineCountStr + ' addresses')
