class Session(object):
    def __init__(self):
        self.threads_pool = []
        self.sockets_pool = []

    def remove_thread(self, socket):
        pos = self.sockets_pool.index(socket)
        self.threads_pool[pos] = None

    def set_thread(self, socket, thread=None):
        try:
            pos = self.sockets_pool.index(socket)
            self.threads_pool[pos] = thread
        except ValueError:
            self.set_socket(socket)
            self.set_thread(socket, thread)
        except IndexError:
            self.threads_pool.append(thread)

    def remove_socket(self, socket):
        pos = self.sockets_pool.index(socket)
        self.sockets_pool[pos] = None

    def add_socket(self, socket):
        # if it exist?
        self.sockets_pool.append(socket)

    def get_thread_by_socket(self, socket):
        try:
            pos = self.sockets_pool.index(socket)
            return self.threads_pool[pos]
        except ValueError:
            return None

    def get_socket_by_thread(self, thread):
        pos = self.threads_pool.index(thread)
        return self.sockets_pool[pos]


session = Session()
