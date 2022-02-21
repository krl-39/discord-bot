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
#users(userID, balance, workMoney, promoBonus, timeRequiredPromo, timeUntilPromo)

# userID = 0
# balance = 1
# workMoney = 2
# promoBonus = 3
# timeRequiredPromo = 4
# timeUntilPromo = 5 

users = []


def findUserIndex(userID):
    index = 0
    for user in users:
        if (user[index] == userID):
            return index
    return None
            


## COMBAT

maxHealth = 100
currentHealth = 100
maxMana = 100
currentHealth = 100
inventory = []







### BOT STUFF ###

#find the author's list number



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

    
    userIndex = findUserIndex(ctx.author)
    if(userIndex == None):
        users.append((ctx.author, 0, 100, 100, 10, 0))
        userIndex = 0



    print(userIndex)

    (userID, balance, workMoney, promoBonus, timeRequiredPromo, timeUntilPromo) = users[userIndex]


    if (timeUntilPromo == timeRequiredPromo):
        promotedWorkMoney = workMoney + promoBonus
        workMoney = promotedWorkMoney
        balance = balance + workMoney
        timeUntilPromo = 0 
        users[userIndex] = (userID, balance, workMoney, promoBonus, timeRequiredPromo, timeUntilPromo)
        await ctx.send('You got promoted! Your new salary is ' + str(promotedWorkMoney) + ' per hour')
        await ctx.send('You worked for an hour and got ' + str(workMoney) + ' dollars')
  
    else:
        timeUntilPromo = timeUntilPromo + 1
        balance = balance + workMoney
        users[userIndex] = (userID, balance, workMoney, promoBonus, timeRequiredPromo, timeUntilPromo)
        await ctx.send('You worked for an hour and got ' + str(workMoney) + ' dollars')

    

#balance command
@bot.command(name='bal', help= '- Shows your current balance')
async def bal(ctx):

    userIndex = findUserIndex(ctx.author)

    if (userIndex == None):
        bal = 0
    else:
        bal = users[userIndex][1]


    await ctx.send("You have " + str(bal) + ' dollars')
        
    




bot.run(TOKEN)
