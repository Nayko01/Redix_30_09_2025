
def player1():
    print("Jogador 1, digite seu nome:")
    jogador1 = input()
    nome1 = jogador1
        
    print("Criando sala de jogo...")
        
    sala = f"{random.randint(1, 10000):05.0f}"
        
    print(f"Seu número de sala é: {sala}. Forneça este número ao Jogador 2 para que ele possa se conectar.")

    # grava os campos `jogador1` e `jogador2` dentro do hash da sala
    r.hset(f"sala:{sala}", mapping={"jogador1": nome1, "jogador2": "", "jogada1": ""})

    return sala, nome1

def player2():
    print("Jogador 2, digite seu nome:")
    jogador2 = input()
    nome2 = jogador2
    sala =(input("Digite o número da sala fornecido pelo Jogador 1: "))
    # grava apenas o campo `jogador2` no hash da sala fornecida
    r.hset(f"sala:{sala}", mapping={"jogador2": nome2, "jogada2": ""})

    return sala, nome2

def jogada1():
    print("Jogador 1, faça sua jogada (pedra, papel ou tesoura):")
    jogada1 = input().lower()
    sala = sala
    r.hset(f"sala:{sala}", "jogada1", jogada1)
    return sala, jogada1

def jogada2():
    print("Jogador 2, faça sua jogada (pedra, papel ou tesoura):")
    jogada2 = input().lower()
    sala = sala
    r.hset(f"sala:{sala}", "jogada2", jogada2)
    return sala, jogada2


import redis
import random
import time

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.ping()

print("Servidor Redis conectado com sucesso!")
print("Aguardando jogadores...")

#valor usado para identificar o jogador e chamar suas devidas funções.
jogador = (input("você é o jogador 1 ou 2? (digite 1 ou 2)"))

if jogador == "1":
    sala, nome1 = player1()
elif jogador == "2":
    sala, nome2 = player2()
else:
    print("Opção inválida. Execute novamente e digite 1 ou 2.")
    raise SystemExit(1)

key = f"sala:{sala}"

dados = r.hgetall(key)
p1 = dados.get("jogador1", "")
p2 = dados.get("jogador2", "")
print(f"Aguardando jogadores na sala {sala}... Jogador 1: {p1} | Jogador 2: {p2}\n")

timeout = 60  
start_time = time.time()

while not (p1 and p2):
    if time.time() - start_time > timeout:
        print(f"Ainda aguardando jogadores na sala {sala}... Jogador 1: {p1 or '<vazio>'} | Jogador 2: {p2 or '<vazio>'}\n")
        start_time = time.time()
    time.sleep(1)
    dados = r.hgetall(key)
    p1 = dados.get("jogador1", "")
    p2 = dados.get("jogador2", "")
print("Ambos os jogadores estão presentes. Iniciando o jogo...")

if jogador == "1":
    sala, jogou1 = jogada1()
elif jogador == "2":
    sala, jogou2 = jogada2()

dados = r.hgetall(key)
p1 = dados.get("jogada1", "")
p2 = dados.get("jogada2", "")
print(f"Aguardando jogada, Jogador 1: {p1} | Jogador 2: {p2}\n")

timeout = 60  
start_time = time.time()

while not (p1 and p2):
    if time.time() - start_time > timeout:
        print(f"Aguardando jogada, Jogador 1: {p1 or '<vazio>'} | Jogador 2: {p2 or '<vazio>'}\n")
        start_time = time.time()
    time.sleep(1)
    dados = r.hgetall(key)
    p1 = dados.get("jogada1", "")
    p2 = dados.get("jogada2", "")

print("Ambos os jogadores fizeram suas jogadas.")
print(f"Jogador 1 jogou: {p1}")
print(f"Jogador 2 jogou: {p2}")
if p1 == p2:
    print("Empate!")
elif (p1 == "pedra" and p2 == "tesoura") or (p1 == "papel" and p2 == "pedra") or (p1 == "tesoura" and p2 == "papel"):
    print("Jogador 1 vence!")
else:
    print("Jogador 2 vence!")



