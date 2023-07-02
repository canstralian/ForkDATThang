# Discord RAT (Remote Access Trojan) 

Discord RAT is an advanced remote access trojan written in Python and controlled through the Discord platform with a dedicated GUI builder. It provides various features for controlling and managing remote machines, including executing commands, geolocation tracking, capturing screenshots, webcam snapshots, network scanning, process management, system information retrieval, website opening, keylogging, and more.

**Disclaimer: This code is intended for educational purposes only. Misuse of this code for any malicious activities is strictly prohibited. The author is not responsible for any consequences resulting from the misuse of this code.**

## Features

- **Spy Mode**: It provides real-time notifications on user activities and credential leaks.
- **Remote Control**: This feature allows users to remotely control the target machine.
- **Startup Auto-Run**: This feature allows to automatically initiate the spy mode on every boot
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
- Requests library: Install using `pip install requests`
- PyAutoGUI library: Install using `pip install pyautogui`

## Usage

1. Clone the repository or download the code.

2. Install the required libraries using the provided commands.

3. Create a Discord bot and obtain the bot token. Refer to the Discord documentation for instructions on creating a bot.

4. Replace the placeholder bot token in the code with your actual bot token.

5. Run the Python script using `python Dat.py` or `python3 Dat.py`

6. Invite the bot to your Discord server and start using the available commands.

## Building the RAT
 
To build the RAT executable (.exe) file, you can use pyinstaller. Follow these steps:

- Install `pyinstaller` by running pip install pyinstaller.
- Open a terminal or command prompt.
- Navigate to the project directory.
- Run the following command: `pyinstaller --onefile --noconsole Dat.py`
- After the build process completes, the executable file will be available in the dist directory.

## Defender Evasion

This RAT is designed to evade detection by traditional antivirus software. However, it's important to note that the effectiveness of evasion techniques may vary over time as antivirus systems improve. While efforts have been made to make the RAT undetectable, it cannot be guaranteed that it will evade all antivirus solutions. It's always recommended to use such tools responsibly and legally.

# Command List

 A list of available commands for the bot.

- `!info` - Display information about the bot
- `!bot_help` - Display this help message
- `!clear [amount]` - Clear a specified number of messages in the channel (default: 5)
- `!contact` - Send feedback to the developer
- `!set_payload <URL>` - Download and execute a file from the provided URL
- `!powershell` - Execute a PowerShell command on the target machine
- `!screenshot` - Take a screenshot of the target machine's screen
- `!get_process_list` - Get a list of running processes on the target machine
- `!kill_process <name>` - Kill a specified process on the target machine
- `!sys_info` - Get information about the target machine's operating system
- `!open_website <URL>` - Open a specified URL on the target machine

Please note that some commands may have security implications or are typically associated with malicious activities. Use them responsibly and in accordance with applicable laws and regulations.

## Premium Plan

- All features from the Free Plan, plus the following:

- `!bot_help`       - Shows the help message for the bot.
- `!bot_restart`    - Restarts the bot.
- `!bot_shutdown`   - Shuts down the bot.
- `!bypass_uac`     - Bypasses User Account Control (UAC) with administrator permissions.
- `!camic`          - Takes a webcam photo.
- `!clear`          - Clears the current screen or messages in the channel.
- `!delete`         - Deletes a file or directory.
- `!download`       - Downloads a file from a specified URL.
- `!grab_browser`   - Retrieves information about the default browser.
- `!grab_history`   - Retrieves browsing history from the default browser.
- `!grab_wifi`      - Retrieves information about saved Wi-Fi networks.
- `!help`           - Shows a help message or provides assistance.
- `!info`           - Displays information about the bot.
- `!kill_process`   - Terminates a running process.
- `!list_process`   - Lists all running processes.
- `!move`           - Moves a file or directory to a new location.
- `!open_url`       - Opens a specified URL in the default browser.
- `!ping`           - Checks the latency (ping) to a specified destination.
- `!powershell`     - Executes a PowerShell command or script.
- `!rename`         - Renames a file or directory.
- `!screenlogger`   - Toggles the screenlogger on or off to capture screen activity.
- `!screenshot`     - Takes a screenshot of the screen.
- `!set_payload`    - Sets a payload by providing a URL to download and execute a file on the target system.
- `!sys_info`       - Retrieves system information.
- `!sys_restart`    - Restarts the system.
- `!sys_shutdown`   - Shuts down the system.
- `!upload`         - Uploads a file.


By upgrading to our Premium plan, you will have access to these advanced features and enjoy a more comprehensive and powerful system management experience.

## Upgrade to Premium

Unlock additional features and upgrade to the premium version!

For more information on premium features and pricing, please contact `business.redalliance@gmail.com`

## Support

For any questions or support regarding this RAT, please contact `faq.redalliance@gmail.com`

## Contributing

Contributions to this project are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository.

## License

This project is licensed under the **No Copy License**. No one has permission to copy, modify, distribute, or use this code for any purpose. This code is provided for educational purposes only and should not be used for any malicious activities. The author is not responsible for any consequences resulting from the misuse of this code.
