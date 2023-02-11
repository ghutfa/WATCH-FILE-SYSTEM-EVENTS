import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# from_dir = "ENTER THE PATH OF DOWNLOAD FOLDER (USE " / ") in VSC"
# to_dir = "ENTER THE PATH OF DESTINATION FOLDER(USE " / ") in VSC"

from_dir = "C:/Users/i_sub/Downloads"
to_dir = "destination"



# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"Hey, {event.src_path} has been created")
        
    def on_deleted(self, event):
        print(f"Oops! Someone deleted {event.src.path}")

    def on_moved(self, event):
        print(f"Hey, {event.src_path} has been moved")
    
    def on_created(self, event):
        print(f"Hey, {event.src_path} has been modified")

event_handler = FileMovementHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True) 
observer.start()


try: 
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()



        
       


