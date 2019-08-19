import time
import os
import sys
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

doc = ['.txt', '.doc', 'docx', '.ppt', '.pptx']
video = ['.mp4', '.flc', '.mkv', 'avi', 'mov', 'webm', 'wmv']
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    # path = sys.argv[1] if len(sys.argv) > 1 else '.'
    path = "/path/to/directory/"
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path)
    observer.start()

    path_to_file = " /path/to/directory/where/the/file/should/reside" 

    def on_created(event):
        file_name = event.src_path
        file_name = file_name.replace(" ", "\ ").replace("(", "\(").replace(")", "\)")
        myCmd = 'mv ' + file_name + path_to_file
        for x in range(len(doc)):
            if file_name.endswith(doc[x]):
                os.system(myCmd)

    def on_modified(event):
        file_name = event.src_path
        file_name = file_name.replace(" ", "\ ").replace("(", "\(").replace(")", "\)")
        myCmd = 'mv ' + file_name + path_to_file
        for x in range(len(doc)):
            if file_name.endswith(doc[x]):
                os.system(myCmd)

    def on_moved(event):
        file_name = event.dest_path
        file_name = file_name.replace(" ", "\ ").replace("(", "\(").replace(")", "\)")
        myCmd = 'mv ' + file_name + path_to_file
        for x in range(len(doc)):
            if file_name.endswith(doc[x]):
                os.system(myCmd)

event_handler.on_created = on_created
event_handler.on_modified = on_modified
event_handler.on_moved = on_moved

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()