def count_trailing_zeros_base12(n):

    count_2 = 0
    n2 = n
    while n2 > 0:
        n2 //= 2
        count_2 += n2
    
    
    count_3 = 0
    n3 = n
    while n3 > 0:
        n3 //= 3
        count_3 += n3
    
    
    return min(count_2, count_3)

def main():
    
    N = int(input())
    
    
    if not (1 <= N <= 10**9):
        print("Invalid input")
        return
    
    
    result = count_trailing_zeros_base12(N)
    print(result)

if __name__ == "__main__":
    main()