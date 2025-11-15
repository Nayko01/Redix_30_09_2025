
def player1():
    print("Jogador 1, digite seu nome:")
    jogador1 = input()
    nome1 = jogador1
        
    print("Criando sala de jogo...")
        
    sala = f"{random.randint(1, 10000):05.0f}"
        
    print(f"Seu número de sala é: {sala}. Forneça este número ao Jogador 2 para que ele possa se conectar.")

    # usa chave com prefixo para ficar consistente com o resto do código
    r.hset(f"sala:{sala}", "p1", nome1)

    return sala, nome1


def player2():
    print("Jogador 2, digite seu nome:")
    jogador2 = input()
    nome2 = jogador2
    sala =(input("Digite o número da sala fornecido pelo Jogador 1: "))
    # usa chave com prefixo e salva como p2
    r.hset(f"sala:{sala}", "p2", nome2)

    return sala, nome2



import redis
import random
import time

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.ping()

print("Servidor Redis conectado com sucesso!")
print("Aguardando jogadores...")

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
p1 = dados.get("p1", "")
p2 = dados.get("p2", "")
print(f"Aguardando jogadores na sala {sala}... Jogador 1: {p1} | Jogador 2: {p2}\n")

timeout = 60  
start_time = time.time()
while not (p1 and p2):
    
    if time.time() - start_time > timeout:
        print(f"Ainda aguardando jogadores na sala {sala}... Jogador 1: {p1 or '<vazio>'} | Jogador 2: {p2 or '<vazio>'}\n")
        start_time = time.time()
    time.sleep(1)
    dados = r.hgetall(key)
    p1 = dados.get("p1", "")
    p2 = dados.get("p2", "")
print("Ambos os jogadores estão presentes. Iniciando o jogo...")





