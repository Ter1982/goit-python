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
