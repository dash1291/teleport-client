from watchdog.events import FileSystemEventHandler
import requests

class FSEventHandler(FileSystemEventHandler):
    def __init__(self, *args, **kwargs):
        self.api_base_uri = kwargs['api_base_uri']
        self.api_secret = kwargs['api_secret']
        super(FSEventHandler, self).__init__()

    def dispatch(self, event):
        super(FSEventHandler, self).dispatch(event)

    def on_created(self, event):
        src_path = event.src_path
        data = {}
        files = {'file': open(src_path).read()}
        self.send_request(filepath, 'PUT', data, files)

    def on_moved(self, event):
        src_path = event.src_path
        dest_path = event.dest_path
        data = {'action': 'moved',
                'new_path': dest_path}
        self.send_request(src_path, 'POST', data)

    def on_deleted(self, event):
        src_path = event.src_path
        data = {}
        self.send_request(src_path, 'DELETE', data)

    def on_modified(self, event):
        src_path = event.src_path
        data = {'action': 'modified'}
        files = {'file': open(src_path).read()}
        self.send_request(src_path, 'POST', data, files)

    def send_request(self, resource, method, data, files):
        uri = self.api_base_uri + resource

        # Auth headers
        headers = {'TELEPORT-API-SECRET': self.api_secret}

        if method == 'PUT':
            requests.put(uri, data=data, headers=headers, files=files)
        elif method == 'DELETE':
            requests.delete(uri, headers=headers)
        elif method == 'POST':
            if data['action'] == 'moved':
                requests.post(uri, data=data, headers=headers)
            else:
                requests.post(uri, data=data, files=files)