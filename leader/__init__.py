from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'leader',
    'version': '1.0.0',
    'name': 'Leader-Plugin',
    'description': 'give a player marker',
    'author': 'WalkerTian',
    'link': 'https://github.com/Walkersifolia/Leader'
}

def on_user_info(server: ServerInterface, info: Info):
    if info.is_player:
        if info.content == '!!leader':
            server.execute('effect give {} minecraft:glowing 1000000'.format(info.player))
        elif info.content == '!!unleader':
            server.execute('effect clear {} minecraft:glowing'.format(info.player))

def on_load(server: ServerInterface, old_module):
    server.register_help_message('!!leader', '高亮自己')
    server.register_help_message('!!unleader', '取消高亮')
    server.register_event_listener('minecraft.console.info', on_user_info)
