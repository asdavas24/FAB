#FORÇAS ARMADAS BREAKPOINT BOT.

#TESTE ANTES DE PUBLICAR OFICIALMENTE EM CANAL ABERTO. O LINK DO CONFIG_BOT_CHANNEL É PRIVADO PARA ADM E PROGRAMADORES DO SERVIDOR.

#LISTA DO QUE FAZER:
#--REACTION ROLE
#--AUTO ROLE BY JOIN THE SERVER 
#--WELCOME/BAN/LEFT MEMBER IN SERVER
#--ANNOUNCEMENTS MESSAGES WITH TIMER AND ONCE MESSAGE ANNOUNCEMMENTS


#
#--------------------------ATIVAÇÃO DO BOT-----------------------------------
import discord
from discord.ext import tasks
from datetime import timezone, datetime
from dotenv import load_dotenv
import signal
import os
import pytz
from discord.ext import commands
import keep_alive

load_dotenv()
intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)



@client.event
async def on_ready():
  print('USER NAME:')
  print(client.user.name)
  print('\nUSER ID:')
  print(client.user.id)
  print('\nStatus: Ativo!'.format(client))
  current_time.start()
  print('-----------------------------')
  bot_config_channel=client.get_channel(865652121901465620)
  await bot_config_channel.send('--------------------------------------------------------\n ﾠﾠﾠﾠﾠﾠﾠﾠﾠﾠ **Estou conectado!** \n --------------------------------------------------------')
  chame_o_bot = comandos_do_bot=client.get_channel(886808192452026438)
  #await comandos_do_bot.send('**STATUS DO BOT:** :white_check_mark:')


 

#-----------------------------CHAMAR O BOT-------------------------------------------------------

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('>teste'):
    await message.channel.send('Aparentemente estou funcional, tente os outros comandos.')

  if message.content.startswith('>uniforme'):
    await message.channel.send("Acesse o link para ver os uniformes e selecione o pdf compativel com seu curso:\n https://discord.com/channels/828029636449402922/848427279880683571")

  if message.content.startswith('>link_do_servidor'):
    await message.channel.send("Este é o link do servidor Forças Armadas Breakpoint: https://discord.gg/8nHpGp7shy")
    
  if message.content.startswith('>regras'):
    await message.channel.send("Para ler as regras, acesse o canal abaixo para ver o material e abra o pdf: \n\n **CANAL:** <#828610849122811954>")

  if message.content.startswith('>classes'):
    await message.channel.send("Acesse o canal abaixo e abra o pdf para ver as classes disponíveis e as regras que utilizamos no servidor de acordo com cada classe. \n\n **CANAL:** <#836299511667884103>")

  if message.content.startswith('>rank'):
    await message.channel.send("Acesse o canal abaixo e selecione o pdf de rank para ver o que você desbloqueia em cada um. \n\n **CANAL:** <#835776514380529674>")


  if message.content.startswith('>comprovar_rank'):
    await message.channel.send("Para comprovar seu rank você deve enviar exatamente no padrão solicitado ou não será atualizado. \n\nVocê descobre como comprovar em. \n <#949099947951804447>")
  
  if message.content.startswith('>patente'):
    await message.channel.send("Acesse o canal abaixo e abra o pdf de patente para ver as patentes do nosso servidor, como progredir e quais suais funções.\n\n **CANAL:** <#835776514380529674>")


  if message.content.startswith('>trocar_classe'):
    await message.channel.send("Para trocar de classe escreva: **'>quero_trocar'** mas antes tenha em mente que você só pode solicitar a troca de classe **apenas 1 vez**, depois ela fica permanente ")
    
  if message.content.startswith('>social'):
    await message.channel.send("\n**CANAL OFICIAL NO YOUTUBE**\n\n **LINK:**https://www.youtube.com/channel/UCct4Pg4cFnCOyuqaIZcxqkw \n\n")
    await message.channel.send('**----------------------------------------------------------** \n\n **CANAL OFICIAL NA TWITCH** \n\n **LINK:**https://www.twitch.tv/forcas_armadas_breakpoint\n\n')
    await message.channel.send('**----------------------------------------------------------** \n\n **CONTA OFICIAL NO INSTAGRAM** \n\n **LINK:** https://www.instagram.com/forcasarmadasbreakpoint/ \n  **----------------------------------------------------------**')

    

