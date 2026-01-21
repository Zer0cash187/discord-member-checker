# Discord Member Checker

A Python tool to check **online members** and **estimated total members** of public Discord servers using a **server ID** or **invite link/code**.  

This tool works for public servers only and **does not require a bot** or joining the server.

---

## Features

- Works with **server ID** or **full invite link/code**  
- Shows **online members** using the Discord Widget (requires widget enabled)  
- Shows **estimated total members** using Discord invite data  
- Menu option to **reset server or invite** without restarting  
- Works on **Linux/Termux, Windows, and macOS**  
- Automatically installs the `requests` library if missing  

---

## Installation

1. Open a terminal (Linux/Termux/macOS) or Command Prompt (Windows).  
2. Download the program by cloning the repository:

```
git clone https://github.com/Zer0cash187/discord-member-checker.git
```
Navigate into the program folder:

```
cd discord-member-checker
```
The script is ready to run. No additional setup is needed. Required libraries will be installed automatically the first time you run the program.
How to Start
Run the program by typing:
```
python member_checker.py
```
Follow the on-screen instructions:
Enter a server ID or full invite link/code when prompted
Use the menu to:
Show online members
Show estimated total members
Show both
Reset server ID or invite to check another server without restarting
Exit the program
After selecting an option, press Enter to continue back to the menu.
## Examples
Server ID: 123456789012345678
Invite link: https://discord.gg/abcd1234
The script automatically extracts the invite code from a full link.

![Logo](Example.png)
## Notes
Only works with public servers or servers that have enabled the widget
Estimated total members may slightly differ from the actual number
Does not join the server or access private data
Use responsibly and do not spam Discord API requests
