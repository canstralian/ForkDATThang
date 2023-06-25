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


# Command List

A list of available commands for the bot.

- `bot_help` - Shows the help message for the bot.
- `bot_restart` - Restarts the bot.
- `bot_shutdown` - Shuts down the bot.
- `bypass_uac` - Bypasses User Account Control (UAC).
- `camic` - Takes a webcam photo.
- `clear` - Clears the current channel or chat.
- `delete` - Deletes a file or directory.
- `download` - Downloads a file from a URL.
- `grab_browser` - Grabs browser-related information.
- `grab_history` - Grabs browsing history.
- `grab_wifi` - Grabs saved Wi-Fi passwords.
- `help` - Shows this message.
- `info` - Shows information about the bot.
- `kill_process` - Terminates a running process.
- `list_process` - Lists the running processes.
- `move` - Moves a file or directory.
- `open_url` - Opens a URL in the default browser.
- `ping` - Checks the network latency to a specified host.
- `powershell` - Executes a PowerShell command or script.
- `rename` - Renames a file or directory.
- `screenlogger` - Logs screen activity.
- `screenshot` - Takes a screenshot of the screen.
- `set_payload` - Sets a payload by providing a URL to download and execute a file.
- `sys_info` - Retrieves system information.
- `sys_restart` - Restarts the system.
- `sys_shutdown` - Shuts down the system.
- `upload` - Uploads a file.

Please note that some commands may have security implications or are typically associated with malicious activities. Use them responsibly and in accordance with applicable laws and regulations.


## Free Plan
  
Our Free plan offers limited features. The following features will be implemented:

1. Improved Information and Interaction:
   - The "**!info**" command will provide more detailed information about the bot, including its capabilities and version.
   - The "**!bot_help**" command will display an updated and user-friendly help message, guiding users through the available commands and    their usage.
   - The "**!contact**" command will enable users to send feedback directly to the developer, facilitating communication and addressing any concerns or suggestions.

2. Streamlined Message Management:
   - The "**!clear**" command will be enhanced to allow users to specify the number of messages to clear, providing more flexibility and control over message cleanup in the channel.

3. Expanded File and System Manipulation:
   - The "**!set_payload <URL>**" command will enable users to download and execute a file from a provided URL, allowing for convenient and secure file execution on the target machine.
   - The "**!powershell**" command will provide users with the ability to execute PowerShell commands directly on the target machine, facilitating advanced scripting and automation tasks.
   - The "**!screenshot**" command will capture a screenshot of the target machine's screen, allowing users to monitor or gather visual information.

4. Enhanced Process and System Information:
   - The "**!get_process_list**" command will provide users with a list of running processes on the target machine, aiding in process management and monitoring.
   - The "**!kill_process <name>**" command will allow users to terminate a specified process on the target machine, providing control over system resources.
   - The "**!sys_info**" command will offer comprehensive information about the target machine's operating system, aiding in system diagnostics and troubleshooting.

5. Improved Web Interaction:
   - The "**!open_website <URL>**" command will enable users to open a specified URL directly on the target machine's browser, facilitating convenient access to web content.

By upgrading to our Free plan, you will enjoy these enhanced features and advanced features, making your system management and interaction more efficient and user-friendly.

## Preminum Plan

Our Premium upgrade plan offers advanced features and enhanced capabilities to further empower the functions . The following upgrades will be implemented:

1. Advanced Data Gathering and Analysis:
   - The "**grab_browser**" command will be expanded to extract additional information from web browsers, such as browsing history, bookmarks, and saved passwords.
   - The "**grab_wifi**" command will be enhanced to capture more detailed information about nearby Wi-Fi networks, including signal strength and encryption types.

2. Extended System Management:
   - The "**kill_process**" command will allow you to terminate multiple processes simultaneously, providing greater control over system resources.
   - The "**list_process**" command will be upgraded to display additional details about running processes, such as CPU and memory usage.

3. Enhanced Remote Operations:
   - The "**open_url**" command will support opening URLs on remote machines, allowing you to access specific web pages or launch remote applications.
   - The "**upload**" command will be enhanced to enable secure and efficient file transfer between local and remote systems.

4. Advanced System Information and Control:
   - The "**sys_info**" command will provide more comprehensive and detailed system information, including hardware specifications, installed software, and network configurations.
   - The "**sys_restart**" and "sys_shutdown" commands will offer additional options for scheduling system restarts or shutdowns at specific times.

5. Expanded Exploitation and Penetration Testing:
   - The "**set_payload**" command will be upgraded to support advanced payload creation and customization for exploitation and penetration testing purposes.
   - The "**powershell**" command will provide direct access to PowerShell functionalities, enabling more sophisticated scripting and automation capabilities.

By upgrading to our Premium plan, you will gain access to these advanced features and enjoy a more comprehensive and powerful system management experience.

## Upgrade to Premium

Unlock additional features and upgrade to the premium version!

For more information on premium features and pricing, please contact `business@redalliance.com`

## Support

For any questions or support regarding this RAT, please contact `faq@redalliance.com`

## Contributing

Contributions to this project are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue on the GitHub repository.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to modify and distribute the code, but remember to adhere to the license terms.

