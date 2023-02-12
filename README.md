# Ping
A simple ping program that returns round-trip min/avg/max.

```bash Start the server
python pingserver.py
```

```bash Run the client (against localhost)
python pingclient.py 127.0.0.1
# Or with a modified wait duration
python pingclient.py 127.0.0.1 -i 5
```

Example output assuming there is some delay between the client and server connection.
```
PING 127.0.0.1: 4 data bytes
4 bytes from 127.0.0.1: time=13.000 ms
4 bytes from 127.0.0.1: time=15.000 ms
4 bytes from 127.0.0.1: time=15.000 ms
4 bytes from 127.0.0.1: time=15.000 ms
4 bytes from 127.0.0.1: time=16.000 ms
--- 127.0.0.1 Ping Statistics ---
5 packets transmitted, 5 packets received, 0.00% packet loss
round-trip min/avg/max = 13.000/14.800/16.000 ms
```