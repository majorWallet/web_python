# ANSWER : START

import random
import csv
listValue = [ 0, 1, 2 ] # 0 is rock, 1 is paper, 2 is scissor
listDescription = [ "rock", "paper", "scissor" ]

class Player():
    def __init__(self, id = ''):
        self.id = id
    def getId(self):
        return self.id
    def setValue(self, listValue = -1):
        self.listValue = listValue
        if(listValue == -1):
            listValue = random.randrange(3)
    def getValue(self):
        return listValue

class Game():
    winner = 0
    gameCnt = 0
    session = '뷁'
    fileList = [['sequence','player1','player1-turn','player2','player2-turn','winner']]
    player1 = ''
    player2 = ''
    def __init__(self, player1 = '뷁', player2 = '뷁', session = '뷁'):
        if(player1 == '뷁' or player2 == '뷁' or session == '뷁'):
            self.player1 = player1
            self.player2 = player2
            self.sesison = session
            Game.session = self.sesison
            Game.player1 = self.player1
            Game.player2 = self.player2
        else:
            Game.gameCnt += 1
            self.player1 = player1
            self.player2 = player2
            self.sesison = session
            Game.session = self.sesison
            Game.player1 = player1.getId()
            Game.player2 = player2.getId()
    def runGame(self, value1 = -1, value2= -1):
        self.value1 = value1
        self.value2 = value2
        if(self.session == '뷁'):
            return (-1, -1)
        else:
            if(value1 == -1 and value2 == -1):
                self.value1 = random.randrange(3)
                self.value2 = random.randrange(3)
                return (self.value1, self.value2)
            else:
                return (value1, value2)
    def decideWinner(self):
        if(self.session == '뷁'):
            return -1
        else:
            if(self.value1 == 0 and self.value2 == 0):
                Game.winner = 0
            elif(self.value1 == 0 and self.value2 == 1):
                Game.winner = 2
            elif(self.value1 == 0 and self.value2 == 2):
                Game.winner = 1
            elif(self.value1 == 1 and self.value2 == 0):
                Game.winner = 1
            elif(self.value1 == 1 and self.value2 == 1):
                Game.winner = 0
            elif(self.value1 == 1 and self.value2 == 2):
                Game.winner = 2
            elif(self.value1 == 2 and self.value2 == 0):
                Game.winner = 2
            elif(self.value1 == 2 and self.value2 == 1):
                Game.winner = 1
            elif(self.value1 == 2 and self.value2 == 2):
                Game.winner = 0
            return Game.winner
    def logGame(self):
        if(self.session == '뷁'):
            return False
        else:
            if(Game.winner == 0):
                Game.fileList.append([str(Game.gameCnt), Game.player1, str(self.value1), Game.player2, str(self.value2), 'tie'])
                return True
            elif(Game.winner == 1):
                Game.fileList.append([str(Game.gameCnt), Game.player1, str(self.value1), Game.player2, str(self.value2), Game.player1])
                return True
            elif(Game.winner == 2):
                Game.fileList.append([str(Game.gameCnt), Game.player1, str(self.value1), Game.player2, str(self.value2), Game.player2])
                return True
    def closeSession(self):
        with open('log.csv', 'w') as fileWrite:
            myWriter = csv.writer(fileWrite)
            for i in range(len(Game.fileList)): 
                myWriter.writerow(Game.fileList[i])

# ANSWER : END

def displayGameResult(player1, givenGamer1, player2, givenGamer2, givenWinner):
    if (givenGamer1 != -1) and (givenGamer2 != -1) and (givenWinner != -1):
        msg = "[" + player1.getId() + ":" + listDescription[givenGamer1] + "] vs [" + player2.getId() + ":" + listDescription[givenGamer2] + "]"
        if winner == 1:
            msg += " -> winner is " + player1.getId()
        elif winner == 2:
            msg += " -> winner is " + player2.getId()
        else:
            msg += " -> tie game" 
        print(msg)
    else:
        print("Game session not ready")

player1 = Player("20190001")
player2 = Player("20190002")

game = Game(player1, player2, "myGame")

gamer1, gamer2 = game.runGame()
winner = game.decideWinner()
game.logGame()
displayGameResult(player1, gamer1, player2, gamer2, winner)

gamer1, gamer2 = game.runGame(listValue[0], listValue[1])
winner = game.decideWinner()
game.logGame()
displayGameResult(player1, gamer1, player2, gamer2, winner)

game.closeSession()