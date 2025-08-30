from pystyle import Colorate, Colors, Center
import os
import random
import string
import json
import sys
import requests
import os
from pystyle import Colorate, Colors, Center
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from hashlib import pbkdf2_hmac
from dns import resolver
from os import system
from tkinter import filedialog
from phonenumbers import geocoder, carrier, timezone
from concurrent.futures import ThreadPoolExecutor
from requests.exceptions import RequestException
from datetime import datetime
from urllib.parse import urljoin, urlparse
from PIL import Image
import phonenumbers
import json
import concurrent.futures
import dns.resolver
import os
import ssl
import sys
import bcrypt
import ctypes
import hashlib
import rarfile
import pyzipper
import base64
import contextlib
import fade
import tkinter
import instaloader
import hashlib
import random
import urllib3
import datetime
import string
import subprocess
import re
import webbrowser
import random
import time
import nmap
import aiohttp
import requests
import asyncio
import itertools
import phonenumbers
import time
import threading
import requests
import win32clipboard
import win32gui
from pynput import keyboard
from time import sleep
import instaloader
import sys
import os
import contextlib


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

banner = Colorate.Horizontal(Colors.green_to_yellow, '''

⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿      
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿    
⣿⣿⣿⣿⣿⣿⣿⣿⠏⣸⣿⣿⡿⢸⣿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿        
⣿⣿⣿⣿⣿⣿⣿⣿⡀⠹⣿⡏⠀⣾⣿⣶⣶⣶⣤⣉⠻⢿⣿⣿⣿⣿⣿⣿         ____  _____ _____   ________   __________  ____  __ 
⣿⣿⣿⣿⣿⣿⡟⢹⣷⣄⠈⠃⠀⠻⢋⣡⣤⣤⣉⠛⣷⣄⣿⣿⣿⣿⣿⣿        / __ \/ ___//  _/ | / /_  __/  /_  __/ __ \/ __ \/ /                
⣿⣿⣿⣿⣿⡿⢀⣿⣿⡇⣼⠖⠁⢠⣾⣿⣿⣿⣿⣧⠈⣿⣿⠙⣿⣿⣿⣿       / / / /\__ \ / //  |/ / / /      / / / / / / / / / /        
⣿⣿⣿⣿⣿⡇⢸⣿⣿⡅⠀⠀⠀⠘⣿⣿⣿⣿⣿⡿⢀⣿⣿⡄⣿⣿⣿⣿      / /_/ /___/ // // /|  / / /      / / / /_/ / /_/ / /_               
⣿⣿⣿⣿⣿⣇⠸⣿⣿⣏⣀⣠⡀⠀⠈⠛⠿⠿⠛⢡⣾⣿⣿⠀⣿⣿⣿⣿      \____//____/___/_/ |_/ /_/      /_/  \____/\____/_____/
⣿⣿⣿⣿⣿⣿⣄⠻⣿⣿⣿⣿⠇⠀⠈⠻⣶⣾⣷⠜⠻⣿⡏⣰⣿⣿⣿⣿          
⣿⣿⣿⣿⣿⣿⣿⣦⣹⡿⠟⠁⠀⠀⠀⠀⣹⣿⣿⣦⠀⠹⣷⣿⣿⣿⣿⣿        ╔═════════════════════════════════════════════════════════════════════════════════╗
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⣀⠀⠀⠀⢀⣴⡿⠟⠛⣿⣧⠀⠘⢿⣿⣿⣿⣿        ║                       OSINT TOOL  BY S3xon_VIRUS                                      ║
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣾⣿⣶⣾⣿⣿⣿⣧⣤⣾⣿⣿⣿⣿        ║═════════════════════════════════════════════════════════════════════════════════║
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿        ║                                                                                 ║
                                    ║    [01]- Ip Lookup                        [07]-                                 ║
                                    ║    [02]- Phone Lookup                     [08]-                                 ║
                                    ║    [03]- DNS Lookup                       [09]-                                 ║
                                    ║    [04]- Google Dork                      [10]-                                 ║
                                    ║    [05]- Email Lookup                     [11]-                                 ║
                                    ║    [06]- GitHub Lookup                    [12]-                                 ║
                                    ║    [06]- Instagram Lookup                 [13]-                                 ║
                                    ║                                                                                 ║
                                    ╚═════════════════════════════════════════════════════════════════════════════════╝
                                 
''')

