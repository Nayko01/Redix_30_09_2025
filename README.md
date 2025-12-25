# Pedra, Papel e Tesoura (PPP) - Multiplayer com Redis

Este projeto é uma implementação em Python do clássico jogo **Pedra, Papel e Tesoura**, projetado para ser jogado de forma distribuída entre dois terminais. A comunicação e o estado do jogo são gerenciados em tempo real utilizando um servidor **Redis**.

---

## 🚀 Funcionalidades

* **Multijogador Distribuído**: Dois jogadores podem interagir de instâncias diferentes.
* **Sincronização via Redis**: Gerenciamento de salas, presença de jogadores e jogadas através de hashes do Redis.
* **Sistema de Salas**: O Jogador 1 gera um código de sala único para que o Jogador 2 possa se conectar.
* **Limpeza Automática**: Remoção automática dos dados da sala após o término da partida ou via expiração (TTL).

---

## 📋 Pré-requisitos

Para rodar este projeto, você precisará de:

1.  **Python 3.x** instalado.
2.  **Servidor Redis** ativo (local ou remoto).
3.  **Biblioteca `redis`** para Python:
    ```bash
    pip install redis
    ```

---

## 🛠️ Configuração e Execução

### 1. Preparar o Servidor
Certifique-se de que o Redis está rodando no `localhost` na porta `6379`. Caso seu servidor esteja em outro endereço, altere a linha de conexão no arquivo `PPP.py`:
```python
r = redis.Redis(host='seu_ip', port=6379, decode_responses=True)
