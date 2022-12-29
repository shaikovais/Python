import random

def get_choices():
    player_choice = input ("chun miya ek (rock,paper,scissor) : ") # getting input from user
    options = ["rock" , "paper" ,"scissor"]   # making  a list of options
    computer_choice = random.choice(options)   # making use of random library and choice function
    choices = {"player" : player_choice , "computer": computer_choice} # creating a dict with both user and computer results
    return choices

# Once you return something from the function next lines are ignored
def check_win(player , computer):
    #print ("tum chuney " + player + "computer chuna " + computer)  
    print (f"tum chuney   {player}  computer chuna {computer}")    # above line and this both are equal
    if player == computer :
        return "tie hogaya " 
    elif player == "rock" :
        if computer == "scissor" :
            return "rock mardiya miya tum jeet gaye"
        else :
            return "computer lapat diya tumaku hargaye tum"
    elif player == "paper" :
        if computer == "rock" :
            return "paper lapat diya jeet agye aap "
        else :
            return "computer scissor se kaat diya apku"
    elif player == "scissor" :
        if computer == "rock" :
            return "rock tod diya scissor hargaye tum "
        else :
            return " scissor se kaat diya aap jeet gaye"
    


#choices = check_win ("rock","paper")   # just becoz the funtion return on equality this returns NULL

choice = get_choices()
result = check_win (choice["player"] , choice["computer"])
print(result)


