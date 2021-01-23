import pathlib
import string
import sys
import os


picture = []
video = []
document = []
music = []
unknown = []

def search(path):
    dir_path = []
    files = os.listdir(path)
    for file_or_dir in files:
        if os.path.isdir(path + os.path.sep + file_or_dir):
            dir_path.append(path + os.path.sep + file_or_dir)
        else:
            sort_by_type(file_or_dir)  
    while(dir_path):
        search(dir_path.pop())          

def sort_by_type(file_name):
    global picture
    global video
    global document
    global music 
    global unknown
     
    if file_name.endswith('jpeg') or file_name.endswith('png') or file_name.endswith('jpg'):
        picture.append(file_name)
    elif file_name.endswith('avi') or file_name.endswith('mp4') or file_name.endswith('mov'):
        video.append(file_name)
    elif file_name.endswith('doc') or file_name.endswith('docx') or file_name.endswith('txt'):
        document.append(file_name)
    elif file_name.endswith('mp3') or file_name.endswith('ogg') or file_name.endswith('amr') or file_name.endswith('wav'):
        music.append(file_name)
    else:
        unknown.append(file_name)
    
def main():
    path = "C:\\Users\\Asus\\Documents\\Test"
    # sort_by_type(path)
    search(path)
    print(F" Music :{music} Document :{document} Pictures :{picture} Video :{video} Unknown :{unknown}")
    
if __name__ == "__main__":
       main()
