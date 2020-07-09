## Mail-trawler: Query email containing congratulations

Problem Statement 9
__________________
Write a program to read and search a given (your) email (with email and password provided to the program) for 5 recent congratulations emails you received.
Input: Email Username, Password, Email: Configuration (Can hardcode in the program)
Output: Subject of 5 Mails
Partial Acceptable Solution: Get last five emails
Complete solution: Get the last five emails containing words similar or equivalent to "congratulation."
Note: You can remove your email and password before submitting and instruct us in the text file to let us put our own email/password to test your code.

<ul>
 <li>Installing relevant packages - <code>pip install -r requirements.txt</code></li>
 <li>Run querymail.py. Enter mailid and password</li>
</ul>


<strong> Note - </strong>
<ul>
 <li>The program is coded for yahoo mail. For using 
gmail, change the line 
<code>imap_host='imap.mail.yahoo.com'</code>
 <br>to<br>
<code>imap_host='imap.gmail.com'</code></li>
 <li>While using a yahoo mail id generate a new "app password", for gmail id "allow less secure apps" from google account settings</li>
</ul>

