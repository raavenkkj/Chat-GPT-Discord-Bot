import disnake
from disnake.ext import commands
import openai
import asyncio
import os

intents = disnake.Intents.default()
intents.members = True
intents.messages = True

bot = commands.InteractionBot(intents=intents)
openai.api_key = "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"

async def processar_pergunta(pergunta: str):
    response = openai.Completion.create(
        prompt=pergunta,
        temperature=0.7,
        max_tokens=1024,
        n=1,
        stop=None,
        frequency_penalty=0.5,
        presence_penalty=0.5,
        model="text-davinci-002",  
    )
    return response.choices[0].text.strip()

@bot.event
async def on_ready():
    os.system('cls')
    print("Estou pronto!")
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.listening, name="/chatgpt"))

@bot.slash_command(name="chatgpt", description="Responde qualquer tipo de pergunta com precisão!")
async def chatgpt(interaction: disnake.ApplicationCommandInteraction, pergunta: str):
    await interaction.response.defer()
    resposta = await asyncio.create_task(processar_pergunta(pergunta))
    
    embed = disnake.Embed(description=resposta, color=0x000000)
    
    await interaction.edit_original_message(embed=embed)


@bot.slash_command(name="imagem", description="Gera imagens com inteligência artificial.")
async def imagem(interaction: disnake.ApplicationCommandInteraction, prompt: str):
    await interaction.response.defer()
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
        )
    image_url = response['data'][0]['url']
    await interaction.edit_original_message(content=image_url)


bot.run("MTA3NzMyMTgxMjE2MzE2NjI2OQ.GlfNNw._h0u1iJ8FNhQN64Fz_rKRrQ1ulbEBCs6nmXRG8")
