from colorama import Fore, Style
import re

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            print(Fore.RED + f"Error: KeyError occurred: {e}" + Style.RESET_ALL)
            return 1
        except ValueError as e:
            print(Fore.RED + f"Error: ValueError occurred: {e}" + Style.RESET_ALL)
            return 1
        except IndexError as e:
            print(Fore.RED + f"Error: IndexError occurred: {e}" + Style.RESET_ALL)
            return 1
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
            return 1
    return inner

def check_arguments(min_args: int):
    def decorator(func):
        def inner(*args, **kwargs):
            try:
                if len(args) < min_args:
                    raise ValueError(f"Please provide at least {min_args} arguments")
                # if min_args == 1 - expects to be a name variable
                if min_args == 1:
                    name  = " ".join(args)
                    if not re.match(r'^[A-Za-z][A-Za-z ]*$', name):
                        raise ValueError(f"name must be a string")

                # if min_args == 2 - expects to be a name and phone variables
                if min_args == 2:
                    *name_parts, phone = args
                    name = " ".join(name_parts)

                    if not re.match(r'^[A-Za-z][A-Za-z ]*$', name):
                        raise ValueError(f"name must be a string")
                    if not re.match(r'^\+?\d{1,12}$', phone):
                        raise ValueError(f"phone number must be an integer and no longer then 12 digits")
            except ValueError as e:
                print(Fore.RED + f"Error: ValueError {e}" + Style.RESET_ALL)
                return 1
            return func(*args, **kwargs)
        return inner
    return decorator