# Bee Movie Discord Bot

This Discord bot sends the script of the Bee Movie, one line at a time, whenever someone sends a message in the "general" text channel. The bot uses a queue system to manage the script lines and ensures each line is sent only once by tracking the lines that have already been sent.

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Files](#files)

## Requirements
- [Python 3.8 or higher](https://www.python.org/downloads/)
- An application created on [Discord's Developer Platform](https://discord.com/developers/docs/intro)
- A local `.env` file that stores the Discord bot's SECRET_KEY
    - The file should contain a single line: `BEE_MOVIE_SCRIPT_SECRET_KEY="{INSERT SECRET KEY HERE}"`
- Necessary Python libraries:
    - [discord.py](https://pypi.org/project/discord.py/)
    - [python-decouple](https://pypi.org/project/python-decouple/)

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/M4GICB/bee-movie-discord-bot.git
    ```

2. Create a local `.env` file in the project directory and add the following line. Be sure to Replace `{INSERT SECRET KEY HERE}` with your actual bot's secret key.
    ```bash
    BEE_MOVIE_SCRIPT_SECRET_KEY="{INSERT SECRET KEY HERE}"
    ```
   

3. Initialize the `Script-Queue.txt` file by copying the contents of `Script-Full.txt`

4. Ensure the `Script-Sent.txt` file is empty to start tracking sent lines


## Usage
### Run Program Directly in Terminal
[Python Command](https://realpython.com/run-python-scripts/#using-the-python-command):
```bash
python BeeMovie.py
```

### Run Program in a Separate Command Prompt Window
#### Windows - [Start Command](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/start):
```bash
start BeeMovie.py
```

#### Mac - [osascript Command](https://ss64.com/mac/osascript.html):
**Terminal:**
```bash
osascript -e 'tell application "Terminal" to do script "python3 BeeMovie.py"'
```

**iTerm2:**
```bash
osascript -e 'tell application "iTerm2" to create window with default profile' \
            -e 'tell current session of current window of application "iTerm2" to write text "python3 BeeMovie.py"'
```

## Features
- **Automated Line Delivery:** Each time a user sends a message in the "general" channel, the bot responds with the next line from the Bee Movie script.
- **Queue Management:** The bot reads from a queue file (`Script-Queue.txt`) and removes the first line after sending it.
- **Line Tracking:** Sent lines are appended to a tracking file (`Script-Sent.txt`) to ensure they are not repeated.
- **Logging:** Detailed logs are maintained in a `BeeMovie.log` file for debugging and monitoring. This file is listed in the `.gitignore` and not committed to the repository.

## Files
- **Script-Full.txt:** Contains the complete Bee Movie script. This file serves as the master list for the bot.
- **Script-Queue.txt:** Initialized with the contents of `Script-Full.txt`. This file contains the lines of the Bee Movie script that are yet to be sent. It is crucial for the queue management system.
- **Script-Sent.txt:** Initialized as an empty file. This file logs the lines that have been sent to avoid duplicates.
- **BeeMovie.log:** A log file that records the bot's activities, useful for debugging and monitoring. It’s ignored by Git, so it won't be included in version control.

