import requests

HOST = 'http://127.0.0.1:8000'

# 인증 토큰 요청


token = '6c5caa817df8c6190944f232877443dc105135e6'
print(token)

# 인증이 필요한 요청에 헤더 추가
headers = {'Authorization': 'JWT ' + token, 'Accept': 'application/json'}

# Post 생성
data = {
    'title': '제목 by code',
    'text': 'API내용 by code',
    'created_date': '2023-10-09T23:14:00Z',
    'published_date': '2023-10-09T23:14:00Z',
}
files = {'image': ('1.jpg', open('/Users/jws/Desktop/1.jpg', 'rb'))}

res = requests.post(HOST + '/api_root/Post/', data=data, files=files, headers=headers)
print(res)
print(res.json())