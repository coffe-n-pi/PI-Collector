import requests
import json
from Capper import Capper

addr = 'http://130.229.181.193:5000'
test_url = addr + '/api/test'

capper = Capper()

content_type = 'image/jpeg'
headers = {'content-type': content_type}

while True:
  response = requests.post(test_url, data=capper.GetImage().tostring(), headers=headers)
  # decode response
  print(response.text)
