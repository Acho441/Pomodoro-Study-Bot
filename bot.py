from discord.ext import tasks, commands
import discord
from dataclasses import dataclass
from datetime import datetime, timedelta
from config import token

BOT_TOKEN = token
# Get the channel Id in your own discord server with developer mode on, and change it to yours
CHANNEL_ID = 709941647424749679
MAX_SESSION_TIME_MINUTES = 25


@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
session = Session()


@bot.event
async def on_ready():
    print("Hello! Pomodoro Study Bot is ready")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Hello! Pomodoro Study Bot is ready")


@tasks.loop(minutes=MAX_SESSION_TIME_MINUTES, count=5)
async def break_reminder(author):

    # Ignore the first execution of this command
    if break_reminder.current_loop == 0:
        return

    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"{author} **Take a break for 5 minutes!** You've been studying for {MAX_SESSION_TIME_MINUTES} minutes.")
    break_reminder_time.start(author)
    

    if break_reminder.current_loop == 4:
        await channel.send(f"{author} **Take a break between 15-30 minutes! you have studied for one full loop** start the session again after coming back from break")
        session.is_active = False


@tasks.loop(minutes=MAX_SESSION_TIME_MINUTES/5, count=2)
async def break_reminder_time(author):

    # Ignore the first execution of this command
    if break_reminder_time.current_loop == 0:
        return
    
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"{author} **Break time is over time to continue working**")

@bot.command()
async def start(ctx):
    if session.is_active:
        await ctx.send("A session is already active!")
        return
    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()
    author = ctx.message.author.mention
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    break_reminder.start(author)
    await ctx.send(f"New session started at {current_time}")


@bot.command()
async def end(ctx):
    if not session.is_active:
        await ctx.send("No session is active!")
        return
    
    session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time
    human_readable_duration = str(timedelta(seconds=duration))
    formated_duration = human_readable_duration.split(".")[0]
    break_reminder.cancel()
    await ctx.send(f"Session ended after {formated_duration}.")


bot.run(BOT_TOKEN)
