<<<<<<< HEAD:Lesson3/Hw_4.py
import os
import sys
import string

picture = []
video = []
document = []
music = []
unknown = []
path = "C:\\Users\\Asus\\Documents\\Test"
files = os.listdir(path)


for file_name in files:
    if file_name.endswith('jpeg') or file_name.endswith('png') or file_name.endswith('jpg'):
        picture.append(file_name)
        continue
    if file_name.endswith('avi') or file_name.endswith('mp4') or file_name.endswith('mov'):
        video.append(file_name)
        continue
    if file_name.endswith('doc') or file_name.endswith('docx') or file_name.endswith('txt'):
        document.append(file_name)
        continue
    if file_name.endswith('mp3') or file_name.endswith('ogg') or file_name.endswith('amr') or file_name.endswith('wav'):
        music.append(file_name) 
        continue
    unknown.append(file_name)
print(F"Music :{music} Document :{document} Pictures :{picture} Video :{video} Unknown :{unknown}")
=======
import os
import sys
import string

picture = []
video = []
document = []
music = []
unknown = []
path = "C:\\Users\\Documents\\Test"
files = os.listdir(path)

for file_name in files:
    if file_name.endswith('JPEG') or file_name.endswith('PNG') or file_name.endswith('JPG'):
        picture.append(file_name)
        continue
    if file_name.endswith('AVI') or file_name.endswith('MP4') or file_name.endswith('MOV'):
        video.append(file_name)
        continue
    if file_name.endswith('DOC') or file_name.endswith('DOCX') or file_name.endswith('TXT'):
        document.append(file_name)
        continue
    if file_name.endswith('MP3') or file_name.endswith('OGG') or file_name.endswith('AMR') or file_name.endswith('WAV'):
        music.append(file_name) 
        continue
    unknown.append(file_name)
    print(F" Music :{music} Document :{document} Pictures :{picture} Video :{video} Unknown :{unknown}")
>>>>>>> 58142f8a6e7fd108faeb0a7760cbae40a19a5a1f:Lesson3/hw_4.py
