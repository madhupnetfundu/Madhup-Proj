# get_response_initial.py

def get_response(server, ports=(443, 80)):
    # The ports argument expects a non-empty tuple
    for port in ports:
        if server.connect(port):
            return server.get()
    return None
