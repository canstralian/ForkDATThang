# Remote Access Trojan (RAT)

![RAT Logo](link_to_logo_or_image)

## Description
This project is a Remote Access Trojan (RAT) designed to allow remote control and monitoring of target devices. It provides various features, such as taking screenshots, capturing webcam photos, retrieving system information, downloading files, and more. Please note that this tool is intended for educational and ethical purposes only. Unauthorized use is strictly prohibited.

## Features
- [x] Capture screenshots
- [x] Take webcam photos
- [x] Retrieve system information
- [x] Download files remotely
- [x] Grab saved passwords from browsers
- [x] Grab saved cookies from browsers
- [x] Grab Discord user token
- [x] Retrieve system logs
- [x] Kill specified processes
- [x] Control screenlogger functionality
- [x] Set and execute payloads from URLs
- [x] Grab saved WiFi passwords
- [x] Ping functionality to check bot responsiveness

## Usage
To use the RAT, follow these steps:
1. Clone or download the repository.
2. Install the required Python packages by running: `pip install -r requirements.txt`
3. Replace `BOT_TOKEN` in the code with your actual Discord bot token.
4. Run the bot by executing the script: `python bot.py`
5. Invite the bot to your Discord server and use the available commands.

## Prerequisites
- Python 3.6 or higher
- Discord.py library
- Other required Python packages listed in `requirements.txt`

## Building the RAT
To build the RAT executable (.exe) file, you can use pyinstaller. Follow these steps:
1. Install pyinstaller by running: `pip install pyinstaller`
2. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the following command: `pyinstaller --onefile --noconsole bot.py`
5. After the build process completes, the executable file will be available in the `dist` directory.

## Defender Evasion
This RAT is designed to evade detection by traditional antivirus software. However, it's important to note that the effectiveness of evasion techniques may vary over time as antivirus systems improve. While efforts have been made to make the RAT undetectable, it cannot be guaranteed that it will evade all antivirus solutions. It's always recommended to use such tools responsibly and legally.

## Contribution
Contributions to this project are welcome. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## Support
If you need help or have any questions, you can join our Discord server (insert invite link) for support and discussions.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer
The creators of this project are not responsible for any unauthorized use or misuse of the software. This tool is intended for educational and ethical purposes only. Use it responsibly and only on devices that you own or have explicit permission to access.

