import requests
import time
from colorama import init, Fore, Style
from termcolor import colored
from data.handler import servers

init()

green = Fore.GREEN
blue = Fore.BLUE
red = Fore.RED
yellow = Fore.YELLOW
reset = Style.RESET_ALL

def check_url(token, server_id, url):
    headers = {"Authorization": token}
    
    while True:
        response = requests.get(f"https://discord.com/api/v9/invites/{url}?with_counts=true&with_expiration=true", headers=headers)
        
        if response.status_code == 200:
            print(colored(f"URL mevcut sunucuda: {url}", 'yellow'))
        else:
            print(colored(f"URL sunucuda bulunmuyor: {url}", 'red')) 
            print(colored("Eski URL geri yüklendi.", 'green')) 
            restore_url(token, server_id, url)
        
        time.sleep(1)

def restore_url(token, server_id, url): 
    headers = {"Authorization": token}
    data = {"code": url}
    response = requests.patch(f"https://discord.com/api/v9/guilds/{server_id}/vanity-url", headers=headers, json=data)
    if response.status_code == 200:
        print(colored(f"Eski URL başarıyla geri yüklendi: {url}", 'green'))
    else:
        print(colored(f"Malesef Eski URL geri yüklenemedi: {url}", 'red'))

def main():
    token = input(colored("Token'i girin: ", 'blue'))
    servers(token)
    server_id = input(colored("Sunucu ID'sini girin: ", 'blue'))
    url = input(colored("Kontrol edilecek URL'yi girin: ", 'blue'))

    check_url(token, server_id, url)

if __name__ == "__main__":
    main()