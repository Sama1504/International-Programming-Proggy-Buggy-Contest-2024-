import sys

def calculate_success_of_humanity():
    input = sys.stdin.read
    data = input().split()
    max_size = data[0]
    min_size = data[1]
    max_exponent = len(max_size) - 1
    min_exponent = -len(min_size) + 2
    success = max_exponent - min_exponent
    
    print(success)

calculate_success_of_humanity()