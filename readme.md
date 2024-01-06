# iMessage status checker
This code will call out to Blue Bubbles server and check if specified numbers/emails are registered with iMessage service.
The main idea is to run this script on a schedule (daily?) and receive an e-mail with the status of registration. 
I believe Blue Bubbles team has something on the roadmap to notify via the app of iMessage registration failure, once that is implemented there won't be much point in this script.
## Usage
This code uses native python3 libraries, so as long as your system has python3, no additional setup is needed. This code should work on all the systems with Python, but I have tested windows only. 
Git clone/download archive/copy-paste the code (whichever way you like), rename `config_sample.json` to `config.json`, adjust values as needed and execute with `python check_imessage.py`
## Configuration
Configuration is expected to be in the `config.json` file located in the same directory as the script. The config is in the json format, so make sure you pay attention to curly brackets, commas and quotes as you edit it, otherwise script won't be able to open it and will fail. 
The following parameters are required:
 - check_imessage_for - list of addresses to check status for. It could be a full phone number with a country code, could be a short version of a number without country code (works in the US, not sure about the rest of the world), or could be an e-mail.
 - bubbles_server - full path to your Blue Bubbles server, including http(s) and any ports you may use.
 - bubbles_pw - password for your Blue Bubbles server (same as what your phone is configured with)
 - send_email - must be `true` or `false`, if true - will send an e-mail
 Optional parameters for e-mail server:
  - smtp_server - your  mail server
  - smpt_server_port - mail server port
  - sender_email - e-mail of a sender, also used to authenticate to mail server
  - receiver_email - e-mail that will receive the notification
  - email_password - password to authenticate to mail server with
## E-mail setup
The script assumes a SMTP server that supports SSL. I've tested it with Gmal only, however any other server should work as well. I am using 2FA with my Google account so I have to create a special Gmal App password for this script to work. I am not sure whether accounts without 2FA can authenticate with their regular username/passwords