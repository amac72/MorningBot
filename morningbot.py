import os
from dotenv import load_dotenv
from discord.ext import commands, tasks

# Imports "dt.py" and its functions
from dt import generate_date
from dt import generate_time

# Imports "weather.py" and its function
from weather import get_temp

# Imports "news.py" and its function
from news import get_news

# Loads environmental variables
load_dotenv()
# In the ".env" file, token can be found in the bot section of app in Discord dev portal
TOKEN = os.getenv('DISCORD_TOKEN')
# In the ".env" file, this is name of desired server
CHANNEL = os.getenv('DISCORD_CHANNEL')

# Creates the client connection
bot = commands.Bot(command_prefix='.')

# Begins run
@bot.event
async def on_ready():
    run.start()
    check_time.start()
    print('Bot is running.')

# Confirms to Discord channel that MorningBot is active 
@tasks.loop(count=1)
async def run():
    # In the ".env" file, channel ID is found on Discord. Must have dev mode on to copy
    channel = bot.get_channel(int(CHANNEL))
    message = ("MorningBot is active.")
    await channel.send(message)

# Checks time every second. If it's 08:00:00 local time, informational message will send with default settings
@tasks.loop(seconds=1)
async def check_time():
    current_time = generate_time()
    if current_time=="08:00:00":
        # In the ".env" file, channel ID is found on Discord. Must have dev mode on to copy
        channel = bot.get_channel(int(CHANNEL))
        current_date = generate_date()
        await channel.send("Good Morning!\n" + current_date)
        city = "New York" # This will be default city
        state = "NY" # This will be default state
        category = "tech" # This will be default category
        temp = get_temp(city, state)
        celsius = temp[0]
        fahrenheit = temp[1]
        weather_info = f"It is currently {celsius:.2f} degrees Celsius in {city}, {state}. That is equal to {fahrenheit:.2f} degrees Fahrenheit.".format({})
        news = get_news(category)
        await channel.send(weather_info)
        await channel.send(news)

# Additionally, weather and news can be accessed at any time and for any city/state/category using these commands
# Weather Command = .get Weather {city_name} {state_code}
# News Command = .get News {category}
@bot.command()
async def get(ctx, arg, arg2, arg3="CA"):
    if arg=="Weather":
        temp = get_temp(arg2, arg3)
        print(temp)
        celsius = temp[0]
        fahrenheit = temp[1]
        weather_info = f"It is currently {celsius:.2f} degrees Celsius in that city. That is equal to {fahrenheit:.2f} degrees Fahrenheit.".format({})
        await ctx.send(weather_info)
    elif arg=="News":
        news_info = get_news(arg2)
        print(news_info)
        await ctx.send(news_info)
    else:
        pass

# This starts the run
bot.run(TOKEN)

# Use control-C to end run in terminal