import sys

def find_smallest_unrepresentable_sum(N, numbers):
    
    numbers.sort()
    
    
    smallest_unrepresentable_sum = 1
    
    
    for num in numbers:
        
        if num > smallest_unrepresentable_sum:
            break
        
        smallest_unrepresentable_sum += num
    
    return smallest_unrepresentable_sum

def main():
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    numbers = list(map(int, data[1:N+1]))
    
    result = find_smallest_unrepresentable_sum(N, numbers)
    print(result)

if __name__ == "__main__":
    main()