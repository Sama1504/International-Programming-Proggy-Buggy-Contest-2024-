def sum_proper_divisors(n):
    
    
    divisor_sum = 1
    
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            
            if i != n // i:
                divisor_sum += n // i
                
    return divisor_sum

def find_amicable_pairs(A, B):
    
    pairs = []
    
    
    for i in range(A, B + 1):
        
        sum_i = sum_proper_divisors(i)
        
        if sum_i > i and sum_i <= B:
            
            sum_j = sum_proper_divisors(sum_i)
            
            
            if sum_j == i:
                pairs.append((i, sum_i))
    
    return pairs

def main():
    # Read input
    A, B = map(int, input().split())
    
    # Validate input
    if not (1 <= A <= B <= 10**6 and B - A <= 5*10**5):
        print("Invalid input")
        return
    
    
    pairs = find_amicable_pairs(A, B)
    
    
    if pairs:
        for pair in pairs:
            print(f"{pair[0]} {pair[1]}")
    else:
        print()

if __name__ == "__main__":
    main()