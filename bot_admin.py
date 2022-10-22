import nextcord as nc
from nextcord.ext import commands, application_checks

client = commands.Bot()

@client.slash_command(
  description='Этой коммандой вы можете забанить пользователя')
@application_checks.has_role('Sky')
async def ban(inser: nc.Interaction, user: nc.Member,why=None):
  await user.ban()
  embed = nc.Embed(title="Бан")
  embed.add_field(name="Был забанен", value=str(user.nick), inline=False)
  embed.add_field(name="За что:", value=why, inline=False) if why != None else ''
  await inser.send(embed=embed)

@client.slash_command(
  description='Этой коммандой вы можете кикнуть пользователя')
@application_checks.has_role('Sky')
async def kick(inser: nc.Interaction,user: nc.Member,why=''):
  await user.kick()
  embed = nc.Embed(title="Кик")
  embed.add_field(name="Был кикнут", value=str(user.nick), inline=False)
  embed.add_field(name="За что:", value=why, inline=False) if why != None else ''
  await inser.send(embed=embed)
  
@client.slash_command(
  description='Этой коммандой вы можете разбанить пользователя')
@application_checks.has_role('Sky')
async def unban(inser: nc.Interaction,user: nc.Member,why=''):
  await user.unban()
  embed = nc.Embed(title="Разбан")
  embed.add_field(name="Был разбанен", value=str(user.nick), inline=False)
  embed.add_field(name="За что:", value=why, inline=False) if why != None else ''
  await inser.send(embed=embed)

if __name__ == '__main__':
  client.run('Token')