#----------------------------4 FAZES DO ALISTAMENTO------------------------------------------------

    

  if message.content.startswith('>alistamento'):
    await message.channel.send(f'**Bem vindo(a) FAB siga a instrução abaixo!** \n\n:flag_br: Para iniciar seu <@&881997038387093525> você precisa responder o formulário abaixo, clicando no link.\n\n:flag_br: LINK: https://docs.google.com/forms/d/1ePxRo4PeWdH9J26GyRd8GmQ0dZdaw8yVgh6e5Tso5xw/edit\n\n **SUPORTE:**\n\n <@827941238606790717> \n\n <@971261598205370409> \n\n <@910233487297114194> \n--------------------------------------------------------------------------------------------------------------------\n\n')



  if message.content.startswith('>selecao_geral'):
    
    await message.channel.send(f'**Bem vindo(a) FAB siga a instrução abaixo!** \n\n <@&865657677031407636> \n\n Agora sabemos de qual plataforma você pertence e você sabe que este é um servidor com foco em MilSim \n\n **Leia todos os PDFs dos 4 canais de regras abaixo:** \n\n <#828610849122811954> \n\n <#835776514380529674> \n\n <#836299511667884103> \n\n <#848427279880683571> \n\n *Somente quando concluir a leitura acesse o canal <#828031424090079263> para iniciar seu processo à aprovação FAB*')


  if message.content.startswith('>designação'): 
    
    await message.channel.send(f'**MONTAGEM DE PERFIL** \n\n *Agora você esta na fase de <@&933144209991553074> e para concluir o seu alistamento FAB você deve responder o formulário abaixo. Lembre-se que este é um servidor MilSim, então* **escolha sua classe com sabedoria!** \n\n **LINK;** https://docs.google.com/forms/d/e/1FAIpQLSfx2Dx1N5MsHpHrCnr71X-0fNRBN4EehoCSgrMhcXFokbP6lA/viewform')




    


  #----------------------------GIVE AUTO ROLE BY REACTION-----------------------------------------------

  #if message.content.startswith(">verificação"):
    #embed_verific = discord.Embed(title = "Selecione o Idioma/Select the Language \n\nPara falantes de português reagir com bandeira do Brasil :flag_br:\n\nFor English speakers react with usa flag :flag_us:", description= " ", color=0xffff00)
  
    #await message.channel.send(embed=embed_verific) #embed funcional porem sem reaction role.

    



 #----------------------------EMBED MESSAGE FOR: >bot_versao--------------------------------------------

  if message.content== '>bot_versao':
    bot_config_channel=client.get_channel(865652121901465620)
    comandos_do_bot=client.get_channel(886808192452026438)
    chame_o_bot_aqui=client.get_channel(886812041640284180)

    myEmbed = discord.Embed(title='Versão Atual:',description='ALPHA: v1.03 ',color=0xffff00)
    myEmbed.add_field(name='.',value='.', inline=False)
    myEmbed.add_field(name='Status atual:',value='Em desenvolvimento', inline=False)
    myEmbed.add_field(name='.',value='.', inline=False)
    myEmbed.add_field(name='Desenvolvedores:',value='asdavas24#4751 & Wolf Blckfield#2181', inline=False)
     
    await bot_config_channel.send(embed=myEmbed)
    await comandos_do_bot.send(embed=myEmbed)
    await chame_o_bot_aqui.send(embed=myEmbed)
    

#--------------------------------LISTA DE COMANDOS > ---------------------------------------------------
  if message.content== '>lista':
    comandos_do_bot=client.get_channel(886808192452026438)
    myEmbed1 = discord.Embed(title='Lista de comandos: Use o prefixo ">"', 
    description= """
   . -----------------------
    1. >teste
    ⠀
    2. >bot_versao
    ⠀
    3. >link_do_servidor
    -----------------------
    4. >regras
    ⠀
    5. >patente
    ⠀
    6. >rank
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    7. >comprovar_rank                      
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    8. >classes
    9. >trocar_classe
    ⠀
    10. >uniforme
    ⠀
    11. >solicitar_oficial 
    -----------------------
    12. >suporte """, color=0xffff00)

    await message.channel.send(embed=myEmbed1)

#--------------------------------SOLICITAÇÃO DE OFICIAL > ---------------------------------------------------

  if message.content== '>solicitar_oficial':
    configuração_de_bot=client.get_channel(865652121901465620)
    myEmbed2 = discord.Embed(title='Lista de comandos: Use o prefixo ">"', 
    description= """
   . -----------------------------------------
    **O que você gostaria de solicitar?** \n\n*Lembre-se que se você não tiver os requisitos o seu pedido será negado.* \n
                             
    1. >obter_curso
                             
    2. >obter_patente""", color=0xffff00)

    await message.channel.send(embed=myEmbed2)
    
