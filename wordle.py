import pathlib
import random
from rich.console import Console
from rich.theme import Theme

console = Console(theme=Theme({"warning": "red on yellow"}))

def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n")

def word_analysis(secret_word, guess):
    ''' Classifies all of the letters in a guess word

    ## Example:

    >>> word_analysis('crane', 'snake')
    [('s', 'Incorrect'), ('n', 'Misplaced'), ('a', 'Correct'), ('k', 'Incorrect'), ('e', 'Correct')]
    
    '''
    
    if len(secret_word) < len(guess):
        #print("Guess is longer than the secret word")
        return None
    secret_word_unique_letters = set(secret_word)
    guess_word_unique_letters = set(guess)


    data = []
    for i in range(len(guess)):
        if guess[i] == secret_word[i]:
            data.append((guess[i], 'Correct', 'bold white on green'))
        elif guess[i] in secret_word:
            data.append((guess[i], 'Misplaced', 'bold white on yellow'))
        else:
            data.append((guess[i], 'Incorrect', 'white on #666666'))

    return data


def displaying_guesses(guess_list, secret_word):
    for guess in guess_list:
        styled_guess = []
        guess_data = word_analysis(secret_word, guess)

        if guess_data == None:
            styled_guess.append(f"[{'dim'}]{'_'}[/]"*5)
    
        else: 
            
            for i in range(5):
                if i>=len(guess):
                    styled_guess.append(f"[{'dim'}]{'_'}[/]")
                else:
                    styled_guess.append(f"[{guess_data[i][2]}]{guess[i]}[/]")

        console.print("".join(styled_guess), justify="center")


def generate_random_word(file_path):
    ''' Returns a random word given a path to a file with words'''

    WORDLIST = pathlib.Path(file_path)
    words_list = [word.lower() for word in WORDLIST.read_text().strip().split('\n') if len(word) == 5]

    return random.choice(words_list)


def word_check(secret_word, guess):
    ''' Simply checks, and outputs a message, if the guess is the same as the secret word'''

    if guess.lower() == secret_word:
        print('Correct! You won the game!')
        return True
    else:
        #print('Incorrect. Try Again')
        return False


def solution_teller(solution):
    ''' Solution print message'''
    print(f'Good try! The word was {solution}')

def user_input():
    guess = input('Guess a five-letter word: ').strip()
    while len(guess) != 5 and guess.isalpha():
        console.print('Your guess must be 5 letters', style='warning')
        guess = input('Guess a five-letter word: ').strip()

    return guess




def main():
    refresh_page('Wordle')
    
    secret_word = generate_random_word('wordlist.txt')
    guesses = ['_'*5] * 5

    for attempts in range(5):

        displaying_guesses(guesses, secret_word)
        guess = user_input()
        refresh_page(f'Guesses: {attempts+1}/5')
        guesses[attempts] = guess

        checker = word_check(secret_word, guess)
        if checker == True:
            break


    else:
        displaying_guesses(guesses, secret_word)
        solution_teller(secret_word)




if __name__ == "__main__":
    main()
    #print(word_analysis('crane', 'snake'))
    #refresh_page('Wordle')
    #console.print("Hello, [bold red]Rich[/] :snake:", style='warning')


