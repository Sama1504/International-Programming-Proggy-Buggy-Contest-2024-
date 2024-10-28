import sys
program_B = input().strip()


parameters = input().strip()


os_command = f'IF (true == A {program_B} {parameters}) THEN HANGS ELSE ENDS'


print(os_command)