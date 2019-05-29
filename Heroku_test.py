import discord
import asyncio
import ffmpeg
import glob




client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')






# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

    if message.content.startswith('/join'):
        role = discord.utils.get(message.guild.roles, name='ggg')
        await message.author.add_roles(role)
        reply = f'{message.author.mention} ようこそ！'
        await message.channel.send(reply)

    if message.content == 'PlEmo':
        await client.wait_for(':ok_hand:')

    if message.content == '574844121882165258':
        channel = message.channel
        #await channel.send('Send me that 👍 reaction, mate')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👌'

        try:
            reaction, user = await client.wait_for('reaction_add', check=check)
        except asyncio.TimeoutError:
            #await channel.send('👎')
            pass
        else:
            await channel.send('👍')
            role = discord.utils.get(message.guild.roles, name='Family')
            await message.author.add_roles(role)

    if message.content == "$custom_key$":
        await message.channel.send('@everyone')
        embed = discord.Embed(title="鯖主制作のBotを追加しました！", description="主に使用する予定の機能は以下の通りです")
        embed.add_field(name="・サーバー管理機能", value="新規加入者様へのルール確認機能や荒し対策機能など")
        embed.add_field(name="・ゲーム募集の効率化", value="募集内容を当てはめて送信するだけでBotが自動で埋め込み機能などを使用し、募集してくれる機能を開発中です")
        embed.add_field(name="・(未定)音楽鑑賞", value="インターネット上のリンクを内容に当てはめ送信するだけでBotが自動で音楽を流してくれる機能の開発を試みています")
        await message.channel.send(content=None, embed=embed)

    messid = message.id

    channel_ids = message.channel.id        
    message_ids = messid
    sender = message.author
    CHANNEL_ID = 575141493417967626# 任意のチャンネルID(int)
    channelg = client.get_channel(CHANNEL_ID)

    #Edit a message
    if message.content == "%test":
        MAE = await message.channel.send("FUCKING_GAME")
        await MAE.edit(content="newcontent")

    #Edit a speccial message
    if message.content == "%tst1":
        TPTK = discord.Embed(title="Player", description="")
        TPTL__ = discord.Embed(title="Player", description="gegs")
        _bots_send_ = await channelg.send(content=None, embed=TPTK)
        await _bots_send_.edit(content=None, embed=TPTL__)








client.run("NTczODg0MDA2MjE1NzEyNzY5.XMxZjw.HykU0JIlXil1t64QhHRdrAetgUY")
