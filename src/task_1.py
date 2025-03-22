'''
    Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для 
    зберігання і повторного використання вже обчислених значень чисел Фібоначчі.  
'''
from colorama import Fore, Style

def caching_fibonacci() -> callable:
    '''
        Function to create and use cache for storing and reusing already calculated Fibonacci numbers.
        @return: function fibonacci(n: int) -> int, if error returns 0
    '''
    cache = {}
    
    def fibonacci(n: int) -> int:
        '''
            Function to calculate Fibonacci number.
            @param n: int
            @return: int
        '''
        
        if not isinstance(n, int):
            print(Fore.RED + "Input must be a positive integer." + Style.RESET_ALL)
            return 0
        if n < 0:
            print(Fore.RED + "Fibonacci number must be a positive integer." + Style.RESET_ALL)
            return 0
        
        
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache: 
            return cache[n]
        try:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        except RecursionError:
            print(Fore.RED + "Maximum recursion depth exceeded" + Style.RESET_ALL)
            return 0

        return cache[n]
    
    return fibonacci

def main():
    print(Fore.GREEN  + '=== TASK 1 ===' + Style.RESET_ALL)
    print('Fibonacci with caching')
    print('')
    
    fib = caching_fibonacci()
    
    print(Fore.CYAN + 'Fibonacci of 5: ',fib(5))
    print(Fore.CYAN + 'Fibonacci of 10: ',fib(10))
    print(Fore.CYAN + 'Fibonacci of 20: ',fib(20))
    print(Fore.CYAN + 'Fibonacci of -2: ',fib(-2))
    print(Fore.CYAN + 'Fibonacci of "a": ',fib('a'))
    print(Fore.CYAN + 'Fibonacci of 2000: ',fib(2000))
    
    print('')
    print(Fore.RED + '=== END TASK 1 ===' + Style.RESET_ALL)
    print('')
    
if __name__ == '__main__':
    main()