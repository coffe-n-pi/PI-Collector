import requests
import json
import time
from Capper import Capper
from IBM_Device import Device
import wiotp.sdk.device

addr = 'http://130.237.20.126:9003'
test_url = addr + '/api/analyse'

capper = Capper()

content_type = 'image/jpeg'
auth_token = "1QPbwyJeFdi/cpdxHCUGEHKE+uhCIuVJVCdXwc9Nmq8="
headers = {
  'content-type': content_type,
  'Authorization': 'Bearer ' + auth_token
}

arg_cfg = "device.yaml"
iot_platform = True
try:
  dev = Device(arg_cfg)
except:
  print("Can not connect to IoT cloud platform.")
  iot_platform = False

while True:
  try:
    response = requests.post(test_url, data=capper.GetImage().tostring(), headers=headers)
    if response.status_code == 200 and iot_platform:
      try:
        if ("person" in response.json().keys()):
          dev.Publish(response.json())
      except:
        iot_platform = False
    else:
      time.sleep(4)
    # decode response
    print(response.text)
  except:
    print("Server at " + test_url + " is not available!")
    time.sleep(4)
