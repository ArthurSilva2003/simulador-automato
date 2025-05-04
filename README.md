# Simulador de Autômatos Finitos

Este projeto é um simulador de autômatos finitos (DFA, NFA e com transições vazias) que funciona via linha de comando. Ele lê um autômato definido em um arquivo `.aut` (JSON), processa a entrada listadas em um arquivo `.in` (CSV), e mostra os resultados num arquivo `.out`.

Como Arquivo de Entrada tivemos:
a;1
ab;0
abab;1
baba;0


Que ao ser lido nos retorna o Arquivo Gerado:
a;1;1;0.0
ab;0;0;0.0
abab;1;1;0.0
baba;0;0;0.0
