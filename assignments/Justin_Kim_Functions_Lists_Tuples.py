def create_zoo():
    
    print("\033[2J\033[;H")
  
    zoo_animals = [
                   input(f"Zoo Animal {i+1}: ").lower()
                       for i in range(5)
                  ]
    
    print('\n' + '_'*20 + '\n')

    print("Zoo:", end="\n    ")
   
    print(*zoo_animals, sep="\n    ", end="\n\n")

    for animal in set(zoo_animals):
        amount = zoo_animals.count(animal)
        is_plural = amount!=1
        print(f"There {'are' if is_plural else 'is'} {amount} {animal}{'s' if is_plural else ''}")


def colour_converter():

    print("\033[2J\033[;H")

    r = int(input("Red: "))
    g = int(input("Green: "))
    b = int(input("Blue: "))
    rgb = (r, g, b)

    print(convert_rgb_to_hex(rgb))


def convert_rgb_to_hex(rgb):
    return "%02x%02x%02x" % rgb

def main():
    while True:
        input_ = input("Zoo or Colour or quit: ").lower()
        if input_ == "zoo":
            create_zoo()
        elif input_ == "colour":
            colour_converter()
        elif input_ == "quit":
            return
        else:
            print("Not an option buddy")

if __name__ == "__main__":
     main()
