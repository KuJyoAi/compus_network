from urllib3 import encode_multipart_formdata

import requests

target_url = "http://yanderemoe.xyz/"
data = {
    "status": "111",
    "timestamp": "",
    "ipv4": "",
    "ipv6": "",
}
# 发送表单数据
res = requests.post(target_url, data=data)
print(res.text)