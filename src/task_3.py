'''
    Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти 
    читати лог-файл, переданий як аргумент командного рядка, і виводити статистику 
    за рівнями логування наприклад, INFO, ERROR, DEBUG. Також користувач може 
    вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня.
'''

from colorama import Fore, Style, Back
import sys
from pathlib import Path
from datetime import datetime as dtdt
from collections import Counter


def parse_log_line(log_line: str) -> dict:
    '''
        Parse log line and return dictionary with log level and message
        @param log_line: str
        @return dict: {'date': str, 'time': str, 'level': str, 'message': str}
    '''
    
    result = {
        'date': None,
        'time': None,
        'level': None,
        'message': None
    }
    
    try:
        date_str, time_str, level, message = log_line.split(' ', 3)
        
        result['date'] = dtdt.strptime(date_str, '%Y-%m-%d').date()
        result['time'] = dtdt.strptime(time_str, '%H:%M:%S').time()
        result['level'] = level.strip()
        result['message'] = message.strip()
    
    except ValueError as e:
        print(Fore.RED + f"Error parsing log line: {e}. Line: {log_line.strip()}" + Style.RESET_ALL)
    
    return result

def load_logs(file_path: str) -> list:
    '''
        Load logs from file
        @param file_path: str
        @return list: list of log lines
    '''
    result = []
    
    try:
        with open(file_path, 'r') as file:
            for line in file:
                result.append(parse_log_line(line))
    except (FileNotFoundError, PermissionError) as e:
        print(Fore.RED + f"Error opening file: {e}" + Style.RESET_ALL)
        sys.exit(1)
    
    return result

def filter_logs_by_level(logs: list, level: str) -> list:
    '''
        Filter logs by level
        @param logs: list
        @param level: str
        @return list: list of log lines
    '''
    result = []
    for logs in logs:
        if logs['level'] == level:
            log_str = f"{logs['date']} {logs['time']} - {logs['message']}"
            result.append(log_str)
    return result

def count_logs_by_level(logs: list) -> dict:
    '''
        Count logs by level
        @param logs: list
        @return dict: dictionary with log levels and their counts
    '''
    return Counter([log['level'] for log in logs])

def display_log_counts(counts: dict):
    '''
        Display log counts in readable format
        @param counts: dict
    '''
    if counts == {}:
        print(Fore.RED + 'No logs found' + Style.RESET_ALL)
        return
    
    print('')
    print(Back.CYAN + '=====================' + Style.RESET_ALL)
    print(Fore.GREEN + "Level     " + Fore.WHITE + "|" + Fore.GREEN +  " Quantity " + Style.RESET_ALL)
    print("-" * 10 + "|" + "-" * 10)
    
    for level, count in sorted(counts.items()):
        color = Fore.CYAN
        
        if level == 'ERROR':
            color = Fore.RED
        elif level == 'INFO':
            color = Fore.BLUE
        elif level == 'WARNING':
            color = Fore.YELLOW
            
        print(color + f"{level.ljust(9)} " + Fore.WHITE + "|" + color + f" {str(count).ljust(9)}")
    print(Back.CYAN + '=====================' + Style.RESET_ALL)
    print('')

def main():
    '''
        Main function to log file and display log counts
    '''
    
    file_path = Path(sys.argv[1])
    level_input = sys.argv[2] if len(sys.argv) > 2 else None
    level = level_input.upper() if level_input else None
    
    try:
        file_path = file_path.resolve()
        if not file_path.exists():
            print(Fore.RED + f"Error: The file '{file_path}' does not exist." + Style.RESET_ALL)
            sys.exit(1)
            
        all_logs = load_logs(file_path) # returns list of log lines as dictionaries
        level_count = count_logs_by_level(all_logs) # returns dict with log levels and their counts
        display_log_counts(level_count) # display log counts in readable format
        
        if level:
            if level not in level_count:
                print(f"No logs found with level " + Back.CYAN + f"{level}:")
            else:
                print(f"Logs with level " + Back.GREEN + f"{level}:" + Style.RESET_ALL)
                print('-' * 30)
                for log in filter_logs_by_level(all_logs, level):
                    print(log)
        
    except IndexError:
        print(Fore.RED + 'Please provide log file path as argument' + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)
       
if __name__ == '__main__':
    main()