#Checkagem de cenários possíveis
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

#Função que  calcula o IMC recebido do input e do Teste de cenários
def CalculaIMC(altura, peso):
    #IMC = Peso / Altura²
    imc = float(peso / (altura * altura))
    imc_formatado = round(imc, 2)
    
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
        CalculaIMC(scenariosdict[scenario]["Altura"], scenariosdict[scenario]["Peso"])

def main():
    print("==================================")
    print("App Calculo de IMC")

    # Obter peso do usuário (com validação)
    peso = None
    while peso is None:
        peso_input = input("Insira seu peso (em kg): ")
        if peso_input.isdigit():
            peso = float(peso_input)
        else:
            print("Por favor, insira um valor numérico para o peso.")
    
    # Obter altura do usuário (com validação)
    altura = None
    while altura is None:
        altura_input = input("insira sua altura em metros: ")
        if '.' in altura_input and all([c.isdigit() or c == '.' for c in altura_input]):
                altura = float(altura_input)
        else:
                print("Insira um valor de altura válido (Ex: 1,80 ou 1.10): ")

    CalculaIMC(altura, peso)


SanityCheck()
main()