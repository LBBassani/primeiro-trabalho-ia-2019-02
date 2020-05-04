""" Problemas de teste e treinamento 
para o primeiro trabalho prático de IA 
"""
from Busca.ProblemasBusca import IProblema
from sklearn.model_selection import ParameterGrid
from queue import PriorityQueue
import pandas as pd


""" Classe de Treinameto
        Atributos :
            problemas   : Dicionário de problemas a serem utilizados para o treinamento do método
            metodo      : Método a ser treinado
            parametros  : dicionário com listas de parâmetros a serem testados
            respostaProblema : objeto contendo as respostas por problema do treinamento após realizado (não existe antes de treinar)
            respostaParametros : objeto contendo as respostas por parametro do treinamento após realizado (não existe antes de normalizar os resultados)
            respostaProblemaNormal : objeto contendo as respostas normalizadas por problema do treinamento após realizado (não existe antes de normalizar os resultados)

        Métodos :
            realizaTreino
                Descrição : Método de treinamento de algoritmos que, com base nos parametros passados 
                            na construção da classe, realiza uma busca em grade dos parametros com melhor
                            desempenho nos casos de treinamento.
                Parametros : Sim
                    tempo    : tempo limite de execução de cada tentativa de rodar um problema
                Retorno    : Sim
                    melhoresParametros : Tupla no formato (melhor média, melhores parametros)
                    respostaProblema : Respostas obetidas nos problemas, juntamente com os parâmetros usados
                    temposAlcancados : Lista com todos os tempos alcançados durante o treinamento
                Lança exceções : Sim
                    IProblema.TimedOutExec  : Exceção de tempo limite
                    NotImplementedError     : Erro de método não implementado por subclasse de IProblema
"""
class treinamento:

    def __init__(self, problemas, metodo, **keyargs ):
        self.problemas = problemas
        self.metodo = metodo
        self.parametros = ParameterGrid(keyargs)
    
    
    def realizaTreino(self, tempoLimite = 2):
        tempo = list()
        timeout = tempoLimite # Tempo de timeout default de 2 minutos
        
        """ Rodar os testes 
                Como :  Para cada problema a ser usado para treino roda o algoritmo
                            para cada combinação de parametros vindos da grid de parametros.
                        Guarda o resultado de tempo, resposta e lista de parametros
        """
        self.respostaProblema = list()
        for nome, p in self.problemas.items():
            resultados = list()
            for paramList in self.parametros:
                # prepara as variáveis para o problema
                terminou = True
                estado = p.estadoNulo()
                tempo.clear()
                tempo.append(timeout)
                # Realiza a busca
                try:
                    p.busca(estado, self.metodo, tempo, **paramList)
                except IProblema.TimedOutExc:
                    # Se veio com timeout, muda a flag de termino para False
                    terminou = False
                # Formata a resposta
                resp = {"Tempo" : tempo[0], "Resposta" : [estado.copy(), p.aptidao(estado)], "Parametros" : paramList, "Terminou" : terminou}
                resultados.append(resp)
            resp = {"Problema" : (nome, p.descricao()), "Resultados" : resultados}
            self.respostaProblema.append(resp)
        self.resultadosNormalizados()
        self.resultadosPorParametros()
        return (self.melhoresParametros(), self.respostaProblema, self.temposAlcancados(), self.dezMelhores, self.respostaProblemaNormal)

    def resultadosPorParametros(self):
        """ Montar os resultados por parametros """
        self.respostaParametros = list()
        for param in self.parametros:
            lista = list()
            for resposta in self.respostaProblemaNormal:
                resposta = resposta["Resultados"]
                resposta = list(filter(lambda x: x["Parametros"] == param, resposta))
                lista.append(resposta[0]["Resposta"])
            self.respostaParametros.append({"Parametros" : param, "Resultados" : lista})

    def resultadosNormalizados(self):
        """ Normalizar os resultados por problema do conjunto de treino """
        self.respostaProblemaNormal = self.respostaProblema.copy()
        mini, maxi = self.minMaxValueResultadosPorProblema()
        divisor = maxi - mini
        for r in self.respostaProblemaNormal:
            resultados = r["Resultados"]
            for resultado in resultados:
                resp = resultado["Resposta"]
                resp[1] = (resp[1] - mini)/divisor

    def mediaResultadosPorParametros(self, p):
        aux = p["Resultados"]
        aux = list(map(lambda x: x[1], aux))
        media = sum(aux)
        media = media/(len(p["Resultados"]))
        return media
    
    def minMaxValueResultadosPorProblema(self):
        aux = self.aptidoesResultados()
        return (min(aux), max(aux))

    def aptidoesResultados(self):
        aux = list(map(lambda x: x["Resultados"], self.respostaProblema))
        aux = [item for sublist in aux for item in sublist]
        aux = list(map(lambda x : x["Resposta"], aux))
        aux = list(map(lambda x: x[1], aux))
        return aux

    def melhoresParametros(self):
        """ Encontrar o melhor resultado """
        dezMelhores = PriorityQueue(10)
        melhorMedia = 0
        melhorParam = None
        for p in self.respostaParametros:
            m = self.mediaResultadosPorParametros(p)
            if dezMelhores.full():
                mold, pold = dezMelhores.get()
                if m < mold:
                    dezMelhores.put((mold, pold))
                else:
                    dezMelhores.put((m, p))
            else:
                dezMelhores.put((m, p))
            if m > melhorMedia:
                melhorMedia = m
                melhorParam = p
        self.dezMelhores = list()
        for _ in range(0, 10):
            if dezMelhores.empty():
                break
            self.dezMelhores.append(dezMelhores.get()[1])
        return (melhorMedia, melhorParam["Parametros"])

    def temposAlcancados(self):
        """ Retornar os tempos """
        tempos = list()
        for resp in self.respostaProblema:
            resultado = resp["Resultados"]
            for r in resultado:
                tempo = r["Tempo"]
                tempos.append(tempo)
        return tempos

