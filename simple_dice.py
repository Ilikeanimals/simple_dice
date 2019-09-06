import random

def roll():
    sides = 6
    num_rolled = random.randint(1,sides)
    return num_rolled


def main():
    sides = 6
    rolling = True
    while rolling:
        roll_again = input('Ready to roll? Enter=Roll. Q=Quit.')
        if roll_again.lower() != 'q':
            num_rolled = roll()
            print("you rolled",num_rolled)

        else:
            rolling = False
        print('Thank you for playing')

if __name__ == '__main__':
    main()
