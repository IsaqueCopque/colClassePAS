# Algoritmo de coloração de grafos para o problema de alocação de Salas
 Isaque Copque e Caio Pontes

 ---

 ## Descrição

 Este projeto foi desenvolvido como atividade da disciplina Teoria Dos Grafos - MATA53 ministrada pelo professor Roberto Parente.
 O problema de alocação de salas (PAS) consistem em alocar salas de aulas para um conjunto de horários de aulas e turmas pré-estabelecidos. Foram desenvolvidos dois códigos para a resolução do PAS: pas.py e pas2.py. O primeiro implementa uma solução proposta em Silva [1] que utiliza coloração própria de grafos, enquanto o segundo foi construído utilizando uma abordagem de força bruta para comparar com os resultados do primeiro.

## Requisitos

É necessário ter o [Python3](https://www.python.org/downloads/) instalado para executar o código. São utilizadas as bibliotecas *networkx*, *matplotlib* e *pandas*, que podem ser facilmente instaladas utilizando o instalador de pacotes [pip](https://pypi.org/project/pip/) com os comandos:

``` bash
pip install networkx
pip install matplotlib
pip install pandas
```

## Execução

Para executar os códigos execute os comandos

``` bash
python pas2.py
```
e
``` bash
python pas.py
```

Os dados de entrada podem ser passados manualmente na execução do programa ou com um arquivo de entrada. Para executar os códigos com os arquivos de teste como entrada, execute os comandos

``` bash
python pas2.py < teste.txt
```
e
``` bash
python pas.py < teste.txt
```

onde teste.txt é o arquivo que contém as entradas. Para criar arquivos de teste, a entrada deve seguir o seguinte padrão: A quantidade de turmas, a quantidade de horarios de uma turma i, os horários da turma i, o tamanho da turma i, a quantidade de salas1 e a capacidade da sala j.

 ---

 [1]: D. J. Silva, G. C. Silva, Heurísticas baseadas no algoritmo de coloração
de grafos para o problema de alocação de salas em uma instituição de
ensino superior, Anais do XLII SBPO (2010) 2839–2849.