menu_text = Colorate.Horizontal(Colors.black_to_white, '''

''')

def show_tool_options():
    print(Colorate.Horizontal(Colors.black_to_white, '''


'''))

def main():
    while True:
        clear_screen()
        print(banner)
        print(menu_text)
        show_tool_options()
        select = input(Colorate.Horizontal(Colors.green_to_blue, "\nChoice: ")).strip()
        
        if select == "1":
            ip_geolocation_lookup()
        elif select == "0":
            print("Chiusura...")
            break
        if select == "2":
            phone()                  
        if select == "3":
            dnsscan()  
        if select == "4":
            dork()      
        if select == "5":
            emailook()         
        if select == "6":
            githubemail()     
        if select == "7":
            instagram()              

        else:
            print("Scelta non valida.")


def ip_geolocation_lookup():



    header = '''
                                      :**+ :::+*@@.                                                         
                              +: @ = =.  :#@@@@@@@@                 :     .=*@@#     -                      
                 @@@@-. :=: +@@.:% *=@@:   @@@@@@          :#=::     .:@=@@@@@@@@@@@@@@@@@@@@--.-:          
             .#@@@@@@@@@@@@@@@@@@:# .@@   #@@    :@-     +@@:@@@+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*        
             #*   :%@@@@@@@@@@:   .@@#*              ..  ##@ *#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-:- %=         
                   *@@@@@@@@@@@@%@@@@@@@            = @=+@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@+   #.        
                   #@@@@@@@@@##@@@@@= =#              #@@@#@@@@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=            
                  @@@@@@@@@@@#+#@@=                 :@@@-.#-*#@.  .@@.=%@@@@%@@@@@@@@@@@@@@@@@=  +          
                 :@@@@@@@@@@@@@@:                   :@@    # - @@@@@@@ =@@@*#*@@@@@@@@@@@@@=.=-  #:         
                  :@@@@@@@@@@@+                     @@@@@@@: :    @@@@@@@@@@@@@@@@@@@@@@@@@@@               
                   #@@@@@    @                     #%@@@@@@@@@@@@@@@@@:@@@@@@@@@@@@#@@@@@@@@@:              
                     @@@     .                    @@@@@@@@@@@@@@@@-%@@@%@#   @@@@@@#=@#@@@@@==              
                     =@@##@   =:*.                @@@@@@*@@@@@@@@@@-=@@@@.    +@@@:  %#@@#=   :             
                         .=@.                     #@@@@@@@@#@@@@@@@@+#:        %@      *%@=                 
                            . @@@@@@               @#@@*@@@@@@@@@@@@@@@=        :-     -       =.           
                             :@@@@@@@#=                   @@@@@@@@@@@@-               :+%  .@=              
                            -@@@@@@@@@@@@                 @+@@@@*+@@#                   @. @@.#   # :       
                             @@@@@@@@@@@@@@@               @@@@@*@@@                     :=.        @@@.    
                              @@@@@@@@@@@@@                #@@@@@@%@.                             :  :      
                               *@@@@@@@@@@%               :@@@@@@@@@ @@.                      .@@@@=:@      
                                :@@@@@@@@@                 #@@@@@@   @:                    .#@@@@@@@@@@     
                                :@@@@%@@                   .@@@@@-   .                     @@@@@@@@@@@@*    
                                :@@@@@@.                    *@@@-                          @@@@#@@@@@@@     
                                .@@@@@                                                           =@@@:    @=
                                 =@@                                                              =    #+   
                                  @%       
                                                                                 
    '''
    print(Colorate.Horizontal(Colors.green_to_white, header))
    
    prompt = Colorate.Horizontal(Colors.green_to_white, "Enter the IP address: ")
    ip_address = input(prompt).strip()
    if not ip_address:
        ip_address = requests.get('https://api.ipify.org').text
    
    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        response.raise_for_status()
        data = response.json()
        
        info = f'''
╔══════════════════════════════════════════════════════════╗
║ IP Address: {data.get('ip', 'N/A'):<45}║
║ Hostname: {data.get('hostname', 'N/A'):<46} ║
║ City: {data.get('city', 'N/A'):<50} ║
║ Region: {data.get('region', 'N/A'):<48} ║
║ Country: {data.get('country', 'N/A'):<47} ║
║ Location: {data.get('loc', 'N/A'):<46} ║
╚══════════════════════════════════════════════════════════╝
        '''
        colored_info = Colorate.Horizontal(Colors.green_to_white, info)
        print(colored_info)
    except requests.RequestException as e:
        print(Colorate.Horizontal(Colors.red_to_white, f"Error: {str(e)}"))
    input("\nPress Enter to return to the main menu...")

