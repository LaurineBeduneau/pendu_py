import random

mots = ["chat", "arbre", "maison", "ordinateur", "pomme", 
        "bouteille", "voiture", "ciel", "avion", "bicyclette"]

computer = random.choice(mots)
display = ['_' for _ in computer]
error = 0
max_error = 6

def update_game(user_input):
    global error, display
    if len(user_input) > 1:
        if user_input == computer:
            return True, f'Félicitations ! Le mot était : {computer}'
        else:
            error += 1
            return False, "Mauvaise supposition pour le mot complet."
    else:
        if user_input in computer:
            for count, lettre in enumerate(computer):
                if user_input == lettre:
                    display[count] = user_input
            return False, ' '.join(display)
        else:
            error += 1
            return False, f"La lettre '{user_input}' n'est pas dans le mot."

def check_win():
    if '_' not in display:
        return True, f'Félicitations ! Vous avez gagné avec {error} erreur(s) !'
    if error == max_error:
        return True, f"Perdu ! Le mot était : {computer}"
    return False, ""