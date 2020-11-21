def ask_for_number(secret_number):

    while True:
        answer=input(f'Zgaduję: czy tą liczbą jest {secret_number}? ')
        if answer=='za dużo':
            return 1
        elif answer=='za mało':
            return -1
        elif answer =='zgadłeś':
            return 0
        else:
            print('Nie rozumiem!\nPodaj jedną z odpoiwdzi: za dużo, za mało, zgadłeś')

