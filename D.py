def is_plagiarism(proggy_line, buggy_line):
    
    if len(proggy_line) != len(buggy_line):
        return False
    proggy_freq = {}
    buggy_freq = {}
    
    for char in proggy_line:
        proggy_freq[char] = proggy_freq.get(char, 0) + 1
        
    for char in buggy_line:
        buggy_freq[char] = buggy_freq.get(char, 0) + 1
    
    return proggy_freq == buggy_freq

def main():
    
    proggy_line = input().rstrip()
    buggy_line = input().rstrip()
    
    if len(proggy_line) > 1000000 or len(buggy_line) > 1000000:
        return "Invalid input: String too long"

    result = "PLAGIARISM" if is_plagiarism(proggy_line, buggy_line) else "AUTHENTIC"
    print(result)

if __name__ == "__main__":
    main()