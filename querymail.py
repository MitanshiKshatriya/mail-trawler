import imaplib
#import getpass
import pprint
import email
import datetime

#for printing last 5 emails
def process_mailbox_last5messages(M):
    
    tmp, data = M.search(None, "ALL")
    if tmp != 'OK':
        print("No messages found!")
        return

    len_data_split_uid = len(data[0].split())
    
    for num in data[0].split()[len_data_split_uid-5:len_data_split_uid]:
        tmp, data = M.fetch(num, '(RFC822)')
        if tmp != 'OK':
            print("ERROR getting message", num)
            return

        msg = email.message_from_bytes(data[0][1])
        hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
        subject = str(hdr)
        print('Subject of email %s: %s' % (num, subject))
        
        # Now convert to local date-time
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple))
            print ("Local Date:", \
                local_date.strftime("%a, %d %b %Y %H:%M:%S"))

#for printing last 5 congratulation emails
def process_mailbox_congratulations(M):

    #for custom search inputs
    #text_to_be_searched = input('Enter the keyword to be searched: ')
    #tmp, data = M.uid('search',None, '(TEXT )')
    
    tmp, data = M.uid('search',None, '(TEXT "congratulation")')
    
    if tmp != 'OK':
        print("No messages found!")
        return

    len_data_split_uid = len(data[0].split())

    if(len_data_split_uid<=5):
        for num in data[0].split():
            tmp, data = M.fetch(num, '(RFC822)')
            if tmp != 'OK':
                print("ERROR getting message", num)
                return

            msg = email.message_from_bytes(data[0][1])
            hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
            subject = str(hdr)
            print('Subject of email %s: %s' % (num, subject))
            
            # Now convert to local date-time
            date_tuple = email.utils.parsedate_tz(msg['Date'])
            if date_tuple:
                local_date = datetime.datetime.fromtimestamp(
                    email.utils.mktime_tz(date_tuple))
                print ("Local Date:", \
                    local_date.strftime("%a, %d %b %Y %H:%M:%S"))
            return

    for num in data[0].split()[len_data_split_uid-5:len_data_split_uid]:
        tmp, data = M.fetch(num, '(RFC822)')
        if tmp != 'OK':
            print("ERROR getting message", num)
            return

        msg = email.message_from_bytes(data[0][1])
        hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
        subject = str(hdr)
        print('Subject of email %s: %s' % (num, subject))
        
        # Now convert to local date-time
        date_tuple = email.utils.parsedate_tz(msg['Date'])
        if date_tuple:
            local_date = datetime.datetime.fromtimestamp(
                email.utils.mktime_tz(date_tuple))
            print ("Local Date:", \
                local_date.strftime("%a, %d %b %Y %H:%M:%S"))

#for gmail
#imap_host='imap.gmail.com'
#imap_port=993

imap_host='imap.mail.yahoo.com'
imap_port=993
##imap_user = input('Enter your email id: ')
##imap_password=getpass.getpass()

imap_user = input("enter your email address: ")
imap_password = input("enter your password: ")

# connection to host using SSL
imap = imaplib.IMAP4_SSL(imap_host,imap_port)

#login
imap.login(imap_user,imap_password)

#printing list of mail boxes
tmp, mailboxes = imap.list()
if tmp=='OK':
    print('Mailboxes: ')
    print(mailboxes)

#selecting a mailbox
imap.select(mailbox='INBOX')

#Printing the emails 

tmp, data = imap.search(None, 'ALL')
#print(data)

if tmp == 'OK':
    print('mailbox: \n')
    process_mailbox_congratulations(imap)
else:
    print("Error unable to print mailboxes")


imap.close()
