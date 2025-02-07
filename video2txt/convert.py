import moviepy as mp 
import speech_recognition as sr 
  
# Load the video 
video = mp.VideoFileClip("video.mp4") 
  
# Extract the audio from the video 
audio_file = video.audio 
audio_file.write_audiofile("sound.wav") 
  
# Initialize recognizer 
r = sr.Recognizer() 
  
# Load the audio file 
with sr.AudioFile("sound.wav") as source: 
    data = r.record(source) 
  
# Convert speech to text 
help(r.recognize_google)
text = r.recognize_google(data) 
  
# Print the text 
print("\nThe resultant text from video is: \n") 
print(text) 