#!/usr/bin/env python3
import socket
import json

# get broker's IP
payload = '00000065000000617b22636f6465223a3130362c22666c6167223a302c226c616e6775616765223a224a415641222c226f7061717565223a302c2273657269616c697a655479706543757272656e74525043223a224a534f4e222c2276657273696f6e223a3430337d'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nameserver_addr = ('172.19.0.2', 9876)
sock.connect(nameserver_addr)

sock.sendall(bytes.fromhex(payload))

resp = sock.recv(1024)

_json = resp.decode().split("\"")

broker_ip, broker_port = _json[_json.index("brokerAddrs") + 2].split(':')

print(f'Broker address: {broker_ip}:{broker_port}')

sock.close()

# send to broker
payload = '00000064000000607b22636f6465223a32382c22666c6167223a302c226c616e6775616765223a224a415641222c226f7061717565223a342c2273657269616c697a655479706543757272656e74525043223a224a534f4e222c2276657273696f6e223a3430337d'

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nameserver_addr = (broker_ip, int(broker_port))
sock.connect(nameserver_addr)

sock.sendall(bytes.fromhex(payload))

resp = sock.recv(1024)

_json = resp.decode().split("\"")

print(f'Broker version: {_json[_json.index("brokerVersionDesc") + 2]}')

sock.close()
