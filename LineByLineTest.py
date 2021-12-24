import pandas as pd
from flask import Flask,render_template
from flask_mail import Mail,Message
#connect to my gmail account
sheet_id= '19SRkejC_JGrrfuAI6m3dvArUwgHCrtf4KnRxLA1QYpY'
df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv") #convertir data en liste de dictionnaire
records=df.to_dict(orient='records')
print(records)
x=records[0]
y=records[1]
z=records[2]
print(x)
print(y)
print(z)
app=Flask(__name__)

app.config['DEBUG']=True
app.config['TESTING']=False

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
       #app.config['MAIL_DEBUG']=True
app.config['MAIL_USERNAME']='****@gmail.com'
app.config['MAIL_PASSWORD']='***'
app.config['MAIL_DEFAULT_SENDER']='**@gmail.com'
app.config['MAIL_MAX_EMAILS']=None
       #app.config['MAIL_SUPPRESS_SEND']=False
app.config['MAIL_ASCII_ATTACHMENTS']=False


def appl():
    mail=Mail(app)
    @app.route('/')
    def index():
         msg=Message('Thank you for applying to'+records['Project'],recipients=['a**@gmail.com'])
         mail.send(msg)
         return "done"

    if __name__=='__main__':
   # from waitress import serve
    #serve(app,host="127.0.0.1",port=8000)
          app.run(host='127.0.0.1', port= 5000, debug=True)   


def sorry():
    mail=Mail(app)
    @app.route('/')
    def index():
         msg=Message('We are sorry to tell you that you did not pass the test',recipients=['****@gmail.com'])
         mail.send(msg)
         return "done"

    if __name__=='__main__':
   # from waitress import serve
    #serve(app,host="127.0.0.1",port=8000)
        app.run(host='127.0.0.1', port= 5000, debug=True)

def interview():   #if status submitted and test>25
    mail1=Mail(app)
    @app.route('/')
    def indexxx():
         msg=Message('We are sorry to tell you that you did not pass the test',recipients=['****@gmail.com'])
         mail1.send(msg)
         return "done" 
    if __name__=='__main__':
   # from waitress import serve
    #serve(app,host="127.0.0.1",port=8000)
     app.run(host='127.0.0.1', port= 5000, debug=True) 


if ((x['Status']=='submitted test') and (x.get("Test score")<25)):
     x.update({'Status':'Refusal Mail Sent'})
     x.update({'Mail sent':'24/12/2021 14:40:03'})
     print(x)
     sorry()   
if (y['Status']=='applied'):
     y.update({'Status':'online test Sent'})
     y.update({'Mail sent':'24/12/2021 14:40:03'})
     appl()

if ((z['Status']=='submitted test') and (z.get("Test score")>25)):
      z.update({'Status':'Interview Mail Sent'})
      z.update({'Mail sent':'24/12/2021 14:40:03'})
      print(z)
      interview()  