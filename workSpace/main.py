import wifi_connect
import socket_LED
import time


def main():  
  while True:
    wifi_connect.connect()
    if wifi_connect.connect():   
     print('not connect')
    break
   
main()

