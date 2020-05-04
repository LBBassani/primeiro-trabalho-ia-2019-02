# Algoritmos de Busca
Este trabalho é dedicado a algoritmos de busca estudados em Inteligência Artificial. Alguns algoritmos foram implementados com finalidade de estudos para a primeira prova e alguns para o primeiro trabalho prático da matéria de Inteligência Artificial no semestre de 2019/02, pela Aluna Lorena Bassani do curso de Ciência da Computação da Universidade Federal do Espírito Santo - UFES.

## Primeiro Trabalho de IA
O primeiro trabalho prático de Inteligência Artificial se dedica a encontrar hiperparâmetros e testar cinco métodos de busca aplicados ao problema da mochila. Abaixo estão listados os métodos implementados para o trabalho e as classes de Teste e Treinamento:

### Classe de Treinamento
#### Atributos :
**problemas**   : Dicionário de problemas a serem utilizados para o treinamento do método<br>
**metodo**      : Método a ser treinado<br>
**parametros**  : dicionário com listas de parâmetros a serem testados<br>
**respostaProblema** : objeto contendo as respostas por problema do treinamento após realizado (não existe antes de treinar)<br>
**respostaParametros** : objeto contendo as respostas por parametro do treinamento após realizado (não existe antes de normalizar os resultados)<br>
**respostaProblemaNormal** : objeto contendo as respostas normalizadas por problema do treinamento após realizado (não existe antes de normalizar os resultados)
#### Métodos :
##### realizaTreino
**Descrição** : Método de treinamento de algoritmos que, com base nos parametros passados na construção da classe, realiza uma busca em grade dos parametros com melhor
desempenho nos casos de treinamento.<br>
**Parametros** : Sim<br>
- tempo    : tempo limite de execução de cada tentativa de rodar um problema.<br>

**Retorno**    : Não<br>
**Lança exceções** : Sim<br>
- IProblema.TimedOutExec  : Exceção de tempo limite
- NotImplementedError     : Erro de método não implementado por subclasse de IProblema

### Classe de Teste
#### Atributos :
**problemas**   : Dicionário de problemas a serem utilizados para o teste do método<br>
**metodo** : Método a ser testado<br>
**parametros**  : dicionário com listas de parâmetros a serem testados<br>
**resposta**    : objeto contendo as respostas do teste após realizado (None antes de testar)

#### Métodos :
##### realizaTreino
**Descrição** : Método de teste de algoritmos que, com base nos parametros passados 
na construção da classe, avalia o desempenho do método nos casos de teste.<br>
**Parametros** : Sim<br>
- tempo    : tempo limite de execução de cada tentativa de rodar um problema

**Retorno**    : Não<br>
**Lança exceções** : Sim<br>
- IProblema.TimedOutExec  : Exceção de tempo limite
- NotImplementedError     : Erro de método não implementado por subclasse de IProblema


### Hill Climbing
**Classe** : Baseada em Soluções Parciais<br>
**Descrição** : Procedimento de Estratégia Gulosa que procura construir a solução escolhendo sempre o melhor próximo estado, sem *backtracking*.<br>
**Necessita de Estado Inicial** : Não<br>
**Hiperparametros** : Não tem

### Beam Search
**Classe** : Baseada em Soluções Parciais<br>
**Descrição** : Algoritmo de Busca em amplitude, onde ao invés de utilizar apenas o melhor próximo estado, estuda as possibilidades de vários próximos estados expandindo-os. O número de estados estudados é passado como parâmetro.<br>
**Necessita de Estado Inicial** : Não<br>
**Hiperparametros** : 
* nEstados : número de estados mantidos na expansão

### Simulated Annealing
**Classe** : Baseada em Soluções Completas -> Busca Local <br>
**Descrição** : Baseado em processo físico de resfriamento de sólido superaquecido, onde durante o resfriamento podem ocorrer algumas etapas de medição de aquecimento, representado no algoritmo por uma chance de aceitar um estado pior que o atual. Quanto menor a "temperatura" menos o fenomeno de reaquecimento ocorre, ou seja, menor a chance de aceitarmos estados piores.<br>
**Necessita de Estado Inicial** : Sim<br>
**Hiperparametros** :
* t : temperatura inicial
* a : taxa de queda de temperatura
* minT : temperatura mínima (critério de parada)
* numIter : quantidade de iterações por temperatura

### GRASP - Greedy Randomized Adaptive Search
**Classe** : Baseada em Soluções Completas -> Busca Local<br>
**Descrição** : É um método iterativo probabilístico, onde cada iteração obtém uma solução independente do problema em estudo e é composta de duas fases:
1. *Fase Construtiva* : Determina uma solução a partir de uma função gulosa probabilística
2. *Fase de Busca Local* : Submeter a solução a um outro algoritmo de busca local.

**Necessita de Estado Inicial** : Não<br>
**Hiperparametros** : 
* m : elementos para escolher no construtor guloso de estados
numIter : número de iterações total do algoritmo (critério de parada)

### Algoritmo Genético
**Classe** : Baseada em Soluções Completas -> Busca Populacional -> Computação Evolutiva<br>
**Descrição** : Algoritmo evolutivo baseado na teoria de seleção natural e hereditariedade, que trabalha em cima do conceito de gerações de uma população. Cada geração é composta por descendentes da geração anterior (recombinações ou mutações desses individuos) e são selecionados para continuar os melhores descendentes, com chances de alguns descendentes piores serem escolhidos no lugar de alguns melhores por fator aleatório.<br>
**Necessita de Estado Inicial** : Não<br>
**Hiperparametros** : 
* maxIter : número máximo de iterações (critério de parada)
* tamanhoPop : tamanho da população
* maxSemMelhora : número máximo de iterações sem melhora de resposta (critério de parada)
* chanceCross : chance de ocorrer crossover
* chanceMutacao : chance de ocorrer mutação

## Primeira Prova de IA
Além dos algoritmos do primeiro trabalho, a primeira prova de Inteligência Artifical de 2019/02 do curso de Ciência da Computação da UFES cobre os seguintes algoritmos listados abaixo.

### Branch And Bound
**Classe** : Baseada em Soluções Parciais<br>
**Descrição** : Algoritmo que, baseado em uma solução previamente conhecida (estado inicial) apenas explora as expansões com chances de gerar resultados melhores que ela. Ao achar uma expansão parcial ainda melhor que o melhor estado atualmente conhecido, pode trocar o estado de referencia para poda.<br>
Esse algoritmo conta com uma função heurística que realiza uma estimativa do melhor resultado que pode ocorrer em um ramo de expansão. Essa função pode ser:
* otimista : sempre prevê uma aptidão melhor ou igual a que é na realidade.
* não otimista : pode prever aptidões piores que a realidade, podando o ramo onde estaria uma solução ótima, mas torna o procedimento mais rápido.

Costuma ser muito complexo gerar funções otimistas para a maioria dos problemas.<br>
**Necessita de Estado Inicial** : Sim <br>
**Hiperparametros** :
* otimista : Define se a função heurística é otimista ou não


### Tabu Search
**Classe** : Baseada em Soluções Completas -> Busca Local<br>
**Descrição** : Algoritmo de busca local baseado em soluções completas onde movimentos para soluções piores é permitido, de forma que vizinhos dessa soluções possam ser alcançados mais tarde. O algoritmo evita ciclos de busca a partir da lista tabu, onde guarda os estados já vizitados.<br>
**Necessita de Estado Inicial** : Sim<br>
**Hiperparametros** : 
* numIter : numéro de iterações do algoritmo (critério de parada)
