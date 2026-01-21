import requests
import time
import sys
import os

BLUE = "\033[94m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"
RED = "\033[91m"
GREEN = "\033[92m"
RESET = "\033[0m"

DISCORD_API = "https://discord.com/api/v9"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.008):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    clear()
    print(f"""{BLUE}
███╗   ███╗███████╗███╗   ███╗██████╗ ███████╗██████╗
████╗ ████║██╔════╝████╗ ████║██╔══██╗██╔════╝██╔══██╗                                                                                                                           ██╔████╔██║█████╗  ██╔████╔██║██████╔╝█████╗  ██████╔╝
██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
{CYAN}Member Checker
{GRAY}Public Discord Server Stats
{RESET}""")

def get_widget_data(guild_id):
    try:
        r = requests.get(f"{DISCORD_API}/guilds/{guild_id}/widget.json", timeout=10)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def get_invite_data(code):
    try:
        r = requests.get(f"{DISCORD_API}/invites/{code}?with_counts=true", timeout=10)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

def extract_invite_code(invite_input):
    invite_input = invite_input.strip()
    if "/" in invite_input:
        parts = invite_input.split("/")
        return parts[-1]
    return invite_input

def menu():
    print(f"""{BLUE}
[1]{WHITE} Show online members
[2]{WHITE} Show estimated total members
[3]{WHITE} Show both
[4]{WHITE} Reset server ID or invite
[0]{WHITE} Exit
{GRAY}----------------------------{RESET}
""")

def get_server_input():
    invite_input = input(f"{WHITE}Enter Discord server ID or invite link/code: {RESET}").strip()
    invite_code = extract_invite_code(invite_input)
    guild_id = None
    if invite_code.isdigit():
        guild_id = invite_code
        invite_code = ""
    return guild_id, invite_code

def main():
    banner()
    slow_print(f"{CYAN}Member Checker started\n")

    guild_id, invite_code = get_server_input()

    while True:
        menu()
        choice = input(f"{CYAN}> {RESET}").strip()

        if choice == "1":
            if not guild_id:
                print(f"{RED}Server ID not provided, cannot check online members{RESET}")
            else:
                data = get_widget_data(guild_id)
                if not data:
                    print(f"{RED}Widget data not available{RESET}")
                else:
                    print(f"{GREEN}Server:{RESET} {data['name']}")
                    print(f"{GREEN}Online members:{RESET} {data['presence_count']}")

        elif choice == "2":
            if not invite_code:
                print(f"{RED}No invite link or code provided{RESET}")
            else:
                data = get_invite_data(invite_code)
                if not data:
                    print(f"{RED}Invite data not available{RESET}")
                else:
                    print(f"{GREEN}Server:{RESET} {data['guild']['name']}")
                    print(f"{GREEN}Total members (estimated):{RESET} {data['approximate_member_count']}")

        elif choice == "3":
            widget = get_widget_data(guild_id) if guild_id else None
            invite = get_invite_data(invite_code) if invite_code else None

            if widget:
                print(f"{GREEN}Online members:{RESET} {widget['presence_count']}")
            else:
                print(f"{RED}Online members not available{RESET}")

            if invite:
                print(f"{GREEN}Total members (estimated):{RESET} {invite['approximate_member_count']}")
            else:
                print(f"{RED}Total members not available{RESET}")

        elif choice == "4":
            guild_id, invite_code = get_server_input()
            print(f"{GREEN}Server and invite reset successfully{RESET}")

        elif choice == "0":
            print(f"{BLUE}Exited{RESET}")
            break

        else:
            print(f"{RED}Invalid input{RESET}")

        input(f"{GRAY}\nPress Enter to continue...{RESET}")
        banner()

if __name__ == "__main__":
    main()