#--------------------------------SOLICITAÇÃO DE CURSO > ---------------------------------------------------

  if message.content== '>obter_curso':
    configuração_de_bot=client.get_channel(865652121901465620)
    myEmbed3 = discord.Embed(title='Lista de comandos: Use o prefixo ">"', 
    description= """
   . -----------------------------------------
    **O que você gostaria de solicitar?** \n\n*Lembre-se que se você não tiver os requisitos o seu pedido será negado.* \n
                             
    1. >sniper
                             
    2. >paraquedista
                             
    3. >comandos
                          
    4. >tier_one""", color=0xffff00)

    await message.channel.send(embed=myEmbed3)



#--------------------------------SOLICITAÇÃO DE PATENTE > ---------------------------------------------------

  if message.content== '>obter_patente':
    configuração_de_bot=client.get_channel(865652121901465620)
    myEmbed4 = discord.Embed(title='Lista de comandos: Use o prefixo ">"', 
    description= """
   . -----------------------------------------
    **O que você gostaria de solicitar?** \n\n*Lembre-se que se você não tiver os requisitos o seu pedido será negado.* \n
                             
    >soldado
    >cabo
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    >3_sgt
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    >2_sgt
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    >1_sgt
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    >subtenente
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    >aspirante
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    >2_tenente
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    >1_tenente
  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    >capitão
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    >major""", color=0xffff00)

    await message.channel.send(embed=myEmbed4) 

#--------------------------------RESULTADO DOS ITENS ANTERIORES > ---------------------------------------------------


  
  if message.content== '>quero_trocar':
    solicitação_de_teste=client.get_channel(943335365312405504)
    chame_o_bot = client.get_channel(886812041640284180)
    print(f'{message.author.mention} chamou o bot')
    
    myEmbed = discord.Embed(title=f' ',description='solicitou a troca de classe. Você deve notificar um COO ou o CEO',color=0xffff00)
  
    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')


  if message.content== '>sniper':
    solicitação_de_teste=client.get_channel(949132109451235329)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f' ',description='solicitou o teste de Sniper',color=0xffff00)

    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')



    await bot_config_channel.send(embed=myEmbed)

  if message.content== '>paraquedista':
    solicitação_de_teste=client.get_channel(949132109451235329)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f'  ',description='solicitou o teste de Paraquedista',color=0xffff00)

    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')


  if message.content== '>comandos':
    solicitação_de_teste=client.get_channel(949132109451235329)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f' ',description='solicitou o teste de Comandos',color=0xffff00)

    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')
    



  if message.content== '>tier_one':
    solicitação_de_teste=client.get_channel(949132109451235329)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f'  ',description='solicitou o teste de Tier One',color=0xffff00)

    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')



  if message.content== '>soldado':
    solicitação_de_teste=client.get_channel(943335365312405504)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f' ',description='solicitou o teste de Soldado',color=0xffff00)

    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')



  if message.content== '>cabo':
    solicitação_de_teste=client.get_channel(943335365312405504)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f' ',description='solicitou o teste de Cabo',color=0xffff00)

    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')


    
  if message.content== '>3_sgt':
    solicitação_de_teste=client.get_channel(943335365312405504)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f' ',description='solicitou o teste de 3°Sgt',color=0xffff00)

    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')


    
  if message.content== '>2_sgt':
    solicitação_de_teste=client.get_channel(950093664036745267)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f' ',description='solicitou o teste de 2°Sgt',color=0xffff00)

    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')


    
  if message.content== '>1_sgt':
    solicitação_de_teste=client.get_channel(950093664036745267)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f' ',description='solicitou o teste de 1°Sgt',color=0xffff00)

    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')
    
   if message.content== '>subtenente':
    solicitação_de_teste=client.get_channel(950093664036745267)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f' ',description='solicitou o teste de subtenente',color=0xffff00)

    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')

    
  if message.content== '>aspirante':
    solicitação_de_teste=client.get_channel(950093664036745267)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f' ',description='solicitou o teste de Aspirante',color=0xffff00)

    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')


    
  if message.content== '2_tenente':
    solicitação_de_teste=client.get_channel(950093664036745267)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f' ',description='solicitou o teste de 2°Tenente',color=0xffff00)

    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')



    
  if message.content== '>1_tenente':
    solicitação_de_teste=client.get_channel(950093664036745267)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f' ',description='solicitou o teste de 1°Tenente',color=0xffff00)

    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')



  if message.content== '>capitão':
    solicitação_de_teste=client.get_channel(950093664036745267)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f' ',description='solicitou o teste de Capitão',color=0xffff00)
 
    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')




  if message.content== '>major':
    solicitação_de_teste=client.get_channel(950093664036745267)
    chame_o_bot = chame_o_bot=client.get_channel(886812041640284180)
    
    myEmbed = discord.Embed(title=f' ',description='solicitou o teste de Major',color=0xffff00)

    await solicitação_de_teste.send(f'{message.author.mention} ')
    await solicitação_de_teste.send(embed=myEmbed)
    await chame_o_bot.send(f'{message.author.mention} sua solicitação foi recebida!')
    

