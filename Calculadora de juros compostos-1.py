#!/usr/bin/env python
# coding: utf-8

# In[15]:


import matplotlib.pyplot as plt #Trabalhar com gráficos


# In[16]:


continuar = "s"
while continuar == "s":
    Lista_de_valores = [] #Valores no tempo
    Tempo = [] #Tempo
    VP = float(input("Valor presente:")) #Valor presente
    menu = str(input("Escolha uma opção:\n1 - mensal\n2 - anual\n")) #Escolha do usuário(mensal/anual)
    while menu !=  "1" and menu != "2": #Contrapartida ao erro do usário
        menu = str(input("Escolha uma das opções:\n1 - mensal\n2 - anual\n"))
    if menu == "1": #mensal
        periodo_mensal = int(input("Quantos meses: "))
        r_mensal = float(input("Taxa de juros (mensal): "))
        aporte_mensal = float(input("Aporte mensal: "))
        #Cálculo do valor final com aporte mensal em juros compostos
        VF_mensal = VP * ((1 + (r_mensal / 100)) ** periodo_mensal) +                 aporte_mensal * (((1 + (r_mensal / 100)) ** periodo_mensal - 1) / (r_mensal / 100))    
        print(f"Valor final: R${round(VF_mensal, 2)}")
        #Cálculo mês a mês
        V_mensal = VP
        for tempo in range(1, periodo_mensal+1):
            V_mensal = V_mensal*(1+(r_mensal/100))
            V_mensal = V_mensal + aporte_mensal
            Lista_de_valores.append(round(V_mensal, 2))
            Tempo.append(tempo)   
        #plot do gráfico    
        plt.figure()
        plt.plot(Tempo, Lista_de_valores, marker = "o", linestyle = "-", 
                 color = "g", label="Evolução do investimento")
        plt.xlabel("Meses")
        plt.ylabel("Valor acumulado (R$)")
        plt.title("Crescimento do Investimento (mensal)")
        plt.legend()
        plt.show()
    elif menu == "2": #Opção anual
        periodo_anual = int(input("Quantos anos: "))
        r_anual = float(input("Taxa de juros (anual): "))
        aporte_mensal = float(input("Aporte mensal: "))
        #Cálculo do valor final na opção anual
        VF_anual = VP * ((1 + (r_anual / (12 * 100))) ** (periodo_anual * 12)) +            aporte_mensal * (((1 + (r_anual / (12 * 100))) ** (periodo_anual * 12) - 1) / (r_anual / (12 * 100)))
        print(f"Valor final: R${round(VF_anual, 2)}")
        #Cálculo mês a mês
        V_mensal = VP
        for tempo in range(1, (periodo_anual*12)+1):
            V_mensal = V_mensal*(1+(r_anual/(12*100)))
            V_mensal = V_mensal + aporte_mensal
            Lista_de_valores.append(round(V_mensal, 2))
            Tempo.append(tempo)
        #Plot do gráfico (Matplotlib as plt)    
        plt.figure()
        plt.plot(Tempo, Lista_de_valores, marker = "o", linestyle = "-", 
                 color = "g", label="Evolução do investimento")
        plt.xlabel("Meses")
        plt.ylabel("Valor acumulado (R$)")
        plt.title("Crescimento do Investimento (mensal)")
        plt.legend()
        plt.show()
    #Interação com o usuário    
    continuar = str(input("Deseja continuar (s/n)? ")).lower()
    while continuar != "s" and continuar != "n":
        continuar = str(input("Digite (s/n): ")).lower()
print("Calculadora encerrada.")    

