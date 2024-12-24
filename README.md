# Discord-Vanity-URL-Guard
Discord URL Guard Bot
Description
This Discord URL Guard Bot is designed to monitor and restore a Discord server's vanity URL. It periodically checks if the specified URL is still active on the server, and if not, attempts to restore it. This tool is especially useful for maintaining the continuity of Discord server access and ensuring the URL is not lost or hijacked.

### Features

URL Monitoring: Continuously checks the availability of a Discord server's vanity URL.
URL Restoration: Automatically restores the URL if it is found to be inactive or changed.

### Requirements:
Python 3.6 or higher
requests library
colorama library for colored terminal output
termcolor library

### Installation
Clone the repository:
git clone https://github.com/feraxrd/Discord-Vanity-URL-Guard.git

### Install the required libraries:
pip install requests colorama termcolor

### Run main.py:
python main.py
Enter the required details (Discord token, server ID, and URL) when prompted.
Security Note
This tool requires your Discord token for operation. Ensure that you never share your token publicly and understand the security implications of using this tool.

License
MIT License
