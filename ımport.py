import discord
intents = discord.Intents.default() 
from discord.ext import commands
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def fortnite(ctx):
    embed = discord.Embed(title="Fortnite", description="FORTNİTE 100 KİŞİ BİR ADAYA ATLAYAN VE BUİLD KULLANARAK FİGHT ATABİLECEĞİNİZ BİR OYUNDUR", color=discord.Color.blue())
    embed.add_field(name="Rank Sistemi", value="Bronz dan UnReal a kadar maç atıp kill Alıp sıralama Yaptıkça Puan alır ve Rank Yükselirsiniz", inline=False)
    embed.add_field(name="Pr Sistemi", value="Pr Her Hafta Turnuvalarda Sıralama yaptıkça Alınan Puandır (BEN 4.2K PR IM)", inline=False)

    await ctx.send(embed=embed)

bot.run('MTEwMjI3NDYyNjUzODcwOTAzMw.GPY4RH.VrVa9Dz2WqcOeYyxFsE7Qyx6LvQSxMVQDWZYjU')
