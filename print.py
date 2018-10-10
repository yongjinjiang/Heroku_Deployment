import time
import send_email_with_attachments 
from send_email_with_attachments import send_an_email
i=0
while i<1000:
   i+=1
   print(i) 
   time.sleep(1)

   if i%50==0:
        file = open('test.txt','w')         
        file.write(f'Hello World,  {i}') 
        file.write(r'This is our new text file1') 
        file.write(r'and this is another line.') 
        file.write(r'Why? Because we can.') 
        file.close() 

        subject = f"haha {i}"
        body = 'Hi there, I am sending this email from Python!'
        send_an_email('test.txt',subject=subject,body=body)

