import smtplib
import webbrowser
import os
from twilio.rest import Client
OneIteration = 1
print('Please enter your name: ')
myName = input()
print('\nHello ' +myName+', Welcome to SendAEmail\n')
print('This program can only send email using Gmail\n')
print('This program will only work if the ''Allow Less Secure Apps'' is turned on\n')
while(True):
    print('Would you like us to open this webpage in a new tab? We would be honored...\n')
    print('Type Y for Yes and N for No: ')
    guessing = input()
    if(guessing == 'Y'):
        webbrowser.open('https://myaccount.google.com/lesssecureapps')
        break
    elif(guessing == 'N'):
        print('Please visit https://myaccount.google.com/lesssecureapps to do so\n')
        break
    else:
        print('Please try again!\n')
while(True):
    if(OneIteration == 1):
        print('Do you have a Gmail account? Type Y for Yes and N for No.\n')
    answer = input()
    if(answer == 'Y'):
        conn = smtplib.SMTP('smtp.gmail.com', 587)
        conn.ehlo() 
        conn.starttls() #secure transfer protocol
        print('Please enter your username: ')
        username = input()
        print('Thank you for entering your username\n')
        print('Please enter your password: ')
        password = input()
        try:
            conn.login(username+'@gmail.com', password)
        except:
            print('There was an error authenticating your credentials\n')
            print('Please try again')
        else:
            print('We have successfully authenticated your credentials\n')
            print('We thank you for your continued patience\n')
            print('Please type the recipients email address: ')
            recipient = input()
            print('Thank you! Please enter the subject of the email: ')
            subject = input()
            print('\nThank you! Please enter a greeting for the recipient: ')
            greeting = input()
            print('\nThank you! Please enter the body for your email: ')
            body = input()
            print('\nThank you! Please enter a closing greeting: ')
            closing = input()
            conn.sendmail(username+'@gmail.com', recipient,
                  'Subject: '+subject+'\n\n'+greeting+', \n\n'+body+'\n\n'+closing+',\n'+myName)
            conn.quit()
            print('For security purposes, we have logged you out of the system\n')
            print('Would you like to send another email? Type Y for Yes and N for No.\n')
            oneIteration = 0
    elif(answer == 'N'):
        print('Thank you for trying SendAEmail\n')
        print('We hope you try us again!\n')
        while(True):
            print('Would you like to send a text message to remind your recipient that you have sent mail:\n ')
            print('Type Y for Yes and N for No')
            textMsg = input()
            if(textMsg == 'Y'):
                print('Please enter your twilio account SID: ')
                accountSID = input()
                print('\nThank you! Please enter your Twillio Authentication Token: ')
                authToken = input()
                client = Client(accountSID, authToken)
                print('\nPlease enter your twilio account phone number: ')
                phoneNumberUser = input()
                print('\nPlease enter your recipients phone number that you would like to send a message to: ')
                phoneNumberRecipient = input()
                print('\nPlease enter text that you would like to send to that user: \n')
                bodyInput = input()
                try:
                    client.messages.create(to='+1'+phoneNumberRecipient, 
                                           from_='+1'+phoneNumberUser, 
                                           body=bodyInput)
                except:
                    print('Please Try again')
                else:
                    print('We have successfully sent your text message!\n')
                    print('Thank you for trying our text Messaging service!\n')
                    print('Please try us again!')
                    break
            elif(textMsg == 'N'):
                print('We hope you try our service next time!')
                break
            else:
                print('Please try again!')
        break
    else:
        print('Please try again!\n')
