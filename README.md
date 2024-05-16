# Telegram Bot for Tracking and Closing Applications

A bot that helps to track the running time of programs remotely through the Telegram system. PS: Based on the telebot library.

This project is created for educational purposes by Vladimir Bryzgalov and Danil Belousov.

This Telegram bot is designed to track the running time of various applications and close them if needed. The bot uses the `psutil` library to interact with system processes and the `telebot` library to interact with the Telegram API.

## Features

### Tracking Applications

The bot can track the running time of the following applications:

- Google (chrome.exe)
- Telegram (Telegram.exe)
- Yandex (browser.exe)
- WeChat (WeChat.exe)

### Closing Applications

The bot can close the following applications:

- Google (chrome.exe)
- Telegram (Telegram.exe)
- Yandex (browser.exe)
- WeChat (WeChat.exe)

## Usage

### Starting the Bot

To start the bot, send the `/start` or `/restart` command. This will display a message with two buttons: "Track" and "Close".

### Tracking Applications

Click the "Track" button to display a list of applications to track. Select the application you want to track, and the bot will display the running time of the application in minutes and seconds.

### Closing Applications

Click the "Close" button to display a list of applications to close. Select the application you want to close, and the bot will terminate the process.

## Note

The bot requires the `psutil` and `telebot` libraries to be installed. You also need to replace `'YOUR_TELEGRAM_BOT_TOKEN'` with your actual Telegram bot token.

## Limitations

The bot can only track and close applications that are running under the same user account as the bot. It may not work correctly if the applications are running under a different user account or as system services.

## First Version

1. To customize for yourself, you should enter your token received from BotFather in line 20.
2. By default, this bot is configured for the Windows operating system and monitors programs such as Google, Telegram, Yandex, and WeChat.
   - To change the list of programs, you can enter your data by analogy with the code block (86-96) lines or (134-136) lines.
   - To add the buttons, you can view the lines (69-70) or (51-52), do not forget to add them to the keyboard!

Have a good experience!
