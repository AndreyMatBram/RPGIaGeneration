
def evolution(iastts:list, plystts:list,levelCap:int):


    if sum(iastts) <= levelCap:
        b = True
    else:
        b = False
        a = -1
        return a,b

    plyHealth, iaHealth = 100, 100

     # detectar qual atributo defensivo é menor para ent determinar o modo de ataque
    
    fisico = iastts[0]-plystts[2]
    magico = iastts[1]-plystts[3]
    if fisico > magico:
        mainAttkIa = fisico
    else:
        mainAttkIa = magico
    
    fisico = plystts[0]-iastts[2]
    magico = plystts[1]-iastts[3]
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


    [print (i,"| ", end='') for i in battleOrd]


    round = 0
    winner = "none"
    while winner == "none":
        print("\n==========================================\nRound: ",round+1,"\n")

        if battleOrd[round] == 1:
            print("Player Ataca!\n -",mainAttkPly)
            iaHealth = iaHealth - mainAttkPly
            print("IA: ",iaHealth,"/100")
        elif battleOrd[round] == 0:
            print("Ia Ataca!\n -",mainAttkIa)
            plyHealth = plyHealth - mainAttkIa
            print("Player: ",plyHealth,"/100")

        round += 1
        if round == 100:
            round = 0
        
        if plyHealth <= 0:
            winner = "IA"
        elif iaHealth <= 0:
            winner = "player"
        
     
    print ("\n",winner,"VENCEU!!!!!")

    if winner == "player":
        a = plyHealth
    elif winner == "IA":
        a = 0

        

    return a,b
def main():
    s1= [2,5,10,2,6] # Fisico, Magico, Def Fisico, Def Magico, Agi
    s2= [1,1,1,1,1]
    max = 20
    evolution(s1,s2,max+5)

if __name__ == "__main__":
    main()