#----------------------------LISTA SELECIONADO: SUPORTE ------------------------------------------------

  if message.content== '>suporte':
    configuração_de_bot=client.get_channel(865652121901465620)
    myEmbed3 = discord.Embed(title='Lista de comandos: Use o prefixo ">"', 
    description= """
   . -----------------------------------------
    Qual tipo de suporte você gostaria de solicitar?
    ⠀⠀⠀⠀⠀
    1. >admin
    ⠀⠀
    2. >programador""", color=0xffff00)

    await message.channel.send(embed=myEmbed3)

  if message.content== '>admin':
    bot_config_channel=client.get_channel(886812041640284180)
    coronel_cordeiro = client.get_user(827941238606790717)
    tencol_oliveira = client.get_user(971261598205370409)
    tencol_famarrom = client.get_user(910233487297114194)


    myEmbed = discord.Embed(title='Membros da administração FAB:',description='⠀',color=0xffff00)
    myEmbed.add_field(name=f'{coronel_cordeiro.mention}⠀',value='Criador das Forças Armadas Breakpoint', inline=False)
    myEmbed.add_field(name=f'⠀',value='⠀', inline=False)
    myEmbed.add_field(name=f'{tencol_oliveira.mention}',value='Sub-adm das Forças Armadas Breakpoint', inline=False)
    myEmbed.add_field(name=f'⠀',value='⠀', inline=False)
    myEmbed.add_field(name=f'{tencol_famarrom.mention}⠀',value='Sub-adm das Forças Armadas Breakpoint', inline=False)
    
    await message.channel.send(embed=myEmbed)

  if message.content== '>programador':
    bot_config_channel=client.get_channel(886812041640284180)
    coronel_cordeiro1 = client.get_user(827941238606790717)
    tencol_blackfield1 = client.get_user(786393293415252058)

    myEmbed = discord.Embed(title='Equipe de programação FAB:',description='⠀',color=0xffff00)
    myEmbed.add_field(name=f'{coronel_cordeiro1.mention}⠀',value='Criador das Forças Armadas Breakpoint', inline=False)
    myEmbed.add_field(name=f'⠀',value='⠀', inline=False)
    myEmbed.add_field(name=f'{tencol_blackfield1.mention}⠀',value='Sub-adm das Forças Armadas Breakpoint', inline=False)

    await message.channel.send(embed=myEmbed)


  




#---------------------------EXIT MESSAGE--------------------------------------------------------------


@client.event #CANAL DE DESERTOR
async def on_member_remove(member):
    print(f"{member} has left!")
    leave_channel = client.get_channel(865661676007325707)
    await leave_channel.send(f"\n\n{member.mention} acabou de desertar :clown: \n\n")
  





#------------------------------------------CLEAR CHAT------------------------------------------


    



##--------------------------------------DIA DE HOJE---------------------------------------------------------

@tasks.loop(hours=24)
async def current_time():
  dt = datetime.now(timezone.utc)
  
  # Data no padrão BR
  tz_BR = pytz.timezone("Brazil/East")
  dt = dt.astimezone(tz_BR) 
  data_B = dt.strftime('%d/%m/%Y [%H:%M:%S]')

  # Data no padrão US
  #tz_US = pytz.timezone("US/Central")
  #dt = dt.astimezone(tz_US) 
  #data_US = dt.strftime('%m/%d/%Y [%H:%M:%S]')
  

  channel=client.get_channel(865652121901465620)

  await channel.send("Hoje é " + data_B + " :flag_br: (BR/Brasília)")
  await channel.send("-------------------------------------------------------- ")

  
#-------------------------------------TOKEN----------------------------------------------------------

token =('EtlqRsp1SuFHrjMFPfctArR4vFMUz1Gv')


#LINK PARA PROGRAMAR O BOT: ''https://replit.com/@ForcasArmadas/Forcas-Armadas-Breakpoint-BOT#main.py''

#LINK PARA DESENVOLVEDORES DE APLICAÇÕES DISCORD:  ''https://discord.com/developers/applications/885349727732899880/information''  (gerado apartir do meu notebook)
