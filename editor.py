class editor:
    def __init__(self, filename=""):
        self.fd = filename
        if  self.fd!="" :  # Not ""
            self.source = self.read(filename)
        else:
            self.source = []
    def read(self, fn):
        return open(fn, 'r').read().split('\n')
    def append(self, arr):
        assert type(arr) is list
        for item in arr:
            self.source.append(item)
    def write(self):
        f = open(self.fd, 'w')
        payload = ""
        for item in self.source:
            payload += (item + '\n')
        f.write(payload)
        f.close()

