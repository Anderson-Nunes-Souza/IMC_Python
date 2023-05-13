#Checkagem de Cenarios possíveis
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
        "Peso": 80
    },
    "Obesidade": {
        "Altura": 1.70,
        "Peso": 110
    }
}
print(type(scenariosdict))

def CalculaIMC(scenario,altura, peso):
    altura = float(scenariosdict[scenario]["Altura"])
    peso = float(scenariosdict[scenario]["Peso"])
    #IMC = Peso / Altura²
    imc = float(peso / (altura * altura))
    imc_formatado = float("{:.2f}".format(imc))
    
    #Magreza, quando o resultado é menor que 18,5 kg/m2;
    if imc_formatado < 18.5:
            print("Imc de: ")
            print(imc_formatado)
            print("Magreza")
    # Normal, quando o resultado está entre 18,5 e 24,9 kg/m2;
    if imc_formatado >=18.5 and imc_formatado <=24.9:
            print("Imc de: ")
            print(imc_formatado)
            print("Normal")
    # Sobrepeso, quando o resultado está entre 24,9 e 30 kg/m2;
    if imc_formatado >24.9 and imc_formatado <= 30:
            print("Imc de: ")
            print(imc_formatado)
            print("Sobrepeso")
    # Obesidade, quando o resultado é maior que 30 kg/m2;
    if imc_formatado >30:
            print("Imc de: ")
            print(imc_formatado)
            print("Obesidade")


#Função de checkagem de scenarios possíveis
def SanityCheck():
    for scenario in scenariosdict:
        CalculaIMC(scenario, scenariosdict[scenario]["Altura"], scenariosdict[scenario]["Peso"])

def main():
    print("==================================")
    print("App Calculo de IMC")
    print("insira seu peso:")
    peso =  float(input())
    print("insira sua altura:")
    altura = float(input())
    #Continuar daqui 
    scenariosdict["Input_usuario"]["Altura"] = altura
    scenariosdict["Input_usuario"]["Peso"] = peso 
    #CalculaIMC(scenariosdict[scenario]["Altura"], scenariosdict[scenario]["Peso"])
    print(scenariosdict)


SanityCheck()
main()