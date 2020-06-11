import moviepy.editor
video=moviepy.editor.VideoFileClip("WhatsApp Video 2020-06-06 at 8.06.46 PM.mp4")# enter the name of video u want 
audio=video.audio 
audio.write_audiofile("audio.mp3")#enter the replce name for it