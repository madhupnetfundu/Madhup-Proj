# get_response_assert.py

def get_response(server, ports=(443, 80)):
    assert len(ports) > 0, f"ports expected a non-empty tuple, got{ports}"
    for port in ports:
        if server.connect(port):
            return server.get()
    return None