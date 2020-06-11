import smtplib
 
text = "You are being watched" # enter the text mssg
 
ml = smtplib.SMTP ('smtp.gmail.com',587)
 
ml.ehlo()
 
ml.starttls()
 
ml.login('sender mail id @gmail.com','sender email password')# email addres ,and #password
 
#Now here comes the fun part.
#Let's say you want your boss
#to think he got the mail from CIA.
#Type in like nobody@cia.com in place of 
#foremail and your boss's email in place
#of receiver.
 
ml.sendmail('sender mail id@gmail.com','reciver mailid@gmail.com',tt)#sender,recevier
 
ml.close()
