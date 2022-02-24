import os
from xml.dom.minidom import Element
import discord
from dotenv import load_dotenv
from discord.ext import commands
from userData import EcoStats, User, BattleStats

#get token + guild name
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

### GAME STUFF ###

#Lists for indiv balances
#users(userID, balance, workMoney, promoBonus, timeRequiredPromo, timeUntilPromo)

# userID = 0
# balance = 1
# workMoney = 2
# promoBonus = 3
# timeRequiredPromo = 4
# timeUntilPromo = 5 

users = []


def findUser(userID):
    for user in users:
        if (user.userID == userID):
            return user
    return None
            


## COMBAT
zombie = ['zombie' , 150 , 50, 0, 'undead']
mobs = [zombie]
# mob name = ['mob name' , health , damage , defense , mob type] add true damage?


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

    #userList = list(users)
    user = findUser(ctx.author)
    if(user == None):
        battleStat = BattleStats(maxHP = 100, HP = 100, maxMana = 100, Mana =100, inv = [])
        ecoStat = EcoStats(balance = 0, workMoney = 100, promoBonus = 100, timeRequiredPromo = 10, timeUntilPromo = 0)
        user = User(ctx.author, ecoStat, battleStat)
        users.append(user)
    
    print(user.battleStats.maxHP)

    promoted = user.ecoStats.work()
   
    if (promoted): 
        await ctx.send('You got promoted! Your new salary is ' + str(user.ecoStats.workMoney) + ' per hour')
        await ctx.send('You worked for an hour and got ' + str(user.ecoStats.workMoney) + ' dollars')
    else:
        await ctx.send('You worked for an hour and got ' + str(user.ecoStats.workMoney) + ' dollars')

#balance command
@bot.command(name='bal', help= '- Shows your current balance')
async def bal(ctx):

    user = findUser(ctx.author)

    if (user == None):
        bal = 0
    else:
        bal = user.ecoStats.balance

    await ctx.send("You have " + str(bal) + ' dollars')
#fight command
@bot.command(name = 'fight', help = '- Fight a mob!')
async def fight(ctx):
    await ctx.send('Which mob?')
    await ctx.send('1. ' + str((mobs[0][0])))

        
    
bot.run(TOKEN)
