# MorningBot
MorningBot is a Discord bot written in Python that provides a daily informational report every morning. Additionally, weather and news can be accessed at any time and for any city/state/category using certain commands.

**Example Output**:

<img width="860" alt="GoodMorning" src="https://user-images.githubusercontent.com/93621884/151721860-3da410f9-6382-49a8-8833-30a6935c4264.png">

## Table of Contents
1. Getting Started on the Discord Developer Portal
2. Creating a Bot and Granting Authorization
3. Initial Setup (Python)
4. Additional Links

## Getting Started on the Discord Developer Portal
First, create a Discord account and log in to the [Discord Developer Portal](https://discord.com/developers/applications). After logging in, the "Applications" page should be visible. If interested, additional documentation can be found by navigating to the "Documentation" section of the portal.

Note: Before continuing, make sure to create a Discord server that the bot can join if one isn't already made.

## Creating a Bot and Granting Authorization
1. Click "New Application". Enter a name and click "Create".
2. Under "Settings", navigate to the "Bot" section.
3. Click "Add Bot".
4. Under "Settings, navigate to the "OAuth2" section.
5. Under "OAuth2", click "URL Generator".
6. Check the "bot" scope and the "Administrator" bot permission.
7. Copy the generated URL and paste into a new tab.
8. Select the server that the bot will join.
9. Continue and click "Authorize".

## Initial Setup (Python)
Python will need to be installed in order to run the program. In this case, [Python 3.9](https://www.python.org/downloads/release/python-396/) was used. If using MacOS, navigating to the 3.x (in this instance, 3.9) application file and clicking on "Install Certificates.command" may be necessary to avoid an SSL certificate verification error. This may also be true when using a different operating system or Python version.

"discord.py" needs to be downloaded as well, and can be done with the following command:

> pip install -U discord.py

"morningbot.py" can now be configured and used (along with other files in the repo) to send a daily informational report to the desired Discord server and channel.
There are comments included in each file that provide more information.

## Additional Links
Datetime module: https://docs.python.org/3/library/datetime.html

Weather API: https://openweathermap.org/

News API: https://newsapi.org/
