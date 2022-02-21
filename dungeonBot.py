import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

#get token + guild name
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

### GAME STUFF ###
## MONEY ##

money = 0
workMoney = 100
promotionBonus = 50
timeUntilPromotion = 0
timeRequiredPromotion = 10

## COMBAT

maxHealth = 100
currentHealth = 100
maxMana = 100
currentHealth = 100
inventory = []







### BOT STUFF ###
#bot prefix

bot = commands.Bot(command_prefix=',')

#check to see of bot connects to guild
@bot.event
async def on_ready():

    guild = discord.utils.find(lambda g: g.name == GUILD, bot.guilds)
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

### COMMANDS ###
#work command

@bot.command(name='work', help= '- Work for some money!')
async def work(ctx):
    
    global money
    global workMoney
    global promotionBonus
    global timeUntilPromotion
    global timeRequiredPromotion

    if (timeUntilPromotion >= timeRequiredPromotion):
        promotedWorkMoney = workMoney + promotionBonus
        workMoney = workMoney + promotionBonus
        timeUntilPromotion = 0 
        
        await ctx.send('You got promoted! Your new salary is ' + str(promotedWorkMoney) + ' per hour')
        await ctx.send('You worked for an hour and got ' + str(workMoney))
        money = money + workMoney
    else:
        timeUntilPromotion = timeUntilPromotion + 1
        money = money + workMoney
        await ctx.send('You worked for an hour and got ' + str(workMoney))

#balance command
@bot.command(name='bal', help= '- Shows your current balance')
async def bal(ctx):
    global money

    await ctx.send("You have " + str(money) + ' dollars')
        
    




bot.run(TOKEN)
