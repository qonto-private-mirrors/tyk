import json

from tyk.session import TykSession
from tyk.request import TykCoProcessRequest

class TykCoProcessObject:
    def __init__(self, object_json):
        self.object = json.loads(object_json)

        self.request = TykCoProcessRequest(self.object['request'])
        self.session = TykSession(self.object['session'])

        # Should we require these keys?

        if 'spec' in self.object:
            self.spec = self.object['spec']
        else:
            self.spec = {}

        if 'hook_type' in self.object:
            self.hook_type = self.object['hook_type']
        else:
            self.spec = {}

    def dump(self):
        self.object['request'] = self.request.__dict__
        self.object['session'] = self.session.__dict__

        return json.dumps(self.object)
