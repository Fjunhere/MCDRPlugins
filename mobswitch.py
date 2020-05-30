import json, time


PluginName = 'mobswitch'
ConfigPath = 'config/'
ConfigFilePath = ConfigPath + PluginName + '.json'


with open(ConfigFilePath, 'r') as f:
		js = json.load(f)
		overworld_posi = str(js["overworld"])
		the_nether_posi = str(js["the_nether"])
	

def on_info(server, info):
	if info.is_player == 1 and info.content.startswith('!!mobs'):
		args = info.content.split(' ')
		if len(args) == 1:
			server.say('用!!mobs 维度 open开启，!!mobs 维度 close关闭')
		elif len(args) == 3:
			dimension = args[1]
			status = args[2]
			if dimension == 'overworld':
				dimension_cn = '§2主世界'
				position = overworld_posi
			elif dimension == 'the_nether':
				dimension_cn = '§4地狱'
				position = the_nether_posi
			server.say(f'@{dimension_cn} §r伪和平正在加载')
			cmd_a = f'execute in minecraft:{dimension} run player load spawn at {position}'
			cmd_b = 'player load kill'
			server.execute(cmd_a)
			if status == 'open':
				server.execute(f'execute in minecraft:{dimension} run setblock {position} air')
				time.sleep(5)
				server.execute(cmd_b)
				server.say(f'@{dimension_cn} §r伪和平已开启')
			elif status == 'close':
				server.execute(f'execute in minecraft:{dimension} run setblock {position} redstone_block')
				time.sleep(5)
				server.execute(cmd_b)
				server.say(f'@{dimension_cn} §r伪和平已关闭')

