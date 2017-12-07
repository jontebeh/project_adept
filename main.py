from Konto import konto
import random
import variables as var


def create_konto():
    vorname = input("Vorname: ")
    nachname = input("Nachname: ")
    inhaber = (vorname, nachname)
    pin_list = list("0000")
    for pin_number in range(4):
        pin_list[pin_number] = str(random.randint(0,9))
    pin = ''.join(pin_list)
    print("Ihre Pin lautet: ", pin)
    kontonummer_list = list("0000000000")
    for kontonummer_number in range(9):
        kontonummer_list[kontonummer_number] = str(random.randint(0,9))
    kontonummer_list[9] = str(len(var.konto_liste)+1)
    kontonummer = ''.join(kontonummer_list)
    print("Ihre Kontonummer lautet: ", kontonummer)
    new_konto = konto(inhaber, kontonummer, pin, 0, 0)
    var.konto_liste.append(new_konto)
    
def login():
    kontonummer = input("Geben sie ihre Kontonummer ein: ")
    for konten in var.konto_liste:
        if konten.Kontonummer == kontonummer:
            for versuche in range(3):
                pin = input("Geben sie ihre Pin ein: ")
                if pin == konten.Pin:
                    var.log_state = True
                    print("Login erfolgreich")
                    var.konto_now = var.konto_liste.index(konten)
                    break
                else:
                    print("Die von ihnen eingegebene Pin war leider falsch, bitte probieren sie es erneut")
    
def commands(usr_input, log_state, konto_now):
    if usr_input == "new konto":
        create_konto()
        
    elif usr_input == "login":
        if log_state == True:
            print("Du bist bereits eingelogt")
        else:
            login()
    elif usr_input == "logout":
        if log_state == True:
            print("Auf Wiedersehen!")
            log_state = False
        else:
            print("Sie sind nicht eingelogt!")
    elif usr_input == "show balance":
        if log_state == True:
            print("Ihr Kontostand lautet: ", var.konto_liste[konto_now].kontostand())
        else:
            print("Sie sind nicht eingelogt!")
    elif usr_input == "einzahlen":
        if log_state == True:
            betrag = int(input("Betrag, den sie einzahlen wollen: "))
            var.konto_liste[konto_now].einzahlen(betrag)
        else:
            print("Sie sind nicht eingelogt!")
    elif usr_input == "auszahlen":
        if log_state == True:
            betrag = int(input("Betrag, den sie auszahlen wollen: "))
            var.konto_liste[konto_now].auszahlen(betrag)
        else:
            print("Sie sind nicht eingelogt!")
            
    elif usr_input == "hilfe":
        print(var.help_text)
    else:
        print("command not found! Geben sie 'hilfe' fuer weiter informationen ein")
def main():
    while True:
        usr_command = input(">> ")
        commands(usr_command, var.log_state, var.konto_now)
        
main()

print("bye")
        

