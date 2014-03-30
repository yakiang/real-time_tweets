class Session(object):
    ''' A dict that globally stores sockets and its corresponding thread object
    '''
    sockets_threads_dict = {}

    def set_thread(self, socket, thread=None):
        self.sockets_threads_dict[socket] = thread

    def remove_socket(self, socket):
        del self.sockets_threads_dict[socket]

    def get_socket_by_thread(self, thread):
        ''' Get key by value
        '''
        pos = self.sockets_threads_dict.values().index(thread)
        return self.sockets_threads_dict.keys()[pos]


session = Session()
