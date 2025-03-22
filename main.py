import src.task_1 as task_1
import src.task_2 as task_2
import src.task_3 as task_3
import src.task_4 as task_4
from colorama import Fore, Style

def main():
    task_1.main()
    task_2.main()
    task_3.main()
    
    print('')
    print(Fore.GREEN + '=== TASK 4 ===' + Style.RESET_ALL)
    print('')
    
    task_4.main()
    
    print('')
    print(Fore.RED + '=== END TASK 4 ===' + Style.RESET_ALL)
    print('')

if __name__ == '__main__':
    main()