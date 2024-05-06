from tkinter import messagebox
import tkinter as tk
import random


root = tk.Tk()
root.title('Wordle')
root.geometry("1152x864")
frame = tk.Frame(root)
frame.pack()
green = '#27e512'
yellow = '#e8ef0e'
gray = '#4c4c4c'
font = 'Verdana, 38'
letters = []
letter_count = 0
guess = ''
words = []
winner = False
with open('words.txt', 'r') as file:
    data = file.readlines()
    for i in data:
        words.append(i[:-1])
def win_lose(winner):
    if not winner:
        title = 'You Lose'
        message = f'The word was {word}'
    else:
        title = 'You Win'
        message = 'Well done, you got it in {} guess(s)'.format(int(letter_count / 5))
    play_again = messagebox.askquestion(title=title, message=f'{message}.\nWould you like to play again?')
    if play_again == 'yes':
        layout()
    else:
        root.destroy()
        quit()
def go_again():
    for i in range(5):
        letters[letter_count + i]['text'] = ' '
def check_word(guess):
    global winner
    btn_index = letter_count - 5
    for i, letter in enumerate(guess):
        if letter == word[i]:
            letters[btn_index + i]['bg'] = green
            letters[btn_index + i]['activebackground'] = green
        elif letter in word:
            if guess.count(letter) >= 1 and guess.count(letter) == word.count(letter):
                letters[btn_index + i]['bg'] = yellow
                letters[btn_index + i]['activebackground'] = yellow
            else:
                letters[btn_index + i]['bg'] = gray
                letters[btn_index + i]['activebackground'] = gray
        else:
            letters[btn_index + i]['bg'] = gray
            letters[btn_index + i]['activebackground'] = gray
    if guess == word:
        winner = True
        win_lose(winner)
def key_pressed(letter):
    global letter_count, guess
    if not winner:
        if letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                      'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
            if letter_count <= 29:
                letters[letter_count]['text'] = letter.upper()
                guess = guess + letter.upper()
                letter_count += 1
                if letter_count % 5 == 0:
                    if guess.lower() in words:
                        check_word(guess)
                        guess = ''
                    else:
                        letter_count -= 5
                        go_again()
                        guess = ''
            if letter_count == 30:
                win_lose(winner)

def create_keyboard_buttons(keyboard_frame):
    keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for key in keys:
        tk.Button(keyboard_frame, text=key, width=3, command=lambda k=key: key_pressed(k.lower())).pack(side=tk.LEFT, padx=5)

def layout():
    global frame, letter_count, winner, guess, word
    frame.destroy()
    frame = tk.Frame(root)
    frame.pack()
    letters.clear()
    letter_count = 0
    winner = False
    guess = ''
    word = random.choice(words).upper()
    for row in range(6):
        for col in range(5):
            btn = tk.Button(frame, text=' ', width=3, bg='white',
                            activebackground='white', font=font)
            btn.grid(row=row, column=col, padx=5, pady=7)
            letters.append(btn)
    keyboard_frame = tk.Frame(root)
    keyboard_frame.pack(pady=10)
    create_keyboard_buttons(keyboard_frame) 

    menu = tk.Menu(root)
    root.config(menu=menu)
    new_game = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label='Game', menu=new_game)
    new_game.add_command(label='New Game', command=layout)
layout()
root.mainloop()