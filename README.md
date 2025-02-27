# Studly Bot

Studly Bot is a Discord bot that provides various commands to convert lengths into LEGO studs, plates, and bricks at different scales.

## Commands

### /studs
Get the number of studs in length at 1:38, 1:42, and 1:48 scale.

- **Parameters:**
  - `length` (int): The length to convert.
  - `unit` (str): The unit of the length, either 'feet' or 'meters'.

### /plates
Get the number of plates tall at 1:38, 1:42, and 1:48 scale.

- **Parameters:**
  - `length` (int): The length to convert.
  - `unit` (str): The unit of the length, either 'feet' or 'meters'.

### /bricks
Get the number of bricks tall at 1:38, 1:42, and 1:48 scale.

- **Parameters:**
  - `length` (int): The length to convert.
  - `unit` (str): The unit of the length, either 'feet' or 'meters'.

### /bp
Get the number of bricks and plates tall at 1:38, 1:42, and 1:48 scales.

- **Parameters:**
  - `length` (int): The length to convert.
  - `unit` (str): The unit of the length, either 'feet' or 'meters'.

### /help
Display Studly Bot's commands.

- **Parameters:**
  - `command` (str, optional): The specific command to get help for. If not provided, lists all commands.

## Setup

To add the bot to your Discord server, follow these steps:

1. Clone the repository:
    ```bash
    git clone /home/aronwk/Documents/git/studly-bot/studly-bot
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Create a `.env` file in the root directory and add your Discord bot token:
    ```env
    DISCORD_TOKEN=your_discord_bot_token
    ```

4. Run the bot:
    ```bash
    python bot.py
    ```

## Contributing

Feel free to submit issues or pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License.

