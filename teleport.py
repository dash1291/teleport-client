import time
import functools

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

from FSEventHandler import FSEventHandler
from config import *

if __name__ == "__main__":
    callback = functools.partial(FSEventHandler, api_base_uri=API_BASE_URI,
                                 api_secret=API_SECRET)
    event_handler = LoggingEventHandler()
    observer = Observer()
    observer.schedule(FSEventHandler(api_base_uri=API_BASE_URI,
                                 api_secret=API_SECRET), path='.', recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()