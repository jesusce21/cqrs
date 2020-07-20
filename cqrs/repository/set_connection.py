dal_connections = {
    "read_connection": f"postgres://{os.getenv('dal_connections')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}",
    "write_connection": f"postgres://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
}


def set_connections(*args):
    class Connection:
        def __init__(self, cls):
            self.connections = args
            self.other_class = cls

        def __call__(self, *cls_ars):
            dal_repository = self.other_class(*cls_ars)

            connections = [{"name": connection, "connection": create_engine(dal_connections.get(connection)).connect()}
                           for
                           connection in self.connections]
            dal_repository.set_connections(connections)
            return dal_repository

    return Connection
