from src.functions.getFirstLetter import split_letters
import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix="!")


@bot.command("roll")
async def roll(ctx, *arg):
    if arg:
        try:
            splitArgs = split_letters(arg[0])
        except:
            await ctx.send("Please specify a dice E.g d20")
            return
        if splitArgs[1][0] != "d":
            await ctx.send("{0} is not a dice. Please specify a dice E.g d20".format(arg[0]))
            return
        else:
            number = 1
            if splitArgs[0] != "":
                number = int(splitArgs[0])

            if number >= 1000000:
                await ctx.send("too many dice rolls try again")
                

            mod = splitArgs[1].split("+")
            negative = False
            if len(mod) == 1:
                mod = splitArgs[1].split("-")
                if len(mod) > 1:
                    negative = True

            modifier = 0
            if len(mod) > 1:
                modifier = int(mod[1])
                if negative:
                    modifier = modifier * -1
            diceType = mod[0].split("d")[1]
            try:
                diceType = int(diceType)
            except:
                await ctx.send("{0} is not a dice type. Please specify a dice E.g d20".format(arg[0]))
                return
            if diceType <= 1:
                await ctx.send("D{0} is not a supported dice type.".format(diceType))
                return
            
            if number == 1:
                if modifier == 0:
                    await ctx.send("D{0} Roll: {1}".format(diceType, random.randrange(1, diceType+1)))
                    return
                roll = random.randrange(1, diceType+1)
                rollMod = roll+modifier
                modStr = "+{0}".format(modifier)
                
                if negative:
                    modStr = "{0}".format(modifier)
                await ctx.send("D{0} Roll: {1}{2} = {3}".format(diceType, roll, modStr, rollMod))
                return
            else:
                total = 0
                rolls = list()
                for i in range(number):
                    roll = random.randrange(1, diceType+1)+modifier
                    rolls.append(roll)
                    total = total+roll
                await ctx.send("Total:\t {0}\nRolls\t{1}\nModifier{2}".format(total, rolls, modifier))
                if (len(endstr) >= 1999):
                    endstr = "Total:\t {0}\nModifier{1}".format(total,modifier)
                await ctx.send(endstr)
                return

    else:
        await ctx.send("D20 Roll: {0}".format(random.randrange(1, 21)))

