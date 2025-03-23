'''
    Необхідно створити функцію generator_numbers, яка буде аналізувати текст, ідентифікувати 
    всі дійсні числа, що вважаються частинами доходів, і повертати їх як генератор. Дійсні числа
    у тексті записані без помилок, чітко відокремлені пробілами з обох боків. Також потрібно 
    реалізувати функцію sum_profit, яка буде використовувати generator_numbers для підсумовування 
    цих чисел і обчислення загального прибутку.
'''

from colorama import Fore, Style
import re

example_text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text: str):
    '''
        Function to generate numbers from the text
        :param text: str: text to parse
        :return generator: float: number
    '''
    if not isinstance(text, str):
        print(Fore.RED + 'Text is not a string')
        return None
    if not text:
        print(Fore.RED + 'Text is empty')
        return None
    
    number_pattern = re.finditer(r'\b\d+(\.\d+)?\b', text)
    for number in number_pattern:
        yield float(number.group())

def sum_profit(text: str, callback: callable):
    '''
        Function to sum profit from the text
        :param text: str: text to parse
        :param callback: callable: function to generate numbers
    '''
    total = 0
    for number in callback(text):
        total += number
    if not total:
        print(Fore.RED + 'No numbers found')
        return None
    print(Fore.CYAN + 'Total: ', total)

def main():
    print('Sum of all numbers from the text')
    
    print(Fore.YELLOW + 'In the text: ' + Style.RESET_ALL, example_text)
    sum_profit(example_text, generator_numbers)
    print('')
    
    print(Fore.YELLOW + 'In the text: ' + Style.RESET_ALL, 123)
    sum_profit(123, generator_numbers)
    print('')
    
    print(Fore.YELLOW + 'In the text: "" ' + Style.RESET_ALL) 
    sum_profit('', generator_numbers)
    print('')
    
    print(Fore.YELLOW + 'In the text: "text without numbers"' + Style.RESET_ALL)
    sum_profit('text without numbers', generator_numbers)
    
if __name__ == '__main__':
    main()