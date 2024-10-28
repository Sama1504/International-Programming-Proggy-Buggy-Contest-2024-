def solve_memory_puzzle(N):
    if not (2024 <= N <= 3024):
        return "Invalid catalogue number"
    stone_colors = 2 
    women = 500
    memorable_number = stone_colors * women
    return memorable_number
def main():
    N = int(input())
    result = solve_memory_puzzle(N)
    print(result)
if __name__ == "__main__":
    main()