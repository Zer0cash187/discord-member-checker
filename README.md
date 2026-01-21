# Discord Member Checker

A Python tool to check **online members** and **estimated total members** of public Discord servers using a **server ID** or **invite link/code**.  

This tool works for public servers only and **does not require a bot** or joining the server.

---

## Features

- Works with **server ID** or **full invite link/code**.  
- Shows **online members** using the Discord Widget (requires widget enabled).  
- Shows **estimated total members** using Discord invite data.  
- Menu option to **reset server or invite** without restarting.  
- Works on **Linux/Termux, Windows, and macOS**.  
- Automatically installs the `requests` library if missing.  

---

## Installation

1. Open a terminal (Linux/Termux/macOS) or Command Prompt (Windows).  
2. Clone the repository:

```bash
git clone https://github.com/Zer0cash187/discord-member-checker.git
Navigate into the folder:
Code kopieren
Bash
cd discord-member-checker
The script is ready to run; no additional setup is needed. The required library will install automatically.
How to Start
Run the script:
Code kopieren
Bash
python member_checker.py
Follow the on-screen instructions:
Enter a server ID or full invite link/code.
Use the menu to:
Show online members
Show estimated total members
Show both
Reset server ID or invite to check another server
Exit the program
Examples
Server ID: 123456789012345678
Invite link: https://discord.gg/abcd1234
The script automatically extracts the invite code from a full link.
Notes
Only works with public servers or servers with enabled widget.
Estimated total members may differ slightly from actual numbers.
Does not join the server or access private data.
Use responsibly and do not spam Discord API requests.
