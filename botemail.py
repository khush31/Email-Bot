import smtplib 
import speech_recognition as sr       
import pyttsx3  
from email.message import EmailMessage

listener=sr.Recognizer()     
engine= pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening......')
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(receiver, subject, content):
    server= smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('kanak56kumari@gmail.com', 'Kanak@56Kumari')
    email= EmailMessage()
    email['From']= 'kanak56kumari@gmail.com'
    email['To']= receiver
    email['Subject']= subject
    email.set_content(content)
    server.send_message(email)






email_list={
    'lady': 'shrutikhati213@gmail.com',
    'khush': 'k319kr@gmail.com',
    'rose': 'singhrewa65@gmail.com'

}



def get_email_info():                 #get voice
    talk('To whom you want to send email')
    name= get_info()
    reciever=email_list[name]
    print(reciever)

    talk('Subject of your email')
    subject= get_info()

    talk('Content of the email')
    content= get_info()
    
    send_email(reciever, subject, content)
    
    talk('your email is sent')
    talk('You want sent more email??')
    
    send_more= get_info()
    if 'yes' in send_more:
        get_email_info()
    elif 'no' in send_more:
        talk('thanks for your emails')
get_email_info()
