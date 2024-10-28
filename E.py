def calculate_painted_area(shots):

    painted_points = set()
    
    for T, L, B, R in shots:
        
        for y in range(B, T + 1):
            for x in range(L, R + 1):
                painted_points.add((x, y))
    
    
    return len(painted_points)

def main():
    
    N = int(input())
    
    
    if N < 0:
        print("Invalid input: N must be non-negative")
        return
    
    
    shots = []
    for _ in range(N):
        T, L, B, R = map(int, input().split())
        
        
        if not (0 <= T <= 1000 and 0 <= L <= 1000 and 
                0 <= B <= 1000 and 0 <= R <= 1000):
            print("Invalid input: Coordinates must be between 0 and 1000")
            return
        
        if not (B <= T and L <= R):
            print("Invalid input: Invalid rectangle coordinates")
            return
            
        shots.append((T, L, B, R))
    
    result = calculate_painted_area(shots)
    print(result)

if __name__ == "__main__":
    main()