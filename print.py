import time
import send_email_with_attachments 
from send_email_with_attachments import send_an_email
i=0
while i<1000:
   i+=1
   print(i) 
   
   time.sleep(1)

   if i%50==0:
        f= open('test.txt','w')         
        f.write(f'Hello World,  {i}') 
        f.write(r'This is our new text file1') 
        f.write(r'and this is another line.') 
        f.write(r'Why? Because we can.') 
        f.close() 

        subject = f"haha {i}"
        body = 'Hi there, I am sending this email from Heroku!'
        send_an_email('test.txt',subject=subject,body=body)

