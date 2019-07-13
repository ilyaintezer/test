import redis
import requests


print(requests.get('http://google.com').content)

print("hello")
r = redis.Redis(host='localhost', port=6379, db=0,charset="utf-8", decode_responses=True)

r.set('foo', 'bar')

print(r.rpush('foo',ds))