from colorama import Fore, Style, init
init(autoreset=True)

def phone():
    def clear():
        import os
        os.system('cls' if os.name == 'nt' else 'clear')

    def Slow(text):
        print(text)

    def Continue():
        input("Premi invio per continuare...")

    def Reset():
        clear()

    def Title(title):
        clear()
        print(f"{Fore.GREEN}=== {title} ==={Style.RESET_ALL}")

    def ErrorModule(e):
        print(f"{Fore.GREEN}Errore modulo: {e}{Style.RESET_ALL}")

    def Error(e):
        print(f"{Fore.GREEN}Errore: {e}{Style.RESET_ALL}")

    white = Fore.WHITE
    red = Fore.RED
    INFO_ADD = "[INFO]"
    INPUT = "[INPUT]"
    WAIT = "[WAIT]"
    INFO = "[INFO]"


    Title("}---------------------------------------Phone Number Lookup---------------------------------")

    try:
        phone_number = input(f"\n{INPUT} enter number for lookup -> {Style.RESET_ALL}")
        print(f"{WAIT} Recupero informazioni...")

        try:
            parsed_number = phonenumbers.parse(phone_number, None)
            status = "Valid" if phonenumbers.is_valid_number(parsed_number) else "Invalid"

            country_code = "+" + phone_number[1:3] if phone_number.startswith("+") else "None"

            operator = carrier.name_for_number(parsed_number, "en") or "None"

            type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixe"

            timezones = timezone.time_zones_for_number(parsed_number)
            timezone_info = timezones[0] if timezones else "None"

            country = phonenumbers.region_code_for_number(parsed_number) or "None"

            region = geocoder.description_for_number(parsed_number, "en") or "None"

            formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL) or "None"

            Slow(f"""
{Fore.RED}───────────────────────────────────────────────
 {INFO_ADD} {Fore.GREEN}Phone        : {white}{phone_number}{red}
 {INFO_ADD} {Fore.GREEN}Formatted    : {white}{formatted_number}{red}
 {INFO_ADD} {Fore.GREEN}Status       : {white}{status}{red}
 {INFO_ADD} {Fore.GREEN}Country Code : {white}{country_code}{red}
 {INFO_ADD} {Fore.GREEN}Country      : {white}{country}{red}
 {INFO_ADD} {Fore.GREEN}Region       : {white}{region}{red}
 {INFO_ADD} {Fore.GREEN}Timezone     : {white}{timezone_info}{red}
 {INFO_ADD} {Fore.GREEN}Operator     : {white}{operator}{red}
 {INFO_ADD} {Fore.GREEN}Type Number  : {white}{type_number}{red}
{white}───────────────────────────────────────────────
""")
            Continue()
            Reset()

        except Exception:
            print(f"{INFO} Formato non valido!")
            Continue()
            Reset()

    except Exception as e:
        Error(e)

