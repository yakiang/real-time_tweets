class Session(object):
    sockets_threads_dict = {}

    def set_thread(self, socket, thread=None):
        self.sockets_threads_dict[socket] = thread

    def remove_socket(self, socket):
        del self.sockets_threads_dict[socket]

    def get_socket_by_thread(self, thread):
        pos = self.sockets_threads_dict.values().index(thread)
        return self.sockets_threads_dict.keys()[pos]


session = Session()
