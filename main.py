import src.task_1 as task_1
import src.task_2 as task_2
import src.task_3 as task_3
import src.task_4 as task_4
from colorama import Fore, Style

def main():
    print('')
    print(Fore.GREEN + '=== TASK 1 ===' + Style.RESET_ALL)
    print('')
    
    task_1.main()
    
    print('')
    print(Fore.RED + '=== END TASK 1 ===' + Style.RESET_ALL)
    print('')
    
    print('')
    print(Fore.GREEN + '=== TASK 2 ===' + Style.RESET_ALL)
    print('')
    
    task_2.main()
    
    print('')
    print(Fore.RED + '=== END TASK 2 ===' + Style.RESET_ALL)
    print('')
    
    print('')
    print(Fore.GREEN + '=== TASK 3 ===' + Style.RESET_ALL)
    print('')
    
    print('To test task 3, please run the following command:')
    print('python src/task_3.py src/files/logs.txt debug')
    
    print('')
    print(Fore.RED + '=== END TASK 3 ===' + Style.RESET_ALL)
    print('')
    
    
    print('')
    print(Fore.GREEN + '=== TASK 4 ===' + Style.RESET_ALL)
    print('')
    
    task_4.main()
    
    print('')
    print(Fore.RED + '=== END TASK 4 ===' + Style.RESET_ALL)
    print('')

if __name__ == '__main__':
    main()