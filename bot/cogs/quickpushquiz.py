from datetime import date, datetime
from discord.ext import commands
from discord.ui import View, button, Button
from discord import Option, OptionChoice, SlashCommandGroup, Interaction
import discord


class QuickPushQuiz(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    # quiz系コマンド
    _quiz_command = SlashCommandGroup(
        name="quiz", description="quick push quiz command")
    # quiz管理者用のコマンド
    _quiz_command.create_subgroup(
        name="admin", description="administer command")

    
