import json

PluginName = 'saymessage'
ConfigPath = 'config/'
ConfigFilePath = ConfigPath + PluginName + '.json'
with open(ConfigFilePath, 'r') as f:
    	js = json.load(f)
    	deathMessage = str(js["deathMessage"])
    	joinMessage = str(js["joinMessage"])
    	leftMessage = str(js["leftMessage"])


def on_death_message(server, death_message):
	player = death_message.split(' ')[0]
	if player != 'load':
		msg = '§e' + deathMessage + ' §7' + player
		server.say(msg)

def on_player_joined(server, player):
	if player != 'load':
		msg = '§e' + joinMessage + ' §7' + player
		server.say(msg)

def on_player_left(server, player):
	if player != 'load':
		msg = '§e' + leftMessage + ' §7' + player
		server.say(msg)