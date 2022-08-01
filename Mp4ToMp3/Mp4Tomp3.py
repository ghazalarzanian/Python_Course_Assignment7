from moviepy import editor 
video = editor.VideoFileClip('1.mp4')
video.audio.write_audiofile('2.mp3')