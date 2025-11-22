
def player1():
    print("Jogador 1, digite seu nome:")
    jogador1 = input()
    nome1 = jogador1
        
    print("Criando sala de jogo...")
        
    sala = f"{random.randint(1, 10000):05.0f}"
        
    print(f"Seu número de sala é: {sala}. Forneça este número ao Jogador 2 para que ele possa se conectar.")

    # grava os campos `jogador1` e `jogador2` dentro do hash da sala
    r.hset(f"sala:{sala}", "jogador1", nome1)
    r.hset(f"sala:{sala}","jogador2", "")
    r.hset(f"sala:{sala}","jogada1", "")                                

    return sala, nome1

def player2():
    print("Jogador 2, digite seu nome:")
    jogador2 = input()
    nome2 = jogador2
    sala =(input("Digite o número da sala fornecido pelo Jogador 1: "))
    # grava apenas o campo `jogador2` no hash da sala fornecida
    r.hset(f"sala:{sala}","jogador2", nome2)
    r.hset(f"sala:{sala}","jogada2","")
    return sala, nome2

def jogada1():
    print("Jogador 1, faça sua jogada (pedra, papel ou tesoura):")
    jogada1 = input()
    r.hset(f"sala:{sala}","jogada1", jogada1)
    return jogada1

def jogada2():
    print("Jogador 2, faça sua jogada (pedra, papel ou tesoura):")
    jogada2 = input()
    r.hset(f"sala:{sala}","jogada2", jogada2)
    return jogada2


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

#chave da sala
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
    jogou1 = jogada1()
elif jogador == "2":
    jogou2 = jogada2()

dados = r.hgetall(key)
jogou1 = dados.get("jogada1", "")
jogou2 = dados.get("jogada2", "")
print(f"Aguardando jogada, Jogador 1: {jogou1} | Jogador 2: {jogou2}\n")

timeout = 60  
start_time = time.time()

while not (jogou1 and jogou2):
    if time.time() - start_time > timeout:
        print(f"Aguardando jogada, Jogador 1: {jogou1 or '<vazio>'} | Jogador 2: {jogou2 or '<vazio>'}\n")
        start_time = time.time()
    time.sleep(1)
    dados = r.hgetall(key)
    jogou1 = dados.get("jogada1", "")
    jogou2 = dados.get("jogada2", "")

print("Ambos os jogadores fizeram suas jogadas.")
print(f"Jogador 1 jogou: {jogou1}")
print(f"Jogador 2 jogou: {jogou2}")
if jogou1 == jogou2:
    print("Empate!")
elif (jogou1 == "pedra" and jogou2 == "tesoura") or (jogou1 == "papel" and jogou2 == "pedra") or (jogou1 == "tesoura" and jogou2 == "papel"):
    print("Jogador 1 vence!")
else:
    print("Jogador 2 vence!")

r.get(key)
remocao = r.delete(key)
if remocao == 1:    
    print("Jogo encerrado. Dados da sala removidos do Redis.")



