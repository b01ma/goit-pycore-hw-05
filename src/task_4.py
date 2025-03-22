'''
    Напишіть консольного бота помічника, який розпізнаватиме команди, 
    що вводяться з клавіатури, та буде відповідати відповідно до введеної команди.
'''

import src.scripts.contacts as contacts
from colorama import Fore, Back, Style

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    '''
        Main function for the assistant bot
        takes following commands:
        - hello - greets the user
        - add <name> <phone> - adds a contact
        - remove <name> - removes a contact
        - update <name> <phone> - updates a contact
        - show <name> - shows a contact
        - all - shows all contacts
        - close/exit - closes the bot
    '''
    print( Back.LIGHTWHITE_EX + Fore.BLACK + "Welcome to the assistant bot!" + Style.RESET_ALL)
    print('')
    while True:
        user_input = input(Fore.BLUE + 'Enter a command: ' + Style.RESET_ALL)
        if user_input.strip() == '':
            print(Fore.YELLOW + 'Please enter a command.')
            continue
        
        cmd, *args = parse_input(user_input)
        
        if cmd == '':
            print(Fore.YELLOW + 'Please enter a command.')
            continue
        elif cmd in ["close", "exit"]:
            contacts.close()
            break
        elif cmd == 'hello':
            print(Fore.GREEN + 'Hello! I am your assistant, how can I help you?' + Style.RESET_ALL)
        elif cmd == 'add':
            contacts.add(*args)
        elif cmd == 'remove':
            contacts.remove(*args)
        elif cmd == 'update':
            contacts.update(*args)
        elif cmd == 'show':
            contacts.show(*args)
        elif cmd == 'all':
            contacts.all()
        else:
            print(Fore.YELLOW + 'Unknown command. Please try again.')
        
if __name__ == '__main__':
    main()