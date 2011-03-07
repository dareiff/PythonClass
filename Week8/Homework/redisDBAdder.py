import redis, random

database = redis.Redis(host='localhost', port=6379)

s = dict()
s["jk"] = 0
listName = "Hello"

for x in range(0,5990):
	randomNumber = random.randint(1,99999)
	# print x, "\t", s[x], "\n"
	database.rpush(listName, randomNumber)
