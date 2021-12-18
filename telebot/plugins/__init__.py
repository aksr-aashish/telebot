#    TeleBot - UserBot
#    Copyright (C) 2020 TeleBot

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from telethon.tl.types import Channel

from telebot import *
from telebot import ALIVE_NAME, bot, telever
from telebot.telebotConfig import Config, Var

# stats
log = "Enabled" if Var.PRIVATE_GROUP_ID else "Disabled"
bots = "Enabled" if Config.TG_BOT_USER_NAME_BF_HER else "Disabled"
lyd = "Enabled" if Var.LYDIA_API_KEY else "Disabled"
sudo = "Disabled" if Config.SUDO_USERS else "Enabled"
pm = "Disabled" if Var.PMSECURITY.lower() == "off" else "Enabled"
TELEUSER = str(ALIVE_NAME) if ALIVE_NAME else "@TeleBotSupport"

tele = f"TeleBot Version: {telever}\n"
tele += f"Log Group: {log}\n"
tele += f"Assistant Bot: {bots}\n"
tele += f"Lydia: {lyd}\n"
tele += f"Sudo: {sudo}\n"
tele += f"PMSecurity: {pm}\n"
tele += '\nVisit @TeleBotSupport for assistance.\n'
telestats = f"{tele}"

TELE_NAME = bot.me.first_name
OWNER_ID = bot.me.id

# count total number of groups


async def tele_grps(event):
    a = []
    async for dialog in event.client.iter_dialogs():
        entity = dialog.entity
        if (
            isinstance(entity, Channel)
            and entity.megagroup
            and (entity.creator or entity.admin_rights)
        ):
            a.append(entity.id)
    return len(a), a
