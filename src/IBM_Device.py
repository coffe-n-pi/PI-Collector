import wiotp.sdk.device

class Device:
  def __init__(self, arg_cfg):
    device_options = wiotp.sdk.device.parseConfigFile(arg_cfg)
    self.device = wiotp.sdk.device.DeviceClient(device_options)
    self.device.commandCallback = self.__CmdProcessor
    self.device.connect()

  def __del__(self):
    self.device.disconnect()

  def __PublishCallback(self, x):
    print("Confirmed event %s received by IoTF\n" % x)

  def __CmdProcessor(self, cmd):
    print("Command received: %s" % cmd.data)

  def Publish(self, data):
    success = self.device.publishEvent("cap_data", "json", data,
                                       qos=0, on_publish=self.__PublishCallback)
    if not success:
      print("Not connected to IoTF")