def dnsscan():
    init(autoreset=True)


    ascii_art = '''
██▄      ▄      ▄▄▄▄▄       █    ████▄ ████▄ █  █▀  ▄   █ ▄▄  
█  █      █    █     ▀▄     █    █   █ █   █ █▄█     █  █   █ 
█   █ ██   █ ▄  ▀▀▀▀▄       █    █   █ █   █ █▀▄  █   █ █▀▀▀  
█  █  █ █  █  ▀▄▄▄▄▀        ███▄ ▀████ ▀████ █  █ █   █ █     
███▀  █  █ █                    ▀              █  █▄ ▄█  █    
      █   ██                                  ▀    ▀▀▀    ▀   
    '''
    print(Colorate.Vertical(Colors.green_to_white, Center.XCenter(ascii_art)))
    
    choice = input(Fore.GREEN + "\n🔍 Inserisci il dominio da scansionare: ")
    api = f"https://api.hackertarget.com/dnslookup/?q={choice}"

    try:
        res = requests.get(api, timeout=10)
        results = res.text
        print(Fore.LIGHTWHITE_EX + "\n🧾 Risultati DNS:\n")
        print(results)
    except Exception as e:
        print(Fore.RED + f"\n❌ Errore durante la richiesta: {e}")

    input(Fore.YELLOW + "\nPremi INVIO per continuare...")
   


