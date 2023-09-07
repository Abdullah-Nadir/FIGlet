import pyfiglet
import sys

# Checking Command-line arguments
if len(sys.argv) != 1 and len(sys.argv) != 3:
    print("Invalid usage")
    sys.exit(1)

# Condition if the user give's no arguments for random fonts
if len(sys.argv) == 1:
    # taking inut from user
    input = input("Input: ")
    # Create a figlet font
    font = pyfiglet.Figlet()
    # Generate ascii_art text
    ascii_art = font.renderText(input)
    # Printing ascii-art text
    print(ascii_art)

# For specified fonts
else:
    # Taking input from user
    input = input("Input: ")
    # Validation of the first argument
    if sys.argv[1] in ["-f", "--font"]:
        try:
            # Create a figlet font
            font = pyfiglet.Figlet(font=sys.argv[2])
            # Generate ascii_art text
            ascii_art = font.renderText(input)
            # Printing ascii-art text
            print(ascii_art)
        except pyfiglet.FontNotFound as e:
            print(f"Font not found: {e}")
            sys.exit(1)
    else:
        print("Invalid usage")
        sys.exit(1)


sys.exit(0)


