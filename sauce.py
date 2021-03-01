from saucenao_api import SauceNao
from discord.ext import commands
from discord import Embed
import yaml

with open("config.yml", 'r') as f:
    config = yaml.load(f)

class SauceNAO(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.nao = SauceNao(api_key=config["api-key"])
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.channel.is_nsfw() and config["nsfw-only"]:
            return
        
        if message.attachments:
            url = message.attachments[0].url
        else:
            return  
        
        result = self.nao.from_url(url)
        if result:
            result = result[0]
        
        if not result.urls:
            embed = Embed(
                title = "No sauce found!",
                description = "SauceNAO couldn't find a sauce to this image.",
                colour = 0xff0000
            )
            await message.channel.send(embed=embed)
            return
        
        embed = Embed(
            title = "Sauce found!",
            url = result.urls[0],
            colour = 0x00ff00
        )
        embed.add_field(name="Title", value=result.title)
        embed.add_field(name="Author", value=result.author)
        embed.add_field(name = "Similarity", value = f"{result.similarity}%")
        
        embed.set_thumbnail(url=url)
        await message.channel.send(embed=embed)
    
    @commands.command()
    async def sauce(self, ctx, *, url=None):
        if not url:
            url = ctx.message.attachments[0].url
        
        result = self.nao.from_url(url)
        if result:
            result = result[0]
        
        if not result.urls:
            embed = Embed(
                title = "No sauce found!",
                description = "SauceNAO couldn't find a sauce to this image.",
                colour = 0xff0000
            )
            await message.channel.send(embed=embed)
            return
        
        embed = Embed(
            title = "Sauce found!",
            url = result.urls[0],
            colour = 0x00ff00
        )
        embed.add_field(name="Title", value=result.title)
        embed.add_field(name="Author", value=result.author)
        embed.add_field(name = "Similarity", value = f"{result.similarity}%")
        
        embed.set_thumbnail(url=url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(SauceNAO(bot))