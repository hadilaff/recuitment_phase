from flask import Flask
from flask_mail import Mail, Message
import pandas as pd

app =Flask(__name__)
mail=Mail(app)

#Global Variables
Sender = ""
Password = ""
Sheet_ID = ""

#configurations
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'hadilaffes2@gmail.com'
app.config['MAIL_PASSWORD'] = 'hadilaff123'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

#Function to format and send emails
def send_message(Subject, Recipient, Sender, Body="Default text"):
    mail=Mail(app)
    msg=Message(Subject, recipients=['**1@gmail.com'], sender = Sender)
    msg.body = Body
    mail.send(msg)
    return

#Function to open and parse spreadsheet data
Sheet_ID='19SRkejC_JGrrfuAI6m3dvArUwgHCrtf4KnRxLA1QYpY'
def get_file(Sheet_ID):
    
    totalTestScore = 50 #Set the test score here
    halfTestScore = totalTestScore / 2
    df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{Sheet_ID}/export?format=csv") #convertir data en liste de dictionnaire
    records = df.to_dict(orient='records')
    for i in records:
        if (i['Test score'] < halfTestScore and (i['Status']=='submitted test')):
            send_message("Test Confirmation", i['Email'], Sender, "We are sorry to tell you that you did not pass the test.")
            i.update({'Mail sent':'test'})
        elif(i['Test score'] > halfTestScore and (i['Status']=='submitted test')):
            send_message("Test Confirmation", i['Email'], Sender, "Congratulations for passing the test. You’ll have an interview")
        elif (i['Status']=='applied'):
            send_message("Test Confirmation", i['Email'], Sender, "Thank you for applying to the project")
#Index Route for Flask
@app.route("/")
def index():
   get_file(Sheet_ID) #put your file id here
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)