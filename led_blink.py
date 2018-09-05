import machine
import time                # 시간 지연을 위한 모듈
pin = machine.Pin(0, machine.Pin.OUT)  # pin 번호 0 번을 출력핀으로 설정
val =0                                 # 반복 제어를 위한 변수 선언
while True:                    # 무한 반복         
  val +=1                      # val 변수를 1씩 증가 
  print (val)                  # val 값을 콘솔 출력
  pin.value(1)                 # pin 1 을 입력 led on
  time.sleep(1)                # 시간 지연 1초 
  pin.value(0)                 # led off
  time.sleep(1)                # 시간 지연 1 초 
  if val == 10:                # 만약에 val 이 10 이면 
    break                      # 무한 반복 정지import machine 


