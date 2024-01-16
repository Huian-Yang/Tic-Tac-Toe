from tkinter import *
import random 


def next_turn(row, column): #check who has next turn
    
    global player #get access to variable "player"
    
    if buttons[row][column]['text'] == "" and check_winner() is False: #if the button on the specific row & column is empty and the winner condition have not been filled
        
        if player == players[0]: #if it is player one's turn
            
            buttons[row][column]['text'] = player #set what is going to be on the button label as the "player" (basically fill button in)

            if check_winner() is False: #if check_winner is false
                player = players[1] #we will switch players from index 0 to 1
                label.config(text=(players[1]+"turn")) #displays the next player's turn
                
            elif check_winner() is True: #if check_winner is true
                label.config(text=(players[0]+" wins"))  #declare a player one as winner
                
            elif check_winner() == "Tie": 
                label.config(text=("Tie!")) #changes the label to tie
                
        else: #player two's turn
            
            buttons[row][column]['text'] = player #set what is going to be on the button label as the "player" (basically fill button in)

            if check_winner() is False: #if check_winner is false
                player = players[0] #we will switch players from index 1 to 0
                label.config(text=(players[0]+"turn")) #displays the next player's turn
                
            elif check_winner() is True: #if check_winner is true
                label.config(text=(players[1]+" wins"))  #declare a player two as winner
                
            elif check_winner() == "Tie": 
                label.config(text=("Tie!")) #changes the label to tie
                
def check_winner(): #check who has won
    
    for row in range(3): #for a horizontal row
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "": #if all the buttons are the same and does not have a empty space, then someone won (horizontal)
            buttons[row][0].config(bg="green") #change color, after there is a win
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True #will return True, indicating someone won 
        
    for column in range(3):  #iterate over columns in the next loop
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green") #change color, after there is a win
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True 
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "": #left diagonal row
        buttons[0][0].config(bg="green") #change color, after there is a win
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "": #right diagonal row
        buttons[0][2].config(bg="green") #change color, after there is a win
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    
    elif not empty_spaces():   #if all spaces are taken and there is no rows
        
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow") #change all button color to yellow if there is a tie

        return "Tie" #it is a tie
    
    else:
        return False
    
def empty_spaces(): #check for empty spaces
    
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True  # Return True if any space is empty
    return False

def new_game():
    
    global player
    
    player = random.choice(players) #chooses a new player to go first from ("x","o")
    
    label.config(text=player+" turn") #change the label to new player's turn
    
    for row in range(3): #clear all buttons in row
        for column in range(3): #clear all buttons in column
            buttons[row][column].config(text="",bg="#F0F0F0") #chnage all button to empty and color back to normal 
    

window = Tk()
window.title("Tic-Tac-Toe")
players = ["x","o"] #creates 2 players and is represented through index 1(player two) and 0(player one) in functions
player = random.choice(players) #randomly chooses from the list
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]] #2D list (the board)

label = Label(text=player + " turn", font=('consolas',40)) #display whoose turn it is
label.pack(side="top") #pack it to top

reset_button = Button(text="restart", font=('consolas',20), command=new_game)  #restart button
reset_button.pack(side="top")

frame = Frame(window) #create a frame and add it to window
frame.pack()

for row in range(3): #nested for loop #incharge of rows
    for column in range(3): #in charge of columns
        buttons[row][column] = Button(frame, text="", font=('consolas', 40), #depending on the iteration of our loop, we will create different buttons
                                      width=5,height=2, command= lambda row=row, column =column: next_turn(row,column)) 
        buttons[row][column].grid(row=row,column=column) #add buttons to grid

window.mainloop()