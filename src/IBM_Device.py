import wiotp.sdk.device

class Device:
  def __init__(self, arg_cfg):
    device_options = wiotp.sdk.device.parseConfigFile(arg_cfg)
    self.device = wiotp.sdk.device.DeviceClient(device_options)
    self.device.connect()

  def __del__(self):
    self.device.disconnect()

  def Publish(self, data):
    success = self.device.publishEvent("cap_data", "json", data, qos=0)
    if not success:
      print("Not connected to IoTF")
