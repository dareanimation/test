# �C���X�g�[������ discord.py ��ǂݍ���
import discord

# ������Bot�̃A�N�Z�X�g�[�N���ɒu�������Ă�������
TOKEN = 'NTgyNzE5MDc0OTc5Njc2MTcw.XOx5mw.xt8_ZOlv9NNTyx_xrT-QQZ46VHo'

# �ڑ��ɕK�v�ȃI�u�W�F�N�g�𐶐�
client = discord.Client()

# �N�����ɓ��삷�鏈��
@client.event
async def on_ready():
    # �N��������^�[�~�i���Ƀ��O�C���ʒm���\�������
    print('���O�C�����܂���')

# ���b�Z�[�W��M���ɓ��삷�鏈��
@client.event
async def on_message(message):
    # ���b�Z�[�W���M�҂�Bot�������ꍇ�͖�������
    if message.author.bot:
        return
    # �u/neko�v�Ɣ���������u�ɂ�[��v���Ԃ鏈��
    if message.content == '/neko':
        await message.channel.send('�ɂ�[��')

# Bot�̋N����Discord�T�[�o�[�ւ̐ڑ�
client.run(TOKEN)