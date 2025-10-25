import turtle
wind = turtle.Screen()
wind.title("X GAME O ")
wind.bgcolor("#000000")
wind.setup(600, 600)
wind.tracer(0)
def main_mani() :
    
    while True :
        A =print ("""
            welcome to my game (X,O)
                  main mani 
                1-play the game   
                2-score save's
                3-exit
            """)
        User_in = int(input("inter your number chose :"))
        
        if User_in ==1:
            U_name1 = str(input("inter your user name 1:"))
            U_name2 = str(input("inter your user name 2:"))
            print (f"let's start the game {U_name1,U_name2} good luck")
            list1 = ["_","_","_","_","_","_","_","_","_"]
            print (f"{list1[0]}|{list1[1]}|{list1[2]}\n{list1[3]}|{list1[4]}|{list1[5]}\n{list1[6]}|{list1[7]}|{list1[8]}")
            while True :
                if list1[U1_in-1] =="0":list1[U1_in-1]="d"

                U1_in = int(input(f"{U_name1} inter your number (1-9):"))
                if list1[U1_in-1] =="_":
                    list1[U1_in-1] = "X"
                    print (f"{list1[0]}{list1[1]}|{list1[2]}\n{list1[3]}|{list1[4]}|{list1[5]}\n{list1[6]}|{list1[7]}|{list1[8]}")
                else :
                    print ("this place is already taken")
                    continue
                if list1[0]==list1[1]==list1[2]=="X" or list1[3]==list1[4]==list1[5]=="X" or list1[6]==list1[7]==list1[8]=="X" or list1[0]==list1[3]==list1[6]=="X" or list1[1]==list1[4]==list1[7]=="X" or list1[2]==list1[5]==list1[8]=="X" or list1[0]==list1[4]==list1[8]=="X" or list1[2]==list1[4]==list1[6]=="X":
                    print (f"congratulation {U_name1} you win")
                    break
                if "_" not in list1:
                    print ("the game is over no one win")
                    break
                U2_in = int(input(f"{U_name2} inter your number (1-9):"))
                if list1[U2_in-1] =="_":
                    list1[U2_in-1] = "O"
                    print (f"{list1[0]}|{list1[1]}|{list1[2]}\n{list1[3]}|{list1[4]}|{list1[5]}\n{list1[6]}|{list1[7]}|{list1[8]}")
                else :
                    print ("this place is already taken")
                    continue
                if list1[0]==list1[1]==list1[2]=="O" or list1[3]==list1[4]==list1[5]=="O" or list1[6]==list1[7]==list1[8]=="O" or list1[0]==list1[3]==list1[6]=="O" or list1[1]==list1[4]==list1[7]=="O" or list1[2]==list1[5]==list1[8]=="O" or list1[0]==list1[4]==list1[8]=="O" or list1[2]==list1[4]==list1[6]=="O":
                    print (f"congratulation {U_name2} you win")
                    break
                if "_" not in list1:
                    print ("the game is over no one win")
                    break
            
        elif User_in ==2:
            print ("score save's")
        elif User_in ==3:
            print ("see you later")
        break

main_mani()