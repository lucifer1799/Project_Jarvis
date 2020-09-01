import wikipedia
import webbrowser
from jarvis_functions import youtube,facebook, program, google, music
from jarvis_functions import mail,video,wallpaper
from jarvis_functions import speaker


### A FUNCTION FOR JARVIS RESPONSE 
### TAKE ONE INPUT QUERY AND RETURN NOTHING
def jarvis_reply(query) :
	"""
		TAKE A QUERY AND TO PERFORM A TASK ACCORDING TO QUERY
	"""

	#TASK TO YOUTUBE SEARCH
	if 'WIKIPEDIA' in query:
                             speaker.speak('Searching Wikipedia...')
                             query = query.replace("wikipedia", "")
                             results = wikipedia.summary(query, sentences=2)
                             speaker.speak("According to Wikipedia")
                             print(results)
                             speaker.speak(results)
	if "YOUTUBE" in query:
		webbrowser.open("youtube.com")
		#return youtube.youtube(query)
        
    #TASK TO FACEBOOK SEARCH
	if "FACEBOOK" in query:
		webbrowser.open("facebook.com")
		#return facebook.facebook(query)

	#TASK TO GOOGLE SEARCH 
	elif "default" in query:
		return google.google(query)
    
              #TASK TO OPEN PROGRAM 
	elif "OPEN" in query:
		return program.program(query)
		
	#DO SOMETHINGS FOR OTHER TASKS
	
	elif 'PLAY MUSIC' in query:
                             return music.music(query)

	elif 'SEND MAIL' in query:
                             return mail.mail(query)
	elif 'VIDEO SONG' in query:
                             return video.video(query)
	elif 'CHANGE WALLPAPER' in query:
                             return wallpaper.wallpaper(query)
	elif 'SEARCH GOOGLE' in query:
                             webbrowser.open("google.com")
	elif 'SEARCH STACKOVERFLOW' in query:
                             webbrowser.open("stackoverflow.com")
               
        

              

              
                            
            
	
	return
