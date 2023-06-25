# Discord RAT (Remote Access Trojan)

Discord RAT is an advanced remote access trojan written in Python and controlled through the Discord platform with a dedicated GUI builder. It provides various features for controlling and managing remote machines, including executing commands, geolocation tracking, capturing screenshots, webcam snapshots, network scanning, process management, system information retrieval, website opening, keylogging, and more.

**Disclaimer: This code is intended for educational purposes only. Misuse of this code for any malicious activities is strictly prohibited. The author is not responsible for any consequences resulting from the misuse of this code.**

## Features

- **Spy Mode**: It provides real-time notifications on user activities and credential leaks.
- **Encryption**: Encrypt the connection with the target, making it secure and undetectable.
- **Task Scheduler**: Schedule specific tasks for future execution on the target machine.
- **Network Management**: Manage and control multiple targets in a single interface. Create, edit, and delete targets on the go.
- **User-Friendly**: User-friendly interface with detailed information about targets and features.
- **Extensibility**: Easily extendable with custom plugins for new features and functionality.

## Prerequisites

- Python 3.7 or above
- Discord.py library: Install using `pip install discord.py`
- Plyer library: Install using `pip install plyer`
- PyAudio library: Install using `pip install pyaudio`
- OpenCV library: Install using `pip install opencv-python`
- Geocoder library: Install using `pip install geocoder`
- Geopy library: Install using `pip install geopy`
- Requests library: Install using `pip install requests`
- Netifaces library: Install using `pip install netifaces`
- PyAutoGUI library: Install using `pip install pyautogui`
- Nmap (optional): Required for network scanning. Install Nmap on your system.

## Usage

1. Clone the repository or download the code.

2. Install the required libraries using the provided commands.

3. Create a Discord bot and obtain the bot token. Refer to the Discord documentation for instructions on creating a bot.

4. Replace the placeholder bot token in the code with your actual bot token.

5. Run the Python script using `python bot.py` or `python3 bot.py`.

6. Invite the bot to your Discord server and start using the available commands.

## Available Commands

- `!set_payload <URL>`: Download and execute a file from the provided URL.
- `!info`: Display information about the bot.
- `!clear [amount]`: Clear a specified number of messages in the channel (default: 5).
- `!bot_help`: Display the help message with available commands.
- `!powershell <command>`: Execute a PowerShell command on the target machine.
- `!geolocate`: Get the geolocation information of the target machine.
- `!screenshot`: Take a screenshot of the target machine's screen.
- `!webcam_snap`: Capture a photo using the target machine's webcam.
- `!scan_network`: Scan the local network for active hosts.
- `!list_interfaces`: List the network interfaces on the target machine.
- `!get_mac <IP>`: Get the MAC address of a specified IP address.
- `!get_process_list`: Get a list of running processes on the target machine.
- `!kill_process <name>`: Kill a specified process on the target machine.
- `!get_startup_programs`: Get a list of startup programs on the target machine.
- `!get_system_info`: Get information about the target machine's operating system.
- `!open_website <URL>`: Open a website on the target machine's default browser.
- `!keylogger_start`: Start the keylogger on the target machine.
- `!keylogger_dump`: Dump the recorded keystrokes from the target machine.
- `!keylogger_stop`: Stop the keylogger on the target machine.

## Contributing

Contributions to this project are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute the code, but remember to adhere to the license terms.

