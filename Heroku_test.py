import discord
import asyncio
import time
import configparser
import os
import sys
import youtube_dl
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

    #Epic ID 連携
    if str(message.channel.id) == str("575631344386965525"):
        print("ID連携者: "+str(sender)+", Epic ID: "+str(message.content))

        #ini書き込み
        INI = "D:\\Documents\\Python\\Member`sEpicID.ini"
        conf = configparser.SafeConfigParser()
        #conf.add_section(str(section))
        #conf.set(str(section), str(key), str(passw))
        #conf.set(str(section), str(key+"1"), str(passw+"1"))
        #f = open(file, "w")
        #conf.write(f)
        #f.close()

    #音声垂れ流し
    ydl_opts = {
        'format': 'bestaudio/best',
        'down_dir': 'F:\\Discord_bot_music_folder', 
        'outtmpl':  "sample_music" + '.%(ext)s',
        'postprocessors': [
            {'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
             'preferredquality': '192'},
            {'key': 'FFmpegMetadata'},
        ],
    }

    Music_filel = 'F:\\動画編集に使うやつら\\動画BGM\\NCS\\Robin Hustin x Tobimorrow - Light It Up (feat. Jex).mp3'
    CDM_file = 'F:\\Discord_bot_music_folder\\AOF Countdown VoiceEdited  Recorded by Mayonez  mikan (Nemesis Gaming Ent.)_A.Y.R.5.mp3'
    #ydl = youtube_dl.YoutubeDL(ydl_opts)
    #info_dict = ydl.extract_info("https://www.youtube.com/watch?v=UQsozNGm3wE", download=True)
    #voice = await discord.VoiceChannel.connect(client.get_channel(476041230648606724))
    if message.content == ("$$join"):
        voice = await discord.VoiceChannel.connect(client.get_channel(476041230648606724))
        voice.play(discord.FFmpegPCMAudio(CDM_file))
        voice.is_playing()
        print("joined")
        return


    if message.content == ("$$GoMatch"):
        try:
            print("is_played (T)")
            voice = await discord.VoiceChannel.connect(client.get_channel(476041230648606724))
            voice.play(discord.FFmpegPCMAudio(CDM_file))
            return

        except:
            print("is_played (E)")
            voice = await discord.VoiceChannel.connect(client.get_channel(476041230648606724))
            voice.is_playing()
            return

    if message.content == ("$$Stop"):
        voice = await discord.VoiceChannel.connect(client.get_channel(476041230648606724))
        if(voice.is_playing()):
            voice.stop()
            print("stoped")
            return


    if message.content == ("$$leave"):
        voice = await discord.VoiceChannel.connect(client.get_channel(476041230648606724))
        try:
            if voice is not None:
                await voice.disconnect()
                voice = None
                print("disconnected")
                return

        except:
            await voice.disconnect()
            print("disconnected")
            return



    









    print(message_ids)
    print(sender)













client.run("NTczODg0MDA2MjE1NzEyNzY5.XMxZjw.HykU0JIlXil1t64QhHRdrAetgUY")
