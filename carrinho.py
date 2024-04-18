class Carro:
    def __init__(self,marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0
    
    def acelerar(self):
        self.velocidade += 10
        print(f"Velocidade atual {self.velocidade}Km/h")
    
    def frear(self):
        self.velocidade -= 10
        print(f"Velocidade atual {self.velocidade}Km/h")
    
    def exibir_info(self):
        print(f"Marca:{self.marca}\nModelo:{self.modelo}\nCor:{self.cor}")
    
lista = []

while True:
    print("\n---MENU---")
    print("1.Para criar um carro")
    print("2. Para acessar a lista de carros")
    print("3. Para acelerar um carro")
    print("4. Para frear um carro")
    print("5. Para sair")
     
    opcao = input("\nSelecione a sua opção:")
    
    if opcao == "1":
        marca = input("Digite a marca do carro:")
        modelo = input("Digite o modelo do carro:")
        cor = input("Digite a cor do carro:")
        carro_novo = Carro(marca, modelo, cor)
        lista.append(carro_novo)
        print("Carro adicionado com sucesso!")


    elif opcao == "2":
        if lista:
            for carro in lista:
                carro.exibir_info()
        else:
            print("Nenhum carro adicionado ainda")


    elif opcao =="3":
         marca = input("Digite a marca do carro: ")
         modelo = input("Digite o modelo do carro: ")
         cor = input("Digite a cor do carro: ")
         for carro in lista:
             if carro.modelo == modelo and carro.marca == marca and cor == carro.cor:
                 carro.acelerar()
                 break
    elif opcao == "4":
        modelo = input("Digite o modelo do carro:")
        for carro in lista:
            if carro.modelo == modelo:
                if carro.velocidade>0:
                    carro.frear()
                    break
                else:
                    print("O está parado!!!!")
    elif opcao == "5":
        print("finalizando")
        break
