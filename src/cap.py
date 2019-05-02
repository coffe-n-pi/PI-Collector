import requests
import json
import time
from Capper import Capper
from IBM_Device import Device
import wiotp.sdk.device

addr = 'http://130.229.181.193:5000'
test_url = addr + '/api/analyse'

capper = Capper()

content_type = 'image/jpeg'
headers = {'content-type': content_type}


arg_cfg = "device.yaml"
dev = Device(arg_cfg)
# Disconnect the device and application from the cloud
while True:
  try:
    response = requests.post(test_url, data=capper.GetImage().tostring(), headers=headers)
    # decode response
    print(response.text)
  except:
    print("Server at " + test_url + " is not available!")
    time.sleep(4)
  dev.Publish(response.json())
