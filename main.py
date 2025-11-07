import redis
r = redis.Redis(host='localhost', port=6379, db=0)
r.ping()


r.hset("777", "p1", "2")
r.hset("777", "p2", "3")

while(True):
    dados = r.hgetall("777")
    p1 = dados["p1".encode()].decode()
    p2 = dados["p2".encode()].decode()
    if p1 != "" and p2 != "":
        print(p1, p2)
        exit()