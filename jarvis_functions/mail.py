import smtplib
from jarvis_functions import speaker,text

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vikashverma1799@gmail.com', '8948800765')
    server.sendmail('vikashverma1799@gmail.com', to, content)
    server.close()

def mail(query):
            try:
                speaker.speak("What should I say?")
                content = input()
                to = "recs.cse1649@gmail.com"    
                sendEmail(to, content)
                speaker.speak("Email has been sent!")
            except Exception as e:
                print(e)
                speaker.speak("Sorry my friend harry bhai. I am not able to send this email")
