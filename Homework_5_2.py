
import re
from typing import Callable

def generator_numbers(text: str):
    pattern = r' [+-]?\d*\.?\d+ '  
    for match in re.findall(pattern, text):
        yield float(match)  

def sum_profit(text, func: Callable):
    return sum(func(text))  

# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")