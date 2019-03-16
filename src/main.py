import discord
import requests
import event_manager

TOKEN = "NTUyOTEwMjE2ODI0NDg3OTU3.D2GbVg.khBctMDju8fWscgYRWbTdjWQOwo"
DESCRIPTION = " with your feelings"

PREFIX_COMMAND = "!"
PREFIX_ERROR = "[ERROR]"
PREFIX_OK = "[OK]"

COMMANDS = {
	"viva"		: PREFIX_COMMAND + "viva",
	"help"		: PREFIX_COMMAND + "help",
	"horario"	: PREFIX_COMMAND + "horario",
	"examenes"	: PREFIX_COMMAND + "examenes",
	"show"		: PREFIX_COMMAND + "show",
	"show_all"	: PREFIX_COMMAND + "show_all",
	"add"		: PREFIX_COMMAND + "add",
	"del"		: PREFIX_COMMAND + "del",
	"search_name"	: PREFIX_COMMAND + "search_name",
	"search_day"	: PREFIX_COMMAND + "search_day",
	"search_month"	: PREFIX_COMMAND + "search_month",
	"search_year"	: PREFIX_COMMAND + "search_year"
}

IMAGES_DIR = "images/"

ERROR_MSG = PREFIX_ERROR + " What the fuck was that? Do us all a favor and type !help"
ADDED_MSG = PREFIX_OK + " Added correctly OwO"
DELETED_MSG = PREFIX_OK + " Deleted correctly OwO"


client = discord.Client()

def format_error_message(correct_format):
	return ("El formato es \"" + correct_format + "\" trozo de mierda")

@client.event
async def on_ready():
	print("Bot ready...")
	await client.change_presence(game=discord.Game(name=DESCRIPTION))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if COMMANDS["viva"] == message.content[:5]:
		await client.send_message(message.channel, "~Viva España~")

	if COMMANDS["help"] == message.content[:5]:
		help_string = ""

		for k, v in COMMANDS.items():
			help_string += "- Comando %s : \"%s\"\n" % (k, v)

		await client.send_message(message.channel, help_string)

	elif COMMANDS["horario"] == message.content[:8]:
		try:
			await client.send_file(message.channel, IMAGES_DIR + message.content[9:12] + '.png')
		except Exception as e:
			print(e)
			await client.send_message(message.channel,
				format_error_message(COMMANDS["horario"] + " group"))

	elif COMMANDS["show_all"] == message.content[:9]:
		await client.send_message(message.channel, event_manager.read_events())

	elif COMMANDS["show"] == message.content[:5]:
		await client.send_message(message.channel, event_manager.pretty_events())

	elif COMMANDS["add"] == message.content[:4]:
		try:
			name	= message.content.split(event_manager.SEPARATOR)[1]
			day	= message.content.split(event_manager.SEPARATOR)[2]
			month	= message.content.split(event_manager.SEPARATOR)[3]
			year	= message.content.split(event_manager.SEPARATOR)[4]

			event_manager.add_event(name, day, month, year)
			await client.send_message(message.channel, ADDED_MSG)
		except Exception as e:
			print(e)
			await client.send_message(message.channel,
				format_error_message(COMMANDS["add"] + " Name day month year"))

	elif COMMANDS["search_name"] == message.content[:12]:
		try:
			name = message.content.split(event_manager.SEPARATOR)[1]

			await client.send_message(message.channel, event_manager.search_events_name(name))
		except Exception as e:
			print(e)
			await client.send_message(message.channel,
				format_error_message(COMMANDS["search_name"] + " name"))

	elif COMMANDS["search_day"] == message.content[:11]:
		try:
			day = message.content.split(event_manager.SEPARATOR)[1]

			await client.send_message(message.channel, event_manager.search_events_day(day))
		except Exception as e:
			print(e)
			await client.send_message(message.channel,
				format_error_message(COMMANDS["search_day"] + " day"))

	elif COMMANDS["search_month"] == message.content[:11]:
		try:
			month = message.content.split(event_manager.SEPARATOR)[1]

			await client.send_message(message.channel, event_manager.search_events_month(month))
		except Exception as e:
			print(e)
			await client.send_message(message.channel,
				format_error_message(COMMANDS["search_month"] + " month"))

	elif COMMANDS["search_year"] == message.content[:11]:
		try:
			year = message.content.split(event_manager.SEPARATOR)[1]

			await client.send_message(message.channel, event_manager.search_events_year(year))
		except Exception as e:
			print(e)
			await client.send_message(message.channel,
				format_error_message(COMMANDS["search_year"] + " year"))

	elif COMMANDS["del"] == message.content[:10]:
		try:
			uid = message.content.split(event_manager.SEPARATOR)[1]

			event_manager.del_event(uid)

			await client.send_message(message.channel, DELETED_MSG)
		except Exception as e:
			print(e)
			await client.send_message(message.channel,
				format_error_message(COMMANDS["del"] + " ID"))

client.run(TOKEN)