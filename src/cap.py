import requests
import json
import time
from Capper import Capper
import wiotp.sdk.device

addr = 'http://130.229.181.193:5000'
test_url = addr + '/api/analyse'

capper = Capper()

content_type = 'image/jpeg'
headers = {'content-type': content_type}

def commandProcessor(cmd):
  print("Command received: %s" % cmd.data)

arg_cfg = "device.yaml" 
deviceOptions = wiotp.sdk.device.parseConfigFile(arg_cfg)
deviceCli = wiotp.sdk.device.DeviceClient(deviceOptions)
deviceCli.commandCallback = commandProcessor

# Connect and send datapoint(s) into the cloud
deviceCli.connect()

def myOnPublishCallback():
  print("Confirmed event %s received by IoTF\n" % x)


# Disconnect the device and application from the cloud
while True:
  response = requests.post(test_url, data=capper.GetImage().tostring(), headers=headers)
  # decode response
  print(response.text)

  success = deviceCli.publishEvent("cap_data", "json", response.json(),
                                   qos=0, on_publish=myOnPublishCallback)
  if not success:
    print("Not connected to IoTF")

deviceCli.disconnect()