def dork():
    init(autoreset=True)


    import os
    import time
    import webbrowser
    import datetime

 
    white = '\033[97m'
    GREEN = '\033[92m'
    reset = '\033[0m'


    BEFORE = f"{GREEN}["
    AFTER = f"{GREEN}]"
    INFO = f"{white}INFO{reset}"
    INPUT = f"{white}INPUT{reset}"
    WAIT = f"{white}WAIT{reset}"


    banner = f"""{GREEN}
                                                                       ..                                   
                                                                     .:@ :...                               
                .:::::::::::::::::::::::::::::::::.             ....-@@@+..                                 
               .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.           .-@@@@@-.                                    
               :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.          .=@@@@-.                                      
               :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.          -@@@@-.                                       
               :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.      @@ :@@#:.                                         
               :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.       %  @%+:                                          
                ::::::::-*@@@@@@@@@@@@@@@*-::::::::        @@ #:@@@                           ..::::::::    
                         -@@@@@@@@@@@@@@@=                 @@ @+@@@@                      .::+@@@@@@@@@@:   
                         -@@@@@@@@@@@@@@@                @@@  @+@%%@@                    -*@@@@@@@@@@@@@:   
                         :@@@@@@@@@@@@@@@            @@@@    @@+.@@=:@@@@              :*@@@@@@@@@@@@@@@:   
                         :@@@@@@@@@@@@@@@          @@@    ..@:@@+ @@%=-:=@@@          :*@@@@@@@@@@@@@@@@:   
                         :@@@@@@@@@@@@@@@       @@@    .-@@@::@#@# @@#@%*-:@@@       .*@@@@@@@@@@@@@@@@@:   
                         :@@@@@@@@@@@@@@@     @@@   ..@@@+:--=@#.@% @#%@@@#=:@@      *@@@@@@@@@@@@@*-::.    
                         :@@@@@@@@@@@@@@@    @@@  :.@@..-++=@@@@. @ =@+@@@@@#:@@@   -@@@@@@@@@@@@@*:        
                         :@@@@@@@@@@@@@@@    @@  :*@.:-=-+@@%-@@@# @ @:@@@@@@#:@@   -@@@@@@@@@@@@@-         
                         :@@@@@@@@@@@@@@@    @@ .-@ -+=@@@=++=@.-@ @ @-@@@@@@@-@@@  -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@    @@ .@@ *@@@:*%=.@@@ @-@ @-%@@@@@@-@@@  -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@    @@   @ :@@.%@+-@ *@@ @@ @-@@@@@@#.@@   -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@     @@  @@ @@ %@.@ :@@@ @@@@-@@@@@*:@@@   -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@      @@   @ @-.* @ -%@@-@ @@*@@@#=:@@     -@@@@@@@@@@@@@.         
                         :@@@@@@@@@@@@@@@       @@@  -@@@  @@ .%* #@@-%#=:-@@@      -@@@@@@@@@@@@@.         
                         -@@@@@@@@@@@@@@%         @@@@   @.  @ =*@@@...-@@@@        -@@@@@@@@@@@@@.         
                          .:::::::::::::.             @@@@@@@@@@@@-*@@@@             ::::::::::::.  
    {reset}
    """
    print(Colorate.Vertical(Colors.green_to_white, Center.XCenter(banner)))

    def current_time_hour():
        return datetime.datetime.now().strftime('%H:%M:%S')


    def Continue():
        input(f"\n{BEFORE + current_time_hour() + AFTER} {INPUT} Press ENTER to return...")

    def Slow(text):
        print(text)
        time.sleep(0.5)

    def ErrorModule(e):
        print(f"{BEFORE + current_time_hour() + AFTER} {red}MODULE ERROR: {e}{reset}")
        input("Press ENTER to exit...")
        exit()

    def Error(e):
        print(f"{BEFORE + current_time_hour() + AFTER} {red}ERROR: {e}{reset}")
        input("Press ENTER to exit...")
        exit()

    try:
        url = "https://www.google.com/search?q="
        database = []

        def AddDataBase(request):
            database.append(request)
            print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Query added: {white}{request}{reset}")

        Slow(f"""
 {BEFORE}00{AFTER} Start search
 {BEFORE}01{AFTER}{white} Keyword in the URL of a website
 {BEFORE}02{AFTER}{white} Keyword in the title of a website
 {BEFORE}03{AFTER}{white} Specific website domain
 {BEFORE}04{AFTER}{white} Keyword in page content
 {BEFORE}05{AFTER}{white} Exclude keyword from pages
 {BEFORE}06{AFTER}{white} File extension (e.g., pdf, txt)
        """)

        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} You can choose multiple options. Enter '0' to launch the search.")

        while True:
            choice = input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Choose option -> {reset}")

            if choice in ['0', '00']:
                break
            elif choice in ['1', '01']:
                request = "inurl:" + input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter keyword for URL -> {reset}")
                AddDataBase(request)
            elif choice in ['2', '02']:
                request = "intitle:" + input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter keyword for title -> {reset}")
                AddDataBase(request)
            elif choice in ['3', '03']:
                request = "site:" + input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter domain (e.g., example.com) -> {reset}")
                AddDataBase(request)
            elif choice in ['4', '04']:
                request = '"' + input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter keyword in content -> {reset}") + '"'
                AddDataBase(request)
            elif choice in ['5', '05']:
                request = "-" + input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter keyword to exclude -> {reset}")
                AddDataBase(request)
            elif choice in ['6', '06']:
                request = "filetype:" + input(f"{BEFORE + current_time_hour() + AFTER} {INPUT} Enter file extension -> {reset}")
                AddDataBase(request)

        total_request = " ".join(database)
        full_url = url + total_request.replace(" ", "%20").replace("\"", "%22")

        print(f"\n{BEFORE + current_time_hour() + AFTER} {INFO} Final Search Query: {white}{total_request}{reset}")
        webbrowser.open(full_url)

        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} Google search launched in your browser.")
        Continue()

    except Exception as e:
        Error(e)


