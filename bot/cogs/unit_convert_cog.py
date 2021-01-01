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
    
    try:
      # Grab the registry of common units and a Quantity object
      ureg = UnitRegistry()
      Q_ = ureg.Quantity
      # Convert the number parameter to an numeric value
      sourceNumber = float(number)
      # Create the source quantity using the Quantity constructor
      quantity = Q_(sourceNumber, sourceUnit)
      # Get the converted value and print the final results
      convertedQuantity = quantity.to(desiredUnit)
      msg = await ctx.send(f"{sourceNumber} {sourceUnit} is {convertedQuantity.magnitude} {desiredUnit}")
    except UndefinedUnitError as e: # If at least one of the given units doesn't exist in the registry
      msg = await ctx.send(e)
    except DimensionalityError as e: # If an invalid conversion is attempted
      msg = await ctx.send(e)

def setup(bot):
  bot.add_cog(UnitConvertCog(bot))
    
