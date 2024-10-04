
# from pygame import time


def evolution(iastts:list, plystts:list,levelCap:int):


    if sum(iastts) > levelCap:
        a = -1
        # print("Pontuação: ",a,"\nValidade: ",b)
        return a
    
    for i in range(5):
        if iastts[i] < 1:
            a = -1
            return a
        iastts[i] = int(iastts[i])
        
    

    plyHealth, iaHealth = 100, 100

    # detectar qual atributo defensivo é menor para ent determinar o modo de ataque

    # 0 = fisico, 1 = magico, 2 = def fisico, 3 = def magico, 4 = agi
    # fisico * (0.5 * (f/d)) = dano fisico
    
    #IA
    fisico = (iastts[0]) * (0.5 * (iastts[0]/plystts[2]))
    magico = (iastts[1]) * (0.5 * (iastts[1]/plystts[3]))
    if fisico > magico:
        mainAttkIa = fisico
    else:
        mainAttkIa = magico
    
    #Player
    fisico = (plystts[0]) * (0.5 * (plystts[0]/iastts[2]))
    magico = (plystts[1]) * (0.5 * (plystts[1]/iastts[3]))
    if fisico > magico:
        mainAttkPly = fisico
    else:
        mainAttkPly = magico
    speedOrd= plystts[4]/iastts[4] 

    battleOrd = []

    countBattle = 0
    orderAux = speedOrd
    while countBattle < 100 :
        
        if orderAux >= 1:
            battleOrd.append(1)
            orderAux -= 1
        else:
            battleOrd.append(0)
            orderAux += speedOrd
        countBattle += 1


    # [print (i,"| ", end='') for i in battleOrd]


    round = 0
    winner = "none"
    while winner == "none":
        # print("\n==========================================\nRound: ",round+1,"\n")

        if battleOrd[round] == 1:
            # print("Player Ataca!\n -",mainAttkPly)
            iaHealth = iaHealth - mainAttkPly
            # print("IA: ",iaHealth,"/100")
        elif battleOrd[round] == 0:
            # print("Ia Ataca!\n -",mainAttkIa)
            plyHealth = plyHealth - mainAttkIa
            #print("Player: ",plyHealth,"/100")

        round += 1
        if round == 100:
            break
        
        if plyHealth <= 0:
            winner = "IA"
        elif iaHealth <= 0:
            winner = "player"
        # time.delay(500)
     
    #print ("\n",winner,"VENCEU!!!!!")

    if winner == "player":
        a = 0
    elif winner == "IA":
        a = iaHealth
    elif round == 100:
        a = -1

        
    #print("Pontuação: ",a ,"\nValidade: ",b)
    
    # Evitamos Batalhas perfeitas buscando não obter resultados com distribuiçoes muito desiguais 
    if a == 100:
        a = -1


    return a

