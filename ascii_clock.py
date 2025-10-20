# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names: Benjamin Nasse
#        Cameron Seal
#        Charles Thomas
#        Nicholas Strickler
#        Radwan Merhebi
# Section: 564
# Assignment: Lab 8 group
# Date: 10/20/2025

time = input("Enter the time: ")
format = int(input("Choose the clock type (12 or 24): "))
char = input("Enter your preferred character: ")

# Validate character input - reject digits, certain punctuation, and confusing letters
invalid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                 ':', '/', '\\', '|', '_', '.', ',', ';', '!', '?', ' ',
                 'i', 'I', 'o', 'O', 'l', 'L', 't', 'T', 'j', 'J', '<', '>', '%', '#']
while any(c in invalid_chars for c in char):
    char = input("Character not permitted! Try again: ")


def print_ascii_clock(time_str, clock_format, fill_char):
    # ASCII art patterns for digits 0-9
    digits = {
        '0': ["000", "0 0", "0 0", "0 0", "000"],
        '1': [" 1 ", "11 ", " 1 ", " 1 ", "111"],
        '2': ["222", "  2", "222", "2  ", "222"],
        '3': ["333", "  3", "333", "  3", "333"],
        '4': ["4 4", "4 4", "444", "  4", "  4"],
        '5': ["555", "5  ", "555", "  5", "555"],
        '6': ["666", "6  ", "666", "6 6", "666"],
        '7': ["777", "  7", "  7", "  7", "  7"],
        '8': ["888", "8 8", "888", "8 8", "888"],
        '9': ["999", "9 9", "999", "  9", "999"]
    }
    
    # Colon pattern
    colon = ["  ", " :", "  ", " :", "  "]
    
    # AM/PM
    am_pm = {
        'A': [" A ", "A A", "AAA", "A A", "A A"],
        'P': ["PPP", "P P", "PPP", "P  ", "P  "],
        'M': ["M   M", "MM MM", "M M M", "M   M", "M   M"]
    }
    
    # Parse time
    hour, minute = time_str.split(':')
    hour = int(hour)
    minute = int(minute)
    
    # Convert to 12-hour format if needed
    suffix = ""
    if clock_format == 12:
        if hour == 0:
            hour = 12
            suffix = "AM"
        elif hour < 12:
            suffix = "AM"
        elif hour == 12:
            suffix = "PM"
        else:
            hour -= 12
            suffix = "PM"
    
    # Build the time string
    time_digits = f"{hour:02d}:{minute:02d}"
    
    # Remove leading zero for single digit hours in display
    if time_digits[0] == '0':
        time_digits = ' ' + time_digits[1:]
    
    # Use digit itself if no character provided
    if fill_char == '':
        fill_char = None
    
    print()
    # Print each line
    for line_num in range(5):
        output = ""
        for char_idx, ch in enumerate(time_digits):
            if ch == ':':
                output += colon[line_num]
            elif ch == ' ':
                output += ""
            else:
                pattern = digits[ch][line_num]
                # Replace digit with fill character
                if fill_char:
                    pattern = pattern.replace(ch, fill_char)
                output += pattern
            
            # Add space between characters (not before colon or after space)
            if char_idx < len(time_digits) - 1:
                next_ch = time_digits[char_idx + 1]
                if ch != ' ' and next_ch != ':':
                    output += " "
        
        # Add AM/PM if 12-hour format
        if suffix:
            output += " "
            for letter_idx, letter in enumerate(suffix):
                pattern = am_pm[letter][line_num]
                output += pattern
                if letter_idx < len(suffix) - 1:
                    output += " "
        
        print(output)

print_ascii_clock(time, format, char)