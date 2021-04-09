##
##
##
##
##
##
from pysat.solvers import Glucose3
import os

## Covertpuzzle and add pure clauses
def puzStrTopuzInt(solver, puzzle):
    for i in range(25):
        for j in range(25):
            letter = puzzle[i][j]
            if letter == 'A':
                number = '1'
            elif letter == 'B':
                number = '2'
            elif letter == 'C':
                number = '3'
            elif letter == 'D':
                number = '4'
            elif letter == 'E':
                number = '5'
            elif letter == 'F':
                number = '6'
            elif letter == 'G':
                number = '7'
            elif letter == 'H':
                number = '8'
            elif letter == 'I':
                number = '9'
            ## dont add 10
            elif letter == 'J':
                number = '11'
            elif letter == 'K':
                number = '12'
            elif letter == 'L':
                number = '13'
            elif letter == 'M':
                number = '14'
            elif letter == 'N':
                number = '15'
            elif letter == 'O':
                number = '16'
            elif letter == 'P':
                number = '17'
            elif letter == 'Q':
                number = '18'
            elif letter == 'R':
                number = '19'
            ## dont add 20
            elif letter == 'S':
                number = '21'
            elif letter == 'T':
                number = '22'
            elif letter == 'U':
                number = '23'
            elif letter == 'V':
                number = '24'
            elif letter == 'W':
                number = '25'
            elif letter == 'X':
                number = '26'
            elif letter == 'Y':
                number = '27'
            else:
                number = '0'
    
            if number != '0':
                newI = i + 1
                if newI <= 9:
                    newI = newI
                elif newI >= 10 and newI < 19:
                    newI = newI + 1
                else: ## i >= 19
                    newI = newI + 2

                newJ = j + 1
                if newJ <= 9:
                    newJ = newJ
                elif newJ >= 10 and newJ < 19:
                    newJ = newJ + 1
                else: ## j >= 19
                    newJ = newJ + 2
                alwaysTrue = int(str(newI) + '0' + str(newJ) + '0' + number)
                solver.add_clause([alwaysTrue])
                ##print(alwaysTrue)
    return solver


## Add the row clauses
def addRows(solver):

    for n in range(25):

        newN = n + 1
        if newN <= 9:
            newN = newN
        elif newN >= 10 and newN < 19:
            newN = newN + 1
        else: ## n >= 19
            newN = newN + 2
        for i in range(25):
            newRow = []
            for j in range(25):
                newI = i + 1
                if newI <= 9:
                    newI = newI
                elif newI >= 10 and newI < 19:
                    newI = newI + 1
                else: ## i >= 19
                    newI = newI + 2

                newJ = j + 1
                if newJ <= 9:
                    newJ = newJ
                elif newJ >= 10 and newJ < 19:
                    newJ = newJ + 1
                else: ## j >= 19
                    newJ = newJ + 2
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(25):
                    newCounterRow = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterRow.append(newVal * -1)
                        newCounterRow.append(counterVal * -1)
                        ##print(newCounterRow)
                        solver.add_clause(newCounterRow)

                newRow.append(newVal)
            ##print(newRow)
            solver.add_clause(newRow)

    return solver

## Add the column clauses
def addCols(solver):

    for n in range(25):
        newN = n + 1
        if newN <= 9:
            newN = newN
        elif newN >= 10 and newN < 19:
            newN = newN + 1
        else: ## n >= 19
            newN = newN + 2
        for j in range(25):
            newRow = []
            for i in range(25):
                newI = i + 1
                if newI <= 9:
                    newI = newI
                elif newI >= 10 and newI < 19:
                    newI = newI + 1
                else: ## i >= 19
                    newI = newI + 2

                newJ = j + 1
                if newJ <= 9:
                    newJ = newJ
                elif newJ >= 10 and newJ < 19:
                    newJ = newJ + 1
                else: ## j >= 19
                    newJ = newJ + 2
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(25):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newX) + '0' + str(newJ) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterRow)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            ##print(newRow)
            solver.add_clause(newRow)
    return solver


