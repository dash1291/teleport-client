import time

from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer

from config import *
from FSEventHandler import FSEventHandler

if __name__ == "__main__":
    observer = Observer()
    observer.schedule(FSEventHandler(api_base_uri=API_BASE_URI,
        api_secret=API_SECRET, path_prefix=PATH_PREFIX), path='.',
        recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()