from discord.ext import commands
import yaml

with open("config.yml", 'r') as f:
    config = yaml.load(f)

bot = commands.Bot(command_prefix=config["prefix"])

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.load_extension("sauce")
bot.run(config["token"])