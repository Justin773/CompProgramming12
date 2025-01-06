def build_pyramid(base_width):
    if base_width > 0 and base_width % 2 == 1:  # Normal pyramid
        current_width = 1
        while current_width <= base_width:
            spaces = (base_width - current_width) // 2
            print(" " * spaces + "#" * current_width)
            current_width += 2
    elif base_width < 0 and abs(base_width) % 2 == 1:  # Upside-down pyramid
        base_width = abs(base_width)
        current_width = base_width
        while current_width > 0:
            spaces = (base_width - current_width) // 2
            print(" " * spaces + "#" * current_width)
            current_width -= 2
    else:
        print("Please enter an odd number for the base width.")

def main():
    base_width = int(input("Enter an odd number for the base width (negative for upside-down): "))
    build_pyramid(base_width)

main()
