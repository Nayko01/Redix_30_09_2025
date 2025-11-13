import redis
import random
import time

r = redis.Redis(host='localhost', port=6379, db=0)
r.ping()

print("Servidor Redis conectado com sucesso!")
print("Aguardando jogadores...")
print("Jogador 1, digite seu nome:")
jogador1 = input()
print("Jogador 2, digite seu nome:")
jogador2 = input()

jogador = (input("você é o jogador 1 ou 2? (digite 1 ou 2)"))
if jogador == "1":
    nome1 = jogador1
    nome2 = jogador2
    sala = f"{random.randint(1, 10000):05.0f}"
    print(f"Seu número de sala é: {sala}. Forneça este número ao Jogador 2 para que ele possa se conectar.")
else:
    nome1 = jogador1
    nome2 = jogador2
    sala = int(input("Digite o número da sala fornecido pelo Jogador 1: "))
print(f"Sala de jogo: {sala}")
r.hset(f"sala:{sala}", "p1", nome1)
r.hset(f"sala:{sala}", "p2", nome2)

print(f"Jogadores {nome1} e {nome2} conectados. Iniciando o jogo...")

#ACABAR DAQUI PRA BAIXO E VER A LOGICA DO JOGADOR 1 E 2 NO MESMO CODIGO DEVERIA TER UMA VEZ A PERGUNTA DO NOME 
#E ELE SE IDENTIFICAR COMO JOGADOR 1 OU 2 

#lugares que tem o valor 9 são a sala de jogo

r.hset(sala, nome1, "")
r.hset(sala, nome2, "")

while(True):
    dados = r.hgetall(sala)
    p1 = dados["p1".encode()].decode()
    p2 = dados["p2".encode()].decode()
    if p1 != "" and p2 != "":
        print(p1, p2)
        exit()