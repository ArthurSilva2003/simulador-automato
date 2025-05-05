# Simulador de Autômato Finito

Este projeto é um simulador de autômato finito. Lê a definição de um autômato a partir de um arquivo `.json` e testa diversas cadeias fornecidas num arquivo `.in`, informando se foram aceitas ou rejeitadas.

---

##  Estrutura dos Arquivos

- `automato.json`: define o autômato (estado inicial, estados finais e transições).
- `testes.in`: lista as cadeias a serem testadas junto com o resultado esperado.
- `saida.out`: é gerado automaticamente com os resultados dos testes (incluindo tempo de execução).

---

##  Sua funcionalidade

O programa faz o seguinte:

1. Lê o estado inicial, estados finais e as transições.
2. Para cada cadeia, simula a leitura símbolo por símbolo.
3. No final, verifica se parou em um estado final:
    Se sim → cadeia **aceita**.
    Se não → cadeia **rejeitada**.
4. Compara com o resultado esperado e escreve no `saida.out`.

---

##  Exemplo de entrada (`testes.in`)
a;1
ab;0
abab;0
baba;0


Cada linha representa uma cadeia e o que se espera dela:
- `1` = aceita
- `0` = rejeitada

---

##  Exemplo de autômato (`automato.json`)

```json
{
  "initial": 0,
  "final": [1],
  "transitions": [
    { "from": 0, "read": "a", "to": 1 },
    { "from": 1, "read": "b", "to": 0 }
  ]
}

