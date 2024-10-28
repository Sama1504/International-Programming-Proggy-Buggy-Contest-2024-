import math
def square_to_circle_radius(A):
    square_area = A * A
    R = math.sqrt(square_area / math.pi)
    return R
def main():
    A = int(input())
    if 0 < A < 10**4:
        result = square_to_circle_radius(A)
        print(result)
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()