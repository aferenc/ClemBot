import logging
import discord
import discord.ext.commands as commands
from pint import UnitRegistry
from pint import UndefinedUnitError
from pint import DimensionalityError

log = logging.getLogger(__name__)

class UnitConvertCog(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def unitconvert(self, ctx, number, sourceUnit, desiredUnit):
    """
    Given a measurement in a source unit, convert to the desired unit (where possible)

    USE: unitconvert <quantity> <source unit> <desired unit>
    EXAMPLE: unitconvert 12.0 inches feet
    """
    # TO-DO: handle cases of temperature conversion, as temps can't be created using the "number * ureg('unit')"" method
    
    try:
      ureg = UnitRegistry()
      sourceNumber = float(number)
      quantity = sourceNumber * ureg(sourceUnit)
      convertedQuantity = quantity.to(desiredUnit)
      msg = await ctx.send(f"{sourceNumber} {sourceUnit} is {convertedQuantity.magnitude} {desiredUnit}")
    except UndefinedUnitError as e: # If at least one of the given units doesn't exist
      msg = await ctx.send(e)
    except DimensionalityError as e: # If an invalid conversion is attempted
      msg = await ctx.send(e)

def setup(bot):
  bot.add_cog(UnitConvertCog(bot))
    
