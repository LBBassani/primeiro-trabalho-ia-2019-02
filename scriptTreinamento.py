from ioTools import ParamFileReader, resultadosFileWriter
from Busca.ProblemasBusca.mochila import mochila
from Busca.AlgoritmosBusca.beamSearch import beamSearch
from Busca.AlgoritmosBusca.simulatedAnnealing import simulatedAnnealing
from Busca.AlgoritmosBusca.genetico import algoritmoGenetico
from Busca.AlgoritmosBusca.grasp import grasp
from problemas import problemasTreino
import trabalhoIA

# Leitura dos Parametros
paramFileReader = ParamFileReader("parametros.param")
parametros = paramFileReader.read()

# algoritmos a serem treinados
treinamentos = {
    "Algoritmo Genetico" : trabalhoIA.treinamento(problemasTreino, algoritmoGenetico, **parametros["Algoritmo Genetico"]),
    "GRASP" : trabalhoIA.treinamento(problemasTreino, grasp, **parametros["GRASP"]),
    "Simulated Annealing" : trabalhoIA.treinamento(problemasTreino, simulatedAnnealing, **parametros["Simulated Annealing"]),
    "Beam Search" : trabalhoIA.treinamento(problemasTreino, beamSearch, **parametros["Beam Search"])
}

# resultados dos treinamentos
resultadosTreinamentos = { }
for key, value in treinamentos.items():
    resultadosTreinamentos[key] = value.realizaTreino()
    nomeArq = "Resultados/resultadoTreinamento" + key + ".result"
    resulwriter = resultadosFileWriter(nomeArq)
    resulwriter.write(resultadosTreinamentos[key])
