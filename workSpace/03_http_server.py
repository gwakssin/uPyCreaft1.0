import socket
import esp
import time


addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

def main():

    import machine
    pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]


    html = """<!DOCTYPE html>
    <html>
    <head> <title>ESP8266 Web Server </title> </head>
    <body> <h1>ESP8266 Pin Status</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
    </body>
    </html>
    """


    LED1 = machine.Pin(4, machine.Pin.OUT)
    LED2 = machine.Pin(5, machine.Pin.OUT)
    LED1.low()
    LED2.high()
    # #

    while True:
        cl, addr = s.accept()
        print('client connected from', addr)
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
            # print(line)
        rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
        response = html % '\n'.join(rows)
        cl.send(response)
        cl.close()

main()


