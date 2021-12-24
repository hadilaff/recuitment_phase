import pandas as pd
from flask  import Flask
from flask_mail import Mail,Message

sheet_id= '19SRkejC_JGrrfuAI6m3dvArUwgHCrtf4KnRxLA1QYpY'
df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv") #convertir data en liste de dictionnaire
records=df.to_dict(orient='records')
x=records[0] #1ere ligne du sheet
y=records[1] #2eme ligne du sheet
z=records[2] #3eme ligne du sheet
print(x)
#print(y)
#print(z)
app=Flask(__name__)

app.config['DEBUG']=True
app.config['TESTING']=False

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

app.config['MAIL_USERNAME']='xxx@gmail.com'
app.config['MAIL_PASSWORD']='xxx'
app.config['MAIL_DEFAULT_SENDER']='xxxx@gmail.com'
app.config['MAIL_MAX_EMAILS']=None

app.config['MAIL_ASCII_ATTACHMENTS']=False

def appl(): #if status=applied
 mail=Mail(app)
 @app.route('/')
 def index():
    msg=Message('Thank you for applying to the project',recipients=['xxx@gmail.com'])
    mail.send(msg)
    return "done"

 if __name__=='__main__':
   
    app.run(host='127.0.0.1', port= 5000, debug=True)    
 


def sorry(): #if status submitted but test<25
    mail=Mail(app)
    @app.route('/')
    def indexx():
         msg=Message('We are sorry to tell you that you did not pass the test',recipients=['xxx@gmail.com'])
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
         msg=Message('We are sorry to tell you that you did not pass the test',recipients=['affeshadil1@gmail.com'])
         mail1.send(msg)
         return "done" 
    if __name__=='__main__':
   # from waitress import serve
    #serve(app,host="127.0.0.1",port=8000)
     app.run(host='127.0.0.1', port= 5000, debug=True) 

for i in records:
     if ((['Status']=='submitted test') and (i.get("Test score")<25)):
      i.update({'Status':'Refusal Mail Sent'})
      i.update({'Mail sent':'24/12/2021 14:40:03'})
      print(i)
      sorry()    
     if (i['Status']=='applied'):
       i.update({'Status':'online test Sent'})
       i.update({'Mail sent':'24/12/2021 14:40:03'})
       print(i)
       appl() 
     if ((i['Status']=='submitted test') and (i.get("Test score")>25)):
      i.update({'Status':'Interview Mail Sent'})
      i.update({'Mail sent':'24/12/2021 14:40:03'})
      print(i)
      interview() 



           