## Add the square clauses
def addSquares(solver):

    ## model by adding each indivdual square

    ## square 1
    for n in range(25):

        newN = n + 1
        if newN <= 9:
            newN = newN
        elif newN >= 10 and newN < 19:
            newN = newN + 1
        else: ## n >= 19
            newN = newN + 2
        newSquare = []
        for i in range(5):
            newRow = []
            for j in range(5):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)

        ## square 2
        newSquare = []
        for i in range(5):
            newRow = []
            for j in range(5, 10):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
       ## print(newSquare)
        solver.add_clause(newSquare)


        ## square 3
        newSquare = []
        for i in range(5):
            newRow = []
            for j in range(10, 15):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
       ## print(newSquare)
        solver.add_clause(newSquare)

         ## square 4
        newSquare = []
        for i in range(5):
            newRow = []
            for j in range(15, 20):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)

         ## square 5
        newSquare = []
        for i in range(5):
            newRow = []
            for j in range(20, 25):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)

         
    ## Start next row of squares

        newSquare = []
        for i in range(5, 10):
            newRow = []
            for j in range(5):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)

        ## square 2
        newSquare = []
        for i in range(5, 10):
            newRow = []
            for j in range(5, 10):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
       ## print(newSquare)
        solver.add_clause(newSquare)


        ## square 3
        newSquare = []
        for i in range(5, 10):
            newRow = []
            for j in range(10, 15):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
       ## print(newSquare)
        solver.add_clause(newSquare)

         ## square 4
        newSquare = []
        for i in range(5, 10):
            newRow = []
            for j in range(15, 20):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)

         ## square 5
        newSquare = []
        for i in range(5, 10):
            newRow = []
            for j in range(20, 25):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)

         

         
    ## Start next row of squares

        newSquare = []
        for i in range(10, 15):
            newRow = []
            for j in range(5):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)

        ## square 2
        newSquare = []
        for i in range(10, 15):
            newRow = []
            for j in range(5, 10):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
       ## print(newSquare)
        solver.add_clause(newSquare)


        ## square 3
        newSquare = []
        for i in range(10, 15):
            newRow = []
            for j in range(10, 15):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
       ## print(newSquare)
        solver.add_clause(newSquare)

         ## square 4
        newSquare = []
        for i in range(10, 15):
            newRow = []
            for j in range(15, 20):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)

         ## square 5
        newSquare = []
        for i in range(10, 15):
            newRow = []
            for j in range(20, 25):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)

        
        
    ## Start next row of squares

        newSquare = []
        for i in range(15, 20):
            newRow = []
            for j in range(5):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)

        ## square 2
        newSquare = []
        for i in range(15, 20):
            newRow = []
            for j in range(5, 10):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
       ## print(newSquare)
        solver.add_clause(newSquare)


        ## square 3
        newSquare = []
        for i in range(15, 20):
            newRow = []
            for j in range(10, 15):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
       ## print(newSquare)
        solver.add_clause(newSquare)

         ## square 4
        newSquare = []
        for i in range(15, 20):
            newRow = []
            for j in range(15, 20):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)

         ## square 5
        newSquare = []
        for i in range(15, 20):
            newRow = []
            for j in range(20, 25):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)


        
    ## Start next row of squares

        newSquare = []
        for i in range(20, 25):
            newRow = []
            for j in range(5):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)

        ## square 2
        newSquare = []
        for i in range(20, 25):
            newRow = []
            for j in range(5, 10):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
       ## print(newSquare)
        solver.add_clause(newSquare)


        ## square 3
        newSquare = []
        for i in range(20, 25):
            newRow = []
            for j in range(10, 15):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
       ## print(newSquare)
        solver.add_clause(newSquare)

         ## square 4
        newSquare = []
        for i in range(20, 25):
            newRow = []
            for j in range(15, 20):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)

         ## square 5
        newSquare = []
        for i in range(20, 25):
            newRow = []
            for j in range(20, 25):
                
                newI, newJ = getIJ(i, j)
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(5):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newX) + '0' + str(newN)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterCol)
                        solver.add_clause(newCounterCol)
                newRow.append(newVal)
            for items in newRow:
                newSquare.append(items)
        ##print(newSquare)
        solver.add_clause(newSquare)

    
    return solver


## Add the unique clauses
def addUnique(solver):
    for n in range(25):

        newN = n + 1
        if newN <= 9:
            newN = newN
        elif newN >= 10 and newN < 19:
            newN = newN + 1
        else: ## n >= 19
            newN = newN + 2
        for j in range(25):
            newRow = []
            for i in range(25):
                newI = i + 1
                if newI <= 9:
                    newI = newI
                elif newI >= 10 and newI < 19:
                    newI = newI + 1
                else: ## i >= 19
                    newI = newI + 2

                newJ = j + 1
                if newJ <= 9:
                    newJ = newJ
                elif newJ >= 10 and newJ < 19:
                    newJ = newJ + 1
                else: ## j >= 19
                    newJ = newJ + 2
                newVal = int((str(newI) + '0' + str(newJ) + '0' + str(newN)))

                for x in range(25):
                    newCounterCol = []
                    newX = x + 1
                    if newX <= 9:
                        newX = newX
                    elif newX >= 10 and newX < 19:
                        newX = newX + 1
                    else: ## i >= 19
                        newX = newX + 2
                    
                    counterVal = int((str(newI) + '0' + str(newJ) + '0' + str(newX)))
                    if counterVal != newVal:
                        newCounterCol.append(newVal * -1)
                        newCounterCol.append(counterVal * -1)
                        ##print(newCounterRow)
                        solver.add_clause(newCounterCol)
            ##newRow.append(newVal)
            ##print(newRow)
            ##solver.add_clause(newRow)
        
    return solver


## helper function
def getIJ(i, j):
    newI = i + 1
    if newI <= 9:               
        newI = newI
    elif newI >= 10 and newI < 19:
        newI = newI + 1
    else: ## i >= 19
        newI = newI + 2

    newJ = j + 1
    if newJ <= 9:
        newJ = newJ
    elif newJ >= 10 and newJ < 19:
        newJ = newJ + 1
    else: ## j >= 19
        newJ = newJ + 2
    
    return newI, newJ
                

