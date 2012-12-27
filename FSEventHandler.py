from datetime import date
import os.path

from watchdog.events import FileSystemEventHandler
import requests

class FSEventHandler(FileSystemEventHandler):
    def __init__(self, *args, **kwargs):
        self.api_base_uri = kwargs['api_base_uri']
        self.api_secret = kwargs['api_secret']
        self.path_prefix = kwargs['path_prefix']
        super(FSEventHandler, self).__init__()

    def dispatch(self, event):
        if not event.is_directory:
            super(FSEventHandler, self).dispatch(event)

    def on_created(self, event):
        src_path = event.src_path
        date_str = str(date.fromtimestamp(os.path.getmtime(src_path)))
        prefix_cut_path = src_path[len(self.path_prefix):]
        data = {'action': 'created', 'last_modified': date_str}
        files = {'file': open(src_path, 'rb')}
        self.send_request(prefix_cut_path, 'POST', data, files)

    def on_moved(self, event):
        src_path = event.src_path
        prefix_cut_src_path = src_path[len(self.path_prefix):]
        dest_path = event.dest_path
        prefix_cut_dest_path = dest_path[len(self.path_prefix):]
        data = {'action': 'moved',
                'new_path': prefix_cut_dest_path}
        self.send_request(prefix_cut_src_path, 'POST', data)

    def on_deleted(self, event):
        src_path = event.src_path
        data = {}
        self.send_request(src_path, 'DELETE', data)

    def on_modified(self, event):
        src_path = event.src_path
        prefix_cut_path = src_path[len(self.path_prefix):]
        date_str = str(date.fromtimestamp(os.path.getmtime(src_path)))
        data = {'action': 'modified', 'last_modified': date_str}
        files = {'file': open(src_path, 'rb')}
        self.send_request(prefix_cut_path, 'POST', data, files)

    def send_request(self, resource, method, data, files):
        uri = self.api_base_uri + resource + '/'

        # Auth headers
        headers = {'TELEPORT-API-SECRET': self.api_secret}

        if method == 'DELETE':
            a = requests.delete(uri, headers=headers)
        elif method == 'POST':
            if data['action'] == 'moved':
                a = requests.post(uri, data=data, headers=headers)
            else:
                a = requests.post(uri, data=data, headers=headers, files=files)
        print a.text
