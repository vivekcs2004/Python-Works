email_path = "file-operations/email_procces/emails.txt"
gmail_path = "file-operations/email_procces/gmail.txt"
outlook_path = "file-operations/email_procces/outlook.txt"
yahoo_path = "file-operations/email_procces/yahoo.txt"

fr_email = open(email_path,"r")

fw_gmail = open(gmail_path,"w")

fw_outlook = open(outlook_path,"w")

fw_yahoo = open(yahoo_path,"w")

for line in fr_email:
    
    mail_id = line.rstrip("\n")

    if mail_id.endswith("@gmail.com"):

        fw_gmail.write(mail_id+"\n")
    
    elif mail_id.endswith("@outlook.com"):

        fw_outlook.write(mail_id+"\n")

    else:

        fw_yahoo.write(mail_id+"\n")
