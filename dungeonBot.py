import os
from xml.dom.minidom import Element
import discord
from dotenv import load_dotenv
from discord.ext import commands

#get token + guild name
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

### GAME STUFF ###

#Lists for indiv balances




def findUserIndex(userID):
    try:
        index = users.index(userID)
        return index
    except:
        return None

## MONEY ##

users = []
balances = []
workMoney = []
promoBonus = []
timeUntilPromo = []
timeRequiredPromo = []

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

    
    userIndex = findUserIndex(ctx.author)
    if(userIndex == None):
        users.append(ctx.author)
        balances.append(0)
        workMoney.append(100)
        promoBonus.append(100)
        timeRequiredPromo.append(10)
        timeUntilPromo.append(0)
        userIndex = 0

    balances[userIndex] = balances[userIndex] + 100

    print(userIndex)

    if (timeUntilPromotion >= timeRequiredPromo):
        promotedWorkMoney = workMoney + promoBonus
        workMoney = workMoney + promoBonus
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
