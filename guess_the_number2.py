def ask_for_number(secret_number):
    """the function gets the player's answers
        and checks for errors

        :param: integer
        :return: integer
        """
    while True:
        answer = input(f'Zgaduję: czy tą liczbą jest {secret_number}? ')

        if answer == 'za dużo':
            return 1
        elif answer == 'za mało':
            return -1
        elif answer == 'zgadłeś':
            return 0
        else:
            print('Nie rozumiem!\nPodaj jedną z odpoiwdzi: za dużo, za mało, zgadłeś')


def guess_the_number2():
    """Main function Guess The Number 2"""

    print('Pomyśl liczbę od 0 do 1000 a sa ją zgadnę w max 10 próbach')
    min_number = 0
    max_number = 1000

    while True:
        guess = int((max_number - min_number) / 2) + min_number
        answer = ask_for_number(guess)

        if answer == 1:
            max_number = guess
        elif answer == -1:
            min_number = guess
        elif answer == 0:
            print('Wygrałem!')
            break


if __name__ == '__main__':
    guess_the_number2()
