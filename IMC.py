'''print("==================================")
print("App Calculo de IMC")
print("insira seu peso:")
peso =  float(input())
print("insira sua altura:")
altura = float(input())
'''
scenariosdict = {
    "Magreza" : {
        "Altura": 1.70,
        "Peso" : 50
    },
    "Normal":{
        "Altura": 1.70,
        "Peso": 70
    },
    "Sobrepeso": {
        "Altura": 1.70,
        "Peso": 90
    },
    "Obesidade": {
        "Altura": 1.70,
        "Peso": 110
    }
}

#print(scenariosdict["Magreza"]["Altura"])

def CalculaIMC(scenario,altura, peso):
    altura = float(scenariosdict[scenario]["Altura"])
    peso = float(scenariosdict[scenario]["Peso"])
    imc = float(peso / (altura * altura))
    imc_formatado = float("{:.2f}".format(imc))
    print(imc_formatado)
'''    if imc_formatado < 18:
        print("Imc de: " + imc_formatado)
        print("Magreza")
    if imc_formatado > 18.5 and imc_formatado < 24.9:
        print("Imc de: " + imc_formatado)
        print("Normal")
    print(imc_formatado)'''



def SanityCheck():
    for scenario in scenariosdict:
        CalculaIMC(scenario, scenariosdict[scenario]["Altura"], scenariosdict[scenario]["Peso"])

SanityCheck()


'''imc = scenariosdict["Peso"] / (scenariosdict["Altura"] * scenariosdict["Altura"])

imc_formatado = "{:.2f}".format(imc)

print(imc_formatado)'''



'''
Faça o cálculo de IMC conforme descrito abaixo (entregue no formato que lhe convier ... web, console, etc)

    Vamos construir um projeto simples, capaz de calcular o IMC (índice de massa corporal), de acordo com a seguinte especificação:
    IMC = Peso / Altura²

O resultado deve ser expresso, conforme os valores abaixo:
Magreza, quando o resultado é menor que 18,5 kg/m2;
Normal, quando o resultado está entre 18,5 e 24,9 kg/m2;
Sobrepeso, quando o resultado está entre 24,9 e 30 kg/m2;
Obesidade, quando o resultado é maior que 30 kg/m2;
Pode ser feita a entrega através do envio de arquivo zip contendo o projeto ou link do github.
'''