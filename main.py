### Estabelecendo conexão ###

import redis
r = redis.Redis(host='10.1.68.172', port=6379, db=0)
r.ping()
# True

# ### Inserindo Dados ###

r.set('Caio_mykey', 'myvalue')
# True

# ### Obtendo Dados ###

name = r.get('Caio_mykey')
print(name.decode())
# myvalue

# ### Removendo Dados ###

r.delete('Caio_mykey')
# 1
name = r.get('Caio_mykey')
print(name.decode())
# Traceback (most recent call last):
# File "", line 1, in print(name.decode())
# ^^^^^^^^^^^
# AttributeError: 'NoneType' object has no attribute 'decode'
