import random

scoreA = 0
scoreB = 0

flag = False
for i in range(0,100000):
    bMoves = []
    flag = ""
    totalA = 0
    for j in range(0,20):
        

        if j == 0 or flag == "defect": #1 defect
            a = 0
        elif flag == "coop":
            if b == 1:
                a = 1
            else:
                a = 0
                flag = "defect"
        elif flag == "half":
            if j % 2 == 0:
                a = 1
            else:
                a = 0

        elif j == 1: #2 coop to coop, defect to defect
            if b == 0:
                a = 0
            else:
                a = 1

        elif j == 2: #CC/DD- defect, CD/DC- coop
            if bMoves[0] == bMoves[1]:
                a = 0
            else:
                a = 1
        
        elif j == 3:
            if bMoves[0] == 1 and bMoves[1] == 1: #CCC and CCD defect
                a = 0
                if bMoves[2] == 0: #CCD defect forever
                    flag = "defect"
            elif bMoves[0] == 0 and bMoves[1] == 0: #DDC/DDD defect forever
                a = 0
                flag = "defect"
            else:
                a = 1
        
        elif j == 4:
            #All C*** and DDDD
            if len(set(bMoves)) == 1: #CCCC defect, and DDDD defect forever
                if bMoves[0] == 1:
                    a = 0
                else:
                    a = 1
                    flag = "defect"

            elif bMoves[0] == 1 and bMoves[0] == 1: #CC** coop
                a = 0
                flag = "defect"

            elif bMoves[0] == 1 and bMoves[3] == 1: #CDCC and CDDC coop
                a = 0

            elif bMoves[0] == 1: #CDDD defect
                a = 1

            #All D***
            elif bMoves[0] == 0 and bMoves[1] == 1 and bMoves[3] == 1: #DCCC and DCDC coop
                a = 1
            else:
                a = 0
                flag = "defect"
        

        elif j == 5:
            if len(set(bMoves)) == 1 and bMoves[0] == 1:
                a = 0
                flag = "defect"
            
            elif bMoves[0] == 1 and bMoves[1]==0 and bMoves[3] == 1 and bMoves[4] == 1:
                a = 1
                flag = "coop"
            elif bMoves[0] == 0 and bMoves[1] == 1 and bMoves[3] == 1 and bMoves[4] == 1:
                a = 1
                flag == "coop"
            
            elif bMoves[0] == 1 and bMoves[1] == 1 and bMoves[2] == 1 and bMoves[3] == 1 and bMoves[4] == 0:
                a = 0
                flag = "half"
            else:
                a = 0
                flag = "defect"


        totalA = totalA + a

        if j == 0:
            b = random.randint(0,1)
        else:
            b = random.uniform(0,1)
            if b < totalA/j:
                b = 1
            else:
                b = 0
        bMoves.append(b)



        if a > b: #a cooperates, b defects
            scoreB = scoreB + 5
        elif b > a: #b cooperates, a defects
            scoreA = scoreA + 5
        elif a == 0: #both defect
            scoreA = scoreA + 1
            scoreB = scoreB + 1
        else: #both cooperate
            scoreA = scoreA + 3
            scoreB = scoreB + 3

print("Custom", scoreA/100000)
print("Avg. Copier", scoreB/100000)