""" Classe de Teste
        Atributos :
            problemas   : Dicionário de problemas a serem utilizados para o teste do método
            metodo      : Método a ser testado
            parametros  : dicionário com listas de parâmetros a serem testados
            resposta    : objeto contendo as respostas do teste após realizado (none antes de testar)

        Métodos :
            realizaTreino
                Descrição : Método de teste de algoritmos que, com base nos parametros passados 
                            na construção da classe, avalia o desempenho do método nos casos de teste.
                Parametros : Sim
                    tempo    : tempo limite de execução de cada tentativa de rodar um problema
                Retorno    : Sim
                    resposta : Respostas alcançadas para cada problema
                    temposAlcançados : lista com os tempos de execução de cada problema
                Lança exceções : Sim
                    IProblema.TimedOutExec  : Exceção de tempo limite
                    NotImplementedError     : Erro de método não implementado por subclasse de IProblema
"""
class teste:

    def __init__(self, problemas, metodo, **keyargs):
        self.problemas = problemas
        self.metodo = metodo
        self.parametros = keyargs

    def realizaTeste(self, tempoLimite = 5):
        tempo = list()
        timeout = tempoLimite # Tempo de timeout default de 5 minutos

        self.resposta = list()
        for nome, p in self.problemas.items():
            terminou = True
            estado = p.estadoNulo()
            tempo.clear()
            tempo.append(timeout)

            try:
                p.busca(estado, self.metodo, tempo, **self.parametros)
            except IProblema.TimedOutExc:
                # Se veio com timeout, muda a flag de termino para False
                terminou = False
            # Formata a resposta
            resultado = {"Tempo" : tempo[0], "Resposta" : [estado.copy(), p.aptidao(estado)], "Terminou" : terminou}
            resp = {"Problema" : (nome, p.descricao()), "Resultados" : resultado}
            self.resposta.append(resp)
        return (self.resposta, self.temposAlcancados(), self.mediaDesvioExecucoes(), self.mediaDesvioTempos())

    def temposAlcancados(self):
        """ Retornar os tempos """
        tempos = list()
        for resp in self.resposta:
            resultado = resp["Resultados"]
            tempo = resultado["Tempo"]
            tempos.append(tempo)
        return tempos
    
    def mediaDesvioExecucoes(self):
        serie = list(map(lambda x: x["Resultados"]["Resposta"][1], self.resposta))
        serie = pd.Series(serie)
        return (serie.mean(), serie.std())

    def mediaDesvioTempos(self):
        serie = self.temposAlcancados()
        serie = pd.Series(serie)
        return (serie.mean(), serie.std())