def emailook():
    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_red_to_white(text):
       
        colors = ["\033[32m", "\033[92m", "\033[92m"]
        lines = text.splitlines()
        n = len(lines)
        for i, line in enumerate(lines):
            color = colors[min(i * len(colors) // n, len(colors)-1)]
            print(f"{color}{line}\033[0m")

    def GetEmailInfo(email):
        info = {}
        try:
            domain_all = email.split('@')[-1]
        except:
            domain_all = None
        try:
            name = email.split('@')[0]
        except:
            name = None
        try:
            domain = re.search(r"@([^@.]+)\.", email).group(1)
        except:
            domain = None
        try:
            tld = f".{email.split('.')[-1]}"
        except:
            tld = None
        try:
            mx_records = dns.resolver.resolve(domain_all, 'MX')
            mx_servers = [str(record.exchange) for record in mx_records]
            info["mx_servers"] = mx_servers
        except:
            info["mx_servers"] = None
        try:
            spf_records = dns.resolver.resolve(domain_all, 'SPF')
            info["spf_records"] = [str(record) for record in spf_records]
        except:
            info["spf_records"] = None
        try:
            dmarc_records = dns.resolver.resolve(f'_dmarc.{domain_all}', 'TXT')
            info["dmarc_records"] = [str(record) for record in dmarc_records]
        except:
            info["dmarc_records"] = None
        if info.get("mx_servers"):
            for server in info["mx_servers"]:
                if "google.com" in server:
                    info["google_workspace"] = True
                elif "outlook.com" in server:
                    info["microsoft_365"] = True
        return info, domain_all, domain, tld, name

    clear()

    titolo = """
                                          ...:----:...                                              
                                     .:=#@@@@@@@@@@@@@@%*-..                                        
                                  .:#@@@@@@@%#*****#%@@@@@@@+..                                     
                               ..-@@@@@%-...... ........+@@@@@@..                                   
                               :%@@@@=..   .#@@@@@@@@#=....+@@@@*.                                  
                             .+@@@@=.      .*@@@%@@@@@@@@=...*@@@@:.                                
                            .#@@@%.                 .=@@@@@=. .@@@@-.                               
                           .=@@@#.                    .:%@@@*. -@@@%:.                              
                           .%@@@-                       .*@@*. .+@@@=.                              
                           :@@@#.                              .-@@@#.                              
                           -@@@#                                :%@@@.                              
                           :@@@#.                              .-@@@#.                              
                           .%@@@-.                             .+@@@=.                              
                           .+@@@#.                             -@@@%:.                              
                            .*@@@%.                          .:@@@@-.                               
                             .+@@@@=..                     ..*@@@@:.                                
                               :%@@@@-..                ...+@@@@*.                                  
                               ..-@@@@@%=...         ...*@@@@@@@@#.                                 
                                  .:*@@@@@@@%*++++**@@@@@@@@=:*@@@@#:.                              
                                     ..=%@@@@@@@@@@@@@@%#-.   ..*@@@@%:.                            
                                        .....:::::::....       ...+@@@@%:                           
                                                                  ..+@@@@%-.                        
                                                                    ..=@@@@%-.                      
                                                                      ..=@@@@@=.                    
                                                                         .=%@@@@=.                  
                                                                          ..-%@@@-.                 
                                                                             ....
    """
    print_red_to_white(titolo)

    email = input("Inserisci email: ").strip()
    print("Recupero informazioni...\n")

    try:
        info, domain_all, domain, tld, name = GetEmailInfo(email)

        print("════════════════ RISULTATI ════════════════")
        print(f"Email        : {email}")
        print(f"Nome         : {name}")
        print(f"Dominio      : {domain}")
        print(f"TLD          : {tld}")
        print(f"Dominio Full : {domain_all}")
        print(f"MX Servers   : {' / '.join(info['mx_servers']) if info['mx_servers'] else 'N/A'}")
        print(f"SPF Records  : {info['spf_records'] if info['spf_records'] else 'N/A'}")
        print(f"DMARC        : {' / '.join(info['dmarc_records']) if info['dmarc_records'] else 'N/A'}")
        print(f"Google WS    : {info.get('google_workspace', False)}")
        print(f"Microsoft 365: {info.get('microsoft_365', False)}")
        print("═══════════════════════════════════════════")

    except Exception as e:
        print(f"[Errore] {str(e)}")

    input("\nPremi INVIO per uscire...")

def githubemail():
    init(autoreset=True)


    ascii_art = """
                                                       j@@@@@^                                 
                           _@v   p@@@@j           j@@@@@@@@@@@@@@@;          |@@@@M   v@}      
                          @@@@@} >@@@@    v@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@p    @@@@_ _@@@@@     
                          >@@@v    @@     v@@@@@@@@@@@@      p@@@@@@@@@@@a     @@    j@@@_     
                           ^@@     @@@@   |@@@@@@@@@@^ @@@@@@; @@@@@@@@@@p   p@@@     M@;      
                           ^@@            >@@@@@@@@@@ p@@@@@@@ M@@@@@@@@@j            M@;      
                           ^@@@@@@@@@@@}   @@@@@@@@|            >@@@@@@@@;   @@@@@@@@@@@;      
                                           }@@@@@@@|    O@@@    >@@@@@@@M                      
                          |@@@@             @@@@@@@|     M@     >@@@@@@@^            @@@@j     
                          @@@@@@@@@@@@@@@>   @@@@@@|    O@@@    >@@@@@@    @@@@@@@@@@@@@@@     
                            ^                 @@@@@v            }@@@@@^                ^       
                                 p@@@@@@@@@^   M@@@@@@@@@@@@@@@@@@@@@    @@@@@@@@@p            
                                 p@_            ^@@@@@@@@@@@@@@@@@@>            >@a            
                                @@@@O              @@@@@@@@@@@@@@              J@@@@           
                               ;@@@@@                 J@@@@@@p                 @@@@@>          
                                  ;              p@              p@>  M@@_       ;             
                                          @@@@p  p@_  ;      j_  a@@@@@@@@j                    
                                         ^@@@@@@@@@   v@_   O@}       M@@_                     
                                            ;         p@|   O@}      }}                        
                                                    >@@@@@  O@@@@@@@@@@@J                      
                                                     p@@@j         ;@@@@^    


                                           ╔═╗╔╦╗╔═╗╦╦    ╔═╗╦ ╦╦  ╦ 
                                           ║╣ ║║║╠═╣║║    ╠═╝║ ║║  ║ 
                                           ╚═╝╩ ╩╩ ╩╩╩═╝  ╩  ╚═╝╩═╝╩═╝    
                                        ╭─────────────────────────────────╮     
                                        │  rat account git hub pull email │
                                        ╰─────────────────────────────────╯  
"""

    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Vertical(Colors.green_to_white, Center.XCenter(ascii_art)))

    Username = input(Fore.LIGHTYELLOW_EX + "Inserisci il nome utente GitHub --> ")
    repos = input(Fore.LIGHTYELLOW_EX + "Inserisci il nome del repository --> ")

    try:
        res = requests.get(f"https://api.github.com/repos/{Username}/{repos}/commits")
        data = res.json()

        first_commit = data[0]
        author = first_commit.get('commit', {}).get('author', {})
        Email = author.get('email', 'N/A')
        User = author.get('name', 'N/A')

        print(f"""
+----+------------------+------------------------+
| ID | Username         | Email                  | 
+----+------------------+------------------------+ 
| 1  | {User}           | {Email}                |
+----+------------------+------------------------+
        """)

    except Exception as e:
        print(Fore.RED + f"[ERRORE] {e}")

    input(Fore.WHITE + "Premi Invio per tornare al menu...")
   

def instagram():



    init(autoreset=True)
    os.system('cls' if os.name == 'nt' else 'clear')

    banner = ''' 
                             ──▄█████████████████████████▄──                        
                              ▄█▀░█░█░█░░░░░░░░░░░░░░░░░░░▀█▄
                              █░░░█░█░█░░░░░░░░░░░░░░█████░░█
                              █░░░█░█░█░░░░░░░░░░░░░░█████░░█
                              █░░░█░█░█░░░░░░░░░░░░░░█████░░█                              ╭────────────────────╮
                              █░░░░░░░░░▄▄▄█████▄▄▄░░░░░░░░░█                              │       FOLLOWERS     │
                              ███████████▀▀░░░░░▀▀███████████                              │       PHOTO         │
                              █░░░░░░░██░░▄█████▄░░██░░░░░░░█                              │       FULL NAME     │
                              █░░░░░░░██░██▀░░░▀██░██░░░░░░░█                              ╰────────────────────╯ 
                              █░░░░░░░██░██░░░░░██░██░░░░░░░█
                              █░░░░░░░██░██▄░░░▄██░██░░░░░░░█
                              █░░░░░░░██▄░▀█████▀░▄██░░░░░░░█
                              █░░░░░░░░▀██▄▄░░░▄▄██▀░░░░░░░░█
                              █░░░░░░░░░░▀▀█████▀▀░░░░░░░░░░█
                              █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
                              █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
                              █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░█
                              ▀█▄░░░░░░░░░░░░░░░░░░░░░░░░░▄█▀
                              ──▀█████████████████████████▀──
                       
                             ╦╔╗╔╔═╗╔╦╗╔═╗╔═╗╦═╗╔═╗╔╦╗  ╔╦╗╦═╗╔═╗╔═╗╦╔═╔═╗╦═╗
                             ║║║║╚═╗ ║ ╠═╣║ ╦╠╦╝╠═╣║║║   ║ ╠╦╝╠═╣║  ╠╩╗║╣ ╠╦╝
                             ╩╝╚╝╚═╝ ╩ ╩ ╩╚═╝╩╚═╩ ╩╩ ╩   ╩ ╩╚═╩ ╩╚═╝╩ ╩╚═╝╩╚═
    '''
    print(Colorate.Vertical(Colors.green_to_white, Center.XCenter(banner)))

    def search_profile(username):
        @contextlib.contextmanager
        def suppress_output():
            with open(os.devnull, 'w') as devnull:
                old_stdout = sys.stdout
                old_stderr = sys.stderr
                sys.stdout = devnull
                sys.stderr = devnull
                try:
                    yield
                finally:
                    sys.stdout = old_stdout
                    sys.stderr = old_stderr

        with suppress_output():
            loader = instaloader.Instaloader()
            profile = instaloader.Profile.from_username(loader.context, username)
        return loader, profile

    try:
        username = input("👤 Enter Instagram username: ").strip()

        if not username:
            print("[!] You must enter a username.")
            input("Press ENTER to exit...")
            return

        loader, profile = search_profile(username)

        print(f"""
────────────────────────────────────────────────────────────
[+] Full Name        : {profile.full_name}
[+] Username         : {profile.username}
[+] Instagram ID     : {profile.userid}
[+] Bio              : {profile.biography}
[+] Profile URL      : https://instagram.com/{profile.username}
[+] Profile Picture  : {profile.profile_pic_url}
[+] Total Posts      : {profile.mediacount}
[+] Followers        : {profile.followers}
[+] Following        : {profile.followees}
[+] Verified         : {"✅ Yes" if profile.is_verified else "❌ No"}
[+] Private          : {"🔒 Yes" if profile.is_private else "🔓 No"}
[+] Business Account : {"🏢 Yes" if profile.is_business_account else "No"}
""")

        if profile.is_business_account:
            print(f"[+] Business Category : {profile.business_category_name}")

        print("────────────────────────────────────────────────────────────")

        if not profile.is_private:
            print("📸 Recent posts:")
            for i, post in enumerate(profile.get_posts()):
                print(f"""
--- Post #{i+1} ---
📎 URL      : https://www.instagram.com/p/{post.shortcode}/
📅 Date     : {post.date}
❤️ Likes    : {post.likes}
💬 Comments : {post.comments}
📝 Caption  : {post.caption[:100] if post.caption else 'None'}""")
                if i == 4:
                    break
        else:
            print("🔒 This account is private. Posts are not visible.")

    except Exception as e:
        print(f"[!] Error: {e}")
        import traceback
        traceback.print_exc()

    input("\nPress ENTER to exit...")  



if __name__ == "__main__":
    main()
