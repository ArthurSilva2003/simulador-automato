# Simulador de Autômatos Finitos

Este projeto é um simulador de autômatos finitos (DFA, NFA e com transições vazias) que funciona via linha de comando. Ele lê um autômato definido em um arquivo `.aut` (JSON), processa cadeias de entrada listadas em um arquivo `.in` (CSV), e salva os resultados em um arquivo `.out`.

## Como funciona

Você fornece:
- Um arquivo JSON com a definição do autômato.
- Um arquivo CSV com as palavras a serem testadas e seus resultados esperados (1 para aceita, 0 para rejeita).

O programa analisa cada palavra, simula o comportamento do autômato e informa se ela foi aceita ou não, junto do tempo de processamento.

### Exemplo de uso:
```bash
python simulador.py automato.aut testes.in saida.out
```

### Exemplo de entrada `.aut` (JSON):
```json
{
  "initial": 0,
  "final": [1],
  "transitions": [
    {"from": 0, "read": "a", "to": 1},
    {"from": 1, "read": "b", "to": 0}
  ]
}
```

### Exemplo de entrada `.in` (CSV):
```
a;1
ab;0
abab;1
```

### Exemplo de saída `.out`:
```
a;1;1;0.002
ab;0;0;0.001
abab;1;1;0.003
```

## Requisitos
- Python 3

## Sobre
Este projeto foi feito como trabalho acadêmico para simular autômatos finitos com base em arquivos de entrada, sem uso de interface gráfica. A ideia é facilitar a validação automática de cadeias por autômatos definidos externamente.

---
Autor: [Seu Nome Aqui]