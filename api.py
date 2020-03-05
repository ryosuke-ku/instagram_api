from configs import *

import requests
from PIL import Image
from io import BytesIO

# APIのURL
# レスポンス(JSON型)
url = "https://graph.facebook.com/v4.0/17841402028711519?fields=name,media{caption,media_url,permalink,timestamp,username}&access_token=EAAzQWSRzQUQBACBZAqAfZCI96pGjGnZCnPye66Pflb294RqQK37RtsWbEKdizfx0XquJH5ZAghubnpAdqzXDKvjTKsCEdZAeF3iXC6v4i5XGb1IaEkq3Pc4elMGsDVnYoV5cPCaANPnLUxwVZCVwWwGZCwIiZCR2GyosZAZBrnkZCXRigZDZD"
response = requests.get(url).json()
print(response)

# print(response['name'])
# print(response['media']['data'])
# print(response['media']['data'][0]['caption'])
# print(len(response['media']['data']))

for upload_number in range(len(response['media']['data'])):
    print(response['media']['data'][upload_number]['caption'])
    print(response['media']['data'][upload_number]['media_url'])
    print(response['media']['data'][upload_number]['timestamp'])
    timestamp = response['media']['data'][upload_number]['timestamp']
    image_response = requests.get(response['media']['data'][upload_number]['media_url'])
    img = Image.open(BytesIO(image_response.content))
    img.save('images/%s.jpg' % ("photo" + str(upload_number)), 'JPEG', quality=100, optimize=True)
    print(img)

# for data in response['media']:
#     print(data)

# レスポンスに格納されている各データに対する処理
# for d in response['data']:
#     # 画像のID
#     image_id = d['id']
#     # 画像のURL
#     image_url = d['images']['standard_resolution']['url']
#     # 画像のURLからのレスポンス
#     image_response = requests.get(image_url)
#     # レスポンスを変換
#     img = Image.open(BytesIO(image_response.content))
#     # 保存
#     img.save('images/%s.jpg' % (image_id), 'JPEG', quality=100, optimize=True)

