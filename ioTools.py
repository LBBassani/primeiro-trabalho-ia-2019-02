
import json
# Leitura de parametros
class ParamFileReader(object):
    def __init__(self, file):
        self.__f = file
    
    def read(self):
        with open(self.__f, "r") as f:
            params = {}
            line = f.readline()
            while line:
                if line.find("beginParam") >= 0:
                    metodo = f.readline().rstrip()
                    params[metodo] = {}
                    line = f.readline()
                    while line.find("endParam") < 0:
                        words = line.split()
                        param = words.pop(0)
                        params[metodo][param] = list()
                        tipo = words.pop(0)
                        tipo = list if tipo == "list" else int if tipo == "int" else float
                        for w in words:
                            params[metodo][param].append(tipo(w))
                        line = f.readline()
                line = f.readline()
            return params

# Escrita de resultados
class resultadosFileWriter(object):
    def __init__(self, file):
        self.__f = file

    def write(self, resultados):
        with open(self.__f, "w+") as f:
            f.write(json.dumps(resultados))

# Leitura de Resultados
class resultadosFileReader(object):
    def __init__(self, file):
        self.__f = file
    
    def read(self):
        with open(self.__f, "r") as f:
            return json.load(f)