from sqlalchemy import create_engine


class DalRepository(object):
    def __init__(self):
        self.connections = []

    def set_connections(self, connections):
        self.connections = connections
        setattr(self, 'connections', connections)
        for connection in connections:
            setattr(self, connection.get('name'), connection.get('connection'))

    def __del__(self):
        for connection in self.connections:
            connection.get('connection') and connection.get('connection').close()



