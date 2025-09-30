# Redix_30_09_2025

python -m venv venv
.\venv\Scripts\python.exe -m pip install redis
.\venv\Scripts\python.exe

### Estabelecendo conexão ###

>>> import redis
>>> r = redis.Redis(host='', port=6379, db=0)
>>> r.ping()
True

### Inserindo Dados ###

>>> r.set('Caio_mykey', 'myvalue')
True

### Obtendo Dados ###

>>> name = r.get('_mykey')
>>> print(name.decode())
myvalue

### Removendo Dados ###

>>> r.delete('_mykey')
1
>>> name = r.get('_mykey')
>>> print(name.decode())
Traceback (most recent call last):
File "", line 1, in print(name.decode())
^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'decode'
