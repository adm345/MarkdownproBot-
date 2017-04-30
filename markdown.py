#!/usr/bin/env python3
#-*- coding: utf-8 -*-
# encoding: utf-8

import telepot, sys, os, sys, requests, requests, random, requests, urllib, urllib2, json, platform
from functools import partial
from pytube import YouTube
from telepot.namedtuple import InlineQueryResultArticle
from datetime import datetime
import threading, time, datetime, string
from PythonColorize import *
from telepot.namedtuple import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, ForceReply
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton
from telepot.namedtuple import InlineQueryResultArticle, InlineQueryResultPhoto, InputTextMessageContent
from pprint import pprint
import string
############
  

os.system("clear")
reload(sys)


sys.setdefaultencoding('utf8')

## BOT Config
today = datetime.datetime.today()
t = today.strftime("[%H:%M:%S] - ")
bot = telepot.Bot(' ')
NomeBot = "Tal"

## BOT LANG
info_id = "Nome: *{}*\nUsuário: {}\nID: `{}`"
dados = "O Dado parou no número: 🎲 `{}`"

def handle(msg):
### BOT PARAMTS
    chat_id = msg['chat']['id']
    chat_type = msg['chat']['type']
    from_id = msg['from']['id']
    from_first_name = msg['from']['first_name']
    from_username = "@" + msg['from']['username']
    texto = msg['text']
    message_id = msg['message_id']
    print(colors.lg_red + t + colors.lg_blue + ' Mensagem executada: %s' % colors.lg_red + texto + colors.nocolor)

### BOT COMANDOS
    if texto == '/hora':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
    elif texto == '/help':
        markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='Ajuda 🗨', url='https://t.me/DailyMotionbot_Channel/27')]])
        bot.sendMessage(chat_id, """

Sr(a) *{}* 😃 eu vi que você está com dúvidas 🤔
Entra no meu canal Aaqui nós botão abaixo👇""".format(msg['from']['first_name']), reply_markup=markup, parse_mode="Markdown")
    elif texto == '/start':
        a = bot.getMe()
        n= a['first_name']
        markup = InlineKeyboardMarkup(inline_keyboard=[[dict(text='canal 🗣', url='https://t.me/DailyMotionbot_Channel')]+[dict(text='Cyon💡', url='https://t.me/equipecyon')]])
        bot.sendMessage(chat_id, """
Olá *{}*
Sou o *{}* criado para formatar textos!
digite /help para saber mais sobre mim.""".format(msg['from']['first_name'], n), "Markdown", reply_markup=markup)
    elif texto == '/markdown':
        bot.sendMessage(chat_id, '''
Use a sintaxe a seguir em sua mensagem com Markdown:

*texto bold*
_texto itálico_
[texto](URL)
`Código de largura fixa em linha`
```Bloco de código pré-formatado de largura fixa```''')
        bot.sendMessage(chat_id, '''
Use a sintaxe a seguir em sua mensagem com Markdown:

*texto bold*
_texto itálico_
[texto](URL)
`Código de largura fixa em linha`
```Bloco de código pré-formatado de largura fixa```''', "Markdown")

    elif texto == '/html':
        bot.sendMessage(chat_id, '''

Use a sintaxe a seguir em sua mensagem com HTML:

<b>texto em negrito</b>
<i>Texto em itálico</i>
<a href="URL">text</a>
<code>Código de largura fixa inline</code>
<pre>Bloco de código pré-formatado de largura fixa</pre>''')
        bot.sendMessage(chat_id, '''

Use a sintaxe a seguir em sua mensagem com HTML:

<b>texto em negrito</b>
<i>Texto em itálico</i>
<a href="URL">text</a>
<code>Código de largura fixa inline</code>
<pre>Bloco de código pré-formatado de largura fixa</pre>''', "HTML")

    elif ("*" in texto or "_" in texto or "`" in texto):
        try:bot.sendMessage(chat_id, texto, parse_mode="Markdown")
        except:bot.sendMessage(chat_id, "\n\nVerifique os parâmetros de formatação")
    elif ("<" in texto or ">" in texto):
            try:bot.sendMessage(chat_id, texto, parse_mode="HTML")
            except:bot.sendMessage(chat_id, texto+"\n\n⚠Verifique os parâmetros de formatação")
### Executando
print(colors.lg_red + t + colors.lg_cyan + NomeBot + " iniciado")
time.sleep(2)
bot.message_loop(handle)
while 1:
    time.sleep(10)
