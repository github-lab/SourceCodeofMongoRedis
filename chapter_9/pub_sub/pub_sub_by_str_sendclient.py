import redis
import datetime
import json


client = redis.Redis()

while True:
    message = input('请输入需要发布的信息：')
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {'message': message, 'time': now_time}
    client.set('message', json.dumps(data))