## Read a file in and add it to puzzle
def readSat(puzzleLink):
    file0 = open('puzzles/' + puzzleLink, "r")
    puzzle = []
    line = file0.readline()
    while line != "":
        line = line.rstrip()
        puzzleLine = []
        
        for letter in line:
            if letter != " ":
                puzzleLine.append(letter)

        if puzzleLine:
            puzzle.append(puzzleLine)
            ##print(puzzleLine)
        line = file0.readline()

    file0.close()

    return puzzle

## Read the solution and convert it to print format
def satToDoku(puzzle, solutions):
    for answer in solutions:
        
        positions = str(answer).split('0')
        strI = positions[0]
        strJ = positions[1]
        strVal = positions[2]

        newI = int(strI)
        if newI <= 9:
            newI = newI
        elif newI >= 10 and newI <= 19:
            newI = newI - 1
        else: ## i >= 19
            newI = newI - 2
        newI = newI - 1

        newJ = int(strJ)
        if newJ <= 9:
            newJ = newJ
        elif newJ >= 10 and newJ <= 19:
            newJ = newJ - 1
        else: ## j >= 19
            newJ = newJ - 2
        newJ = newJ -1

        if strVal == '1':
            intVal = 'A'
        elif strVal == '2':
            intVal = 'B'
        elif strVal == '3':
            intVal = 'C'
        elif strVal == '4':
            intVal = 'D'
        elif strVal == '5':
            intVal = 'E'
        elif strVal == '6':
            intVal = 'F'
        elif strVal == '7':
            intVal = 'G'
        elif strVal == '8':
            intVal = 'H'
        elif strVal == '9':
            intVal = 'I'
        elif strVal == '11':
            intVal = 'J'
        elif strVal == '12':
            intVal = 'K'
        elif strVal == '13':
            intVal = 'L'
        elif strVal == '14':
            intVal = 'M'
        elif strVal == '15':
            intVal = 'N'
        elif strVal == '16':
            intVal = 'O'
        elif strVal == '17':
            intVal = 'P'
        elif strVal == '18':
            intVal = 'Q'
        elif strVal == '19':
            intVal = 'R'
        elif strVal == '21':
            intVal = 'S'
        elif strVal == '22':
            intVal = 'T'
        elif strVal == '23':
            intVal = 'U'
        elif strVal == '24':
            intVal = 'V'
        elif strVal == '25':
            intVal = 'W'
        elif strVal == '26':
            intVal = 'X'
        elif strVal == '27':
            intVal = 'Y'
        else:
            print("error")
        
        if puzzle[newI][newJ] == '_':
            puzzle[newI][newJ] = intVal
        else:
            if puzzle[newI][newJ] != str(intVal):
                print("error with change")
                
    return puzzle






## Main functions
## Iterates through files 
##
def main():

    ## open files
    files = os.listdir('puzzles/')
    
    
    solver = Glucose3()
    
    for puzzles in files:
        print("Start Test :" + puzzles)
        print(" ")
        solver = Glucose3()
        puzzle = readSat(puzzles)
        solver = puzStrTopuzInt(solver, puzzle)
        solver = addRows(solver)
        solver = addCols(solver)
        solver = addSquares(solver)
        solver = addUnique(solver)

        solved = solver.solve()
        
        if solved == True:
            model = solver.get_model()
            numberSoluitons = 0
            
            model2 = solver.get_model()
            
             
            

            numberSoluitons = 0

    
            positives = []
            for items in model:
                if items > 0:
                    positives.append(items)

            positives2 = []
            for items in model2:
                if items > 0:
                    positives2.append(items)

            
    
            ogPuzzle = puzzle

            puzzle = satToDoku(puzzle, positives)
            puzzle2 = satToDoku(ogPuzzle, positives2)

            for i in range(25):
                for j in range(25):
                    if puzzle[i][j] != ogPuzzle[i][j]:
                        numberSoluitons = 2
            
        
        
            counter = 1
            for line in puzzle:
                count = 1
                strLine = ""
                for i in range(25):
                    strLine = strLine + line[i] + " "
                    if count % 5 == 0:
                        strLine = strLine + " " + " "
                        count = 1
                    else:
                        count = count + 1
                print(strLine)
                if counter % 5 == 0:
                    print(" ")
                    counter = 1
                else:
                    counter = counter + 1
        
            if numberSoluitons > 1:
                positives = []
                for items in model2:
                    if items > 0:
                        positives.append(items)
    
    

                puzzle2 = satToDoku(ogPuzzle, positives)
        
        
                counter = 1
                for line in puzzle2:
                    count = 1
                    strLine = ""
                    for i in range(25):
                        strLine = strLine + line[i] + " "
                        if count % 5 == 0:
                            strLine = strLine + " " + " "
                            count = 1
                        else:
                            count = count + 1
                    print(strLine)
                    if counter % 5 == 0:
                        print(" ")
                        counter = 1
                    else:
                        counter = counter + 1
            else:
                print("Solution is Unique")

    

        if solved == True:
            print("Success")
        else:
            print("No Solution")
        print("Test Complete")
        solver.delete()




main()
