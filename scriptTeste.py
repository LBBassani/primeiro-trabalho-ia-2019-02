from ioTools import resultadosFileReader, resultadosFileWriter
from Busca.ProblemasBusca.mochila import mochila
from Busca.AlgoritmosBusca.hillClimbing import hillClimbing
from Busca.AlgoritmosBusca.beamSearch import beamSearch
from Busca.AlgoritmosBusca.simulatedAnnealing import simulatedAnnealing
from Busca.AlgoritmosBusca.genetico import algoritmoGenetico
from Busca.AlgoritmosBusca.grasp import grasp
from problemas import problemasTeste
import trabalhoIA

# Leitura dos Resultados do Treinamento
resultadosTreinamentos = { }

graspReader = resultadosFileReader("resultadoTreinamentoGRASP.result")
resultadosTreinamentos["GRASP"] = graspReader.read()

simulatedAnnealingReader = resultadosFileReader("resultadoTreinamentoSimulated Annealing.result")
resultadosTreinamentos["Simulated Annealing"] = simulatedAnnealingReader.read()

beamSearchReader = resultadosFileReader("resultadoTreinamentoBeam Search.result")
resultadosTreinamentos["Beam Search"] = beamSearchReader.read()

geneticoReader = resultadosFileReader("resultadoTreinamentoAlgoritmo Genetico.result")
resultadosTreinamentos["Algoritmo Genetico"] = geneticoReader.read()

# resultados dos testes
resultadosTestes = {
    "Hill Climbing" : trabalhoIA.teste(problemasTeste, hillClimbing),
    "Beam Search" : trabalhoIA.teste(problemasTeste, beamSearch, **resultadosTreinamentos["Beam Search"][0][1]),
    "Simulated Annealing" : trabalhoIA.teste(problemasTeste, simulatedAnnealing, **resultadosTreinamentos["Simulated Annealing"][0][1]),
    "GRASP" : trabalhoIA.teste(problemasTeste, grasp, **resultadosTreinamentos["GRASP"][0][1]),
    "Algoritmo Genetico" : trabalhoIA.teste(problemasTeste, algoritmoGenetico, **resultadosTreinamentos["Algoritmo Genetico"][0][1])
}

# Realização dos Testes e escrita nos arquivos
for key, value in resultadosTestes.items():
    resultado = value.realizaTeste()
    nomeArq = "Resultados/resultadoFinal" + key + ".result"
    writer = resultadosFileWriter(nomeArq)
    writer.write(resultado)
