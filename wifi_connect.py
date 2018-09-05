import network  # wifi 네트워크 모듈 가져오기 
 
def connect():   # 접속을 위한 함수 
  ssid = "SSID"            # 와이파이 SSID  
  password =  "PASSWORLD"  # 와이파이 패스 워드  입력
 
  station = network.WLAN(network.STA_IF) # 와이 파이 모드를 
                                         # STA_IF 모드로 설정
  if station.isconnected() == True:      # 연결이 되면 
      print("Already connected")         # 연결 완료 출력 
      return
 
  station.active(True)                   # 와이파이 모드 활성화  
  station.connect(ssid, password)        # 와이파이 접속 
 
  while station.isconnected() == False:  # 접속이 되지 않으면 계속 반복  
      pass
 
  print("Connection successful")         #접속 완료 출력   
  print(station.ifconfig())              #접속 완료  아이피 어드레스 출력 
