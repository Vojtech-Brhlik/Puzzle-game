#################################################################
#                                                               #
#                                                               #
#                     Terminal simulation for                   #
#                       teambuilding puzzle                     #
#                    -------------------------                  #
#                                                               #
#     Author: Vojtech Brhlik                                    #
#     Date:   September 2023                                    #
#                                                               #
#################################################################


import re           #re.split()
import random       #random.choice()

########################### DEF #################################

#PROCESS RED ANSWER
def red_answer(str):
    if (str == "RED ANSWER 231"):
        ANS = input("  # # OODPOVĚDI: ")
        RED_ANS[0] = ANS
        
    elif (str == "RED ANSWER 262"):
        ANS = input("  # # OODPOVĚDI: ")
        RED_ANS[1] = ANS
        
    elif (str == "RED ANSWER 13"):
        ANS = input("  # # OODPOVĚDI: ")
        RED_ANS[2] = ANS
        
    elif (str == "RED ANSWER 465"):
        ANS = input("  # # OODPOVĚDI: ")
        RED_ANS[3] = ANS
    
    #WRONG ANSWER NUMBER
    else:
        print("    # Neplatná odpověď.")

#PROCESS BLUE ANSWER
def blue_answer(str):
    if (str == "BLUE ANSWER 1523"):
        ANS = input("  # # OODPOVĚDI: ")
        BLUE_ANS[0] = ANS
        
    elif (str == "BLUE ANSWER 211"):
        ANS = input("  # # OODPOVĚDI: ")
        BLUE_ANS[1] = ANS
        
    elif (str == "BLUE ANSWER 37"):
        ANS = input("  # # OODPOVĚDI: ")
        BLUE_ANS[2] = ANS
        
    elif (str == "BLUE ANSWER 490"):
        ANS = input("  # # OODPOVĚDI: ")
        BLUE_ANS[3] = ANS
    
    #WRONG ANSWER NUMBER
    else:
        print("    # Neplatná odpověď.")
    

########################### INIT ################################

#LOGGED TRIGGER CHECK
LOGGED_BLUE = False
LOGGED_RED = False

#GPS TRIGGER CHECK
GPS_BLUE = False
GPS_RED = False

#USED PASSWORDS
PWD_BLUE = "IAPUTKEF"
PWD_RED = "AXRJEHSX"

#ANSWERS LIST
RED_ANS = [None for i in range(4)]
BLUE_ANS = [None for i in range(4)]

#HELLO LIST
HELLO_LIST = ["Ahojky :3", "Cauko", "HELLO", 
         "Nazdárek", "Ahojda", "Cauwec", "Hi there", "Hello there", 
         "Dobrý den", "Také zdravím", "Čaaaau <3", "Čauky", "Zduř",
         "Zdarec"]

#Just printing some random stuff to hide the starting command
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n##########################################################################################\n")

print("\nInicializace systému...\n\nSpouštění serveru...\n\nAktivace brány...\n\nZkouška spojení...\n\n...\n\n")
print("Úspěšné testy: 55/55\n\n\tServerové testy: 25/25\n\n\tTesty připojení: 18/18\n\n\tBezpečnostní testy: 11/11\n\n\tUwu test: 1/1\n\n")
print("\t\t\t\t    ZAHAJUJI KOMUNIKACI\n")

print("##########################################################################################\n")

