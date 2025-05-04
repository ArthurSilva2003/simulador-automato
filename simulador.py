import json
import csv
import time
import sys
from typing import List, Dict, Optional

class Automato:
    def __init__(self, arquivo_json):
        with open(arquivo_json, 'r') as f:
            dados = json.load(f)

        self.estado_inicial = dados['initial']
        self.estados_finais = set(dados['final'])
        self.transicoes = {}

        for transicao in dados['transitions']:
            origem = transicao['from']
            simbolo = transicao['read']
            destino = transicao['to']
            chave = (origem, simbolo)
            if chave not in self.transicoes:
                self.transicoes[chave] = []
            self.transicoes[chave].append(destino)

    def epsilon_closure(self, estados):
        stack = list(estados)
        closure = set(estados)
        while stack:
            estado = stack.pop()
            for proximo in self.transicoes.get((estado, None), []):
                if proximo not in closure:
                    closure.add(proximo)
                    stack.append(proximo)
        return closure

    def mover(self, estados, simbolo):
        destino = set()
        for estado in estados:
            for proximo in self.transicoes.get((estado, simbolo), []):
                destino.add(proximo)
        return destino

    def aceita(self, cadeia):
        estados_atuais = self.epsilon_closure({self.estado_inicial})
        for simbolo in cadeia:
            estados_atuais = self.epsilon_closure(self.mover(estados_atuais, simbolo))
        return any(estado in self.estados_finais for estado in estados_atuais)


def processar_testes(arquivo_automato, arquivo_entrada, arquivo_saida):
    automato = Automato(arquivo_automato)
    with open(arquivo_entrada, 'r') as f:
        linhas = csv.reader(f, delimiter=';')
        testes = [(linha[0], int(linha[1])) for linha in linhas if linha]

    with open(arquivo_saida, 'w', newline='') as f:
        escritor = csv.writer(f, delimiter=';')
        for palavra, esperado in testes:
            inicio = time.time()
            resultado = 1 if automato.aceita(palavra) else 0
            tempo = round(time.time() - inicio, 3)
            escritor.writerow([palavra, esperado, resultado, tempo])


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Uso: python simulador.py arquivo.automato arquivo.entrada arquivo.saida")
        sys.exit(1)
    processar_testes(sys.argv[1], sys.argv[2], sys.argv[3])