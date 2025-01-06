import random
import time
import os

#ASCII Art Dictionary
ascii_art = {
    "Light bulb": r"""  
  ..---..
 /       \\
|         |
:         ;
 \\  \\~/  /
  `, Y ,'
   |_|_|
   |===|
   |===|
    \\_/
    """,
    
    "Coffee": r"""                      
                            (
                        )     (
                 ___...(-------)-....___
             .-""       )    (          ""-.
       .-'``'|-._             )         _.-|
      /  .--.|   `""---...........---""`   |
     /  /    |                             |
     |  |    |                             |
      \\  \\   |                             |
       `\\ `\\ |                             |
         `\\ `|                             |
         _/ /\\                             /
        (__/  \\                           /
     _..---""` \\                         /`""---.._
  .-'           \\                       /          '-.
 :               `-.__             __.-'              :
 :                  ) ""---...---"" (                 :
  '._               `"--...___...--"`              _.'
jgs \\"--..__                              __..--""/
     '._     -""----.....______.....----""-     _.'
        `""--..,,_____            _____,,..--""`
                      `""------""`
    """,
    "Firework": r"""
                          . : .
      __________    '.  :  .'
     /         /\\__.__'.:.'  .
jgs  \\_________\\/  .  .':'.  .
                    .'  :  '.
                      ' : '
     """,
    "F1": r"""
                         __
                   _.--""  |
    .----.     _.-'   |/\\| |.--.
    |jrei|__.-'   _________|  |_)  _______________  
    |  .-""-.     ___,    `----'"))   __     .-""-.------._  
    '-' ,--. `    |tic|   .---.       |:.|  ' ,--. `      _`.
     ( (    ) ) __|tac|__ \\\\|// _..-- \\/( (    ) )--._".-.
      . `--' ;\\__________________..--------. `--' ;--------'
       `-..-'                               `-..-'
    """,
    
    "Crown": r"""
            .
                        .       |         .    .
                    .  *         -*-          *
                        \\        |         /   .
        .    .            .      /^\\     .              .    .
        *    |\\   /\\    /\\  / / \\ \\  /\\    /\\   /|    *
        .   .  |  \\ \\/ /\\ \\ / /     \\ \\ / /\\ \\/ /  | .     .
                \\ | _ _\\/_ _ \\\_\\_ _ /_/_ _\\/_ _ \\\_/
                \\  *  *  *   \\ \\/ /  *  *  *  /
                    ` ~ ~ ~ ~ ~  ~\\/~ ~ ~ ~ ~ ~ '
    """,
    "Charmander": r"""
              _.--""`-..
            ,'          `.
          ,'          __  `.
         /|          " __   \\
        , |           / |.   .
        |,'          !_.'|   |
      ,'             '   |   |
     /              |`--'|   |
    |                `---'   |
     .   ,                   |                       ,".
      ._     '           _'  |                    , ' \\ `
  `.. `.`-...___,...---""    |       __,.        ,`"   L,|
  |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\
-:..     `. `-..--_.,.<       `"      / `.        `-/ |   .
  `,         ""  '     `.              ,'         |   |  ',,
    `.      '            '            /          '    |'. |/
      `.   |              \\       _,-'           |       ''
        `._'               \\   '"\\                .      |
           |                '     \\                `._  ,'
           |                 '     \\                 .'|
           |                 .      \\                | |
           |                 |       L              ,' |
           `                 |       |             /   '
            \\                |       |           ,'   /
          ,' \\\               |  _.._ ,-..___,..-'    ,'
         /     .             .      `!             ,j'
        /       `.          /        .           .'/
       .          `.       /         |        _.'.'
        `.          7`'---'          |------"'_.'
       _,.`,_     _'                ,''-----"'
   _,-_    '       `.     .'      ,\\
   -" /`.         _,'     | _  _  _.|
    ""--'------""'        `' '! |! /
                             " " -' mh"""
}

# Hints Dictionary
hints = {
    "Light bulb": "Produces light from electricity.",
    "Coffee": "A beverage brewed from roasted seeds.",
    "Firework": "A small explosive device for celebrations.",
    "F1": "A motorsport with Grand Prix races.",
    "Charmander": "A fiery-tailed orange Pokémon.",
    "Crown": "Symbol of royalty and power."
}

def clear_terminal():
    print("c", end="")

def provide_hint(art_key):
    #Provide a hint for the given art key.
    return hints.get(art_key, "No hint available for this art.")

def play_game():
    #Main game function.
    score = 0
    total_time = 0  
    
    print("Welcome to the Python ASCII Art Guessing Game!")
    
    #Shuffle the art keys for random order
    art_keys = list(ascii_art.keys())
    random.shuffle(art_keys)
    
    for art_key in art_keys:
        clear_terminal()
        print("Guess this ASCII Art:")
        print(ascii_art[art_key])
        
        start_time = time.time()
        attempts = 0
        
        while True:
            guess = input("What do you think this is? (type 'hint' for a hint) ").strip().lower()
            attempts += 1
            
            if guess == "hint":
                print(f"Hint: {provide_hint(art_key)}")
            elif guess == art_key.lower():
                elapsed_time = round(time.time() - start_time, 2)
                total_time += elapsed_time
                print(f"Correct! You guessed it in {attempts} attempts and {elapsed_time} seconds.\n")
                score += 1
                break
            else:
                print("That's not correct. Try again!")
    
    print(f"Game Over!\nYour total score: {score}\nTotal time taken: {round(total_time, 2)} seconds.")

def main():
    play_game()

main()