while(True):
    INPUT = input("  # ")

    ########################### MISC ################################
    
    #UH OH
    if (re.search("UH OH", INPUT.upper()) is not None):
        print("    # uh oh.\n")
    
    #UWU OWO
    if (re.search("UWU", INPUT.upper()) is not None
        or re.search("OWO", INPUT.upper()) is not None):
        print("    # Nya.\n")

    #HELLO
    if (re.search("HELLO", INPUT.upper()) is not None
        or re.search("AHOJ", INPUT.upper()) is not None):
        print("    # " + random.choice(HELLO_LIST) + "\n")
        
    ######################### USEFUL ################################

    #CLUELESS
    if (re.search("\?", INPUT) is not None 
        and (re.search("HELP", INPUT.upper()) is None 
        or re.search("POMOC", INPUT.upper()) is None)):
        
        print("    # Pro pomoc použij příkaz HELP nebo POMOC.\n")

    #HELP
    if (re.search("HELP", INPUT.upper()) is not None 
        or re.search("POMOC", INPUT.upper()) is not None):

        #LOGGED check
        if (LOGGED_BLUE == False and LOGGED_RED == False):
            print("    # Pro zjištění více informací je nutné přihlášení do systému.")
            print("    # Přihlášení provedete pomocí příkazu BLUE/RED (podle barvy týmu).")
            print("    # Poté budete vyzvání k zadání osmimístného hesla. Dílky vašeho hesla najdete poschovávané po místnosti.\n")

        #LOGGED success
        else:
            print("    # Přihlášení zaznamenáno.")
            print("    # Vítejte agenti. Požadované informace naleznete v obálkách po okolí.")
            print("    # Pro zjištění pozice vašich informací použijte příkaz BLUE/RED GPS.")
            print("    #")
            print("    # Pro zadání odpovědi do systému použijte příkaz BLUE/RED ANSWER XXX kde:")
            print("    # #  ")
            print("    # # XXX je číslo, které najdete na obálce (Tedy např. RED ANSWER 123).")
            print("    #")
            print("    # Poté budete vyzváni k zadání odpovědi.\n")
    
    #BLUE LOGIN
    elif (INPUT == "BLUE"):
        
        #LOGGED check
        if (LOGGED_BLUE == False):
            PWD = input("  # # PASSWORD: ")
            
            #PWD check
            if (PWD == PWD_BLUE):
                print("    # Tým BLUE úspěšně přihlášen.")
                print("    # Příkaz HELP obsahuje další informace.\n")
                LOGGED_BLUE = True
            
            #PWD wrong
            else:
                print("    # Neplatné heslo. Ruším přihlášení.\n")
        
        #LOGGED already
        else:
            print("    # Tým je již přihlášen.\n")
                   
    #RED LOGIN
    elif (INPUT == "RED"):
        
        #LOGGED check
        if (LOGGED_RED == False):
            PWD = input("  # # PASSWORD: ")
            
            #PWD check
            if (PWD == PWD_RED):
                print("    # Tým BLUE úspěšně přihlášen.")
                print("    # Příkaz HELP obsahuje další informace.\n")
                LOGGED_RED = True
            
            #PWD wrong
            else:
                print("    # Neplatné heslo. Ruším přihlášení.\n")    
        
        #LOGGED already
        else:
            print("    # Tým je již přihlášen.\n")
            
    #BLUE GPS
    elif (INPUT == "BLUE GPS"):
        
        #LOGGED check
        if (LOGGED_BLUE == True):
            print("    # ZA ROTUNDOU")
            print("    # VRÁSA")
            print("    # POD KAŠTANEM")
            print("    # BOROVICE U KLUBOVNY\n")
            GPS_BLUE = True
        #LOGGED fail
        else:
            print("    # Nepovolený přístup. Nutné přihlášení.\n")
            
    #RED GPS
    elif (INPUT == "RED GPS"):
        
        #LOGGED check
        if (LOGGED_RED == True):
            print("    # SV. ANNA")
            print("    # AKVARISTIKA U PRASEČÍHO PLÁCKU")
            print("    # ZIMNÍ STADION")
            print("    # OKAP KLUBOVNY\n")
            GPS_RED = True
        #LOGGED fail
        else:
            print("    # Nepovolený přístup. Nutné přihlášenín.\n")
        
    #RED ANSWER    
    elif (re.search("RED ANSWER", INPUT) is not None and GPS_RED == True):
        red_answer(INPUT)
        print("\n")
        
    #BLUE ANSWER    
    elif (re.search("BLUE ANSWER", INPUT) is not None and GPS_BLUE == True):
        blue_answer(INPUT)
        print("\n")
    
    #UNKNOWN COMMAND  
    else:
        print("    # Neznámý příkaz.\n")
        
    #RED END CHECK
    if (all([item is not None for item in RED_ANS])):
        print("\n##########################################################################################\n")
        print(r"""
                     TÝM
                     RED
                    VÍTĚZÍ
                _____________
                '._==_==_=_.'
                .-\:      /-.
               | (|:.     |) |
                '-|:.     |-'
                  \::.    /
                   '::. .'
                     ) (
                   _.' '._
                  |_______|""")
        
        print("\n\n\tOdpovědi:")
        for index, item in enumerate(RED_ANS):
            print(f"\t{index + 1}) ", item)
            
        print("\n##########################################################################################\n")
        
        #ENDLESS NOTHING
        while(True):
            pass
    
    #BLUE END CHECK
    if (all([item is not None for item in BLUE_ANS])):
        print("\n##########################################################################################\n")
        print(r"""
                     TÝM
                     BLUE
                    VÍTĚZÍ
                _____________
                '._==_==_=_.'
                .-\:      /-.
               | (|:.     |) |
                '-|:.     |-'
                  \::.    /
                   '::. .'
                     ) (
                   _.' '._
                  |_______|""")
        
        print("\n\n\tOdpovědi:")
        for index, item in enumerate(BLUE_ANS):
            print(f"\t{index + 1}) ", item)
        
        print("\n##########################################################################################\n")
        
        #ENDLESS NOTHING
        while(True):
            pass