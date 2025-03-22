from colorama import Fore, Back, Style
from src.scripts.decorators import input_error, check_arguments

contacts = {}

@check_arguments(2)
@input_error
def add(*args: tuple) -> int:
    print(args)
    *name_parts, phone = args
    name = " ".join(name_parts)
    
    contacts[name] = phone
    print(Fore.GREEN + f'Contact {name} with phone {contacts[name]} added successfully', Style.RESET_ALL)
    return 0
 
@check_arguments(1)
@input_error
def remove(*args) -> int:
    name = " ".join(args)
    
    contacts.pop(name)
    print(Fore.GREEN + f'Contact {name} removed successfully', Style.RESET_ALL)
    return 0

@check_arguments(2)
@input_error
def update(*args) -> int:
    name = " ".join(args)
    
    contacts[name] = phone
    print(Fore.GREEN + f'Contact {name} updated with phone {contacts[name]}', Style.RESET_ALL)
    return 0

@check_arguments(1)
@input_error
def show(*args) -> int:
    name = " ".join(args)
    
    print(Fore.GREEN + f'Contact {name}: {contacts[name]} found', Style.RESET_ALL)
    return 0

@input_error
def all() -> int:
    print(Fore.GREEN + f'List of all contacts', Style.RESET_ALL)
    print('')
    if not contacts:
        print(Fore.RED + 'No contacts found.', Style.RESET_ALL)
        return 1
    for name, phone in contacts.items():
        print(Back.CYAN + f'{name}:' + Back.RESET +  Fore.GREEN + f'\t{phone}', Style.RESET_ALL)
    print('')
    return 0

def close():
    print(Back.LIGHTWHITE_EX + Fore.BLACK + 'Goodbye.' + Style.RESET_ALL)
    return 0