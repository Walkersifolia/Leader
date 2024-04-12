from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'leader',
    'version': '1.0.0',
    'name': 'Leader-Plugin',
    'description': 'give a player marker',
    'author': 'WalkerTian',
    'link': 'https://github.com/Walkersifolia/Leader'
}

def is_admin(server: ServerInterface, player: str) -> bool:
    return server.get_permission_level(player) >= 3

def on_user_info(server: ServerInterface, info: Info):
    if info.is_player:
        if info.content == '!!leader':
            server.execute('effect give {} minecraft:glowing 1000000'.format(info.player))
        elif info.content == '!!unleader':
            server.execute('effect clear {} minecraft:glowing'.format(info.player))
        elif info.content == '!!leader all':
            if is_admin(server, info.player):
                server.execute('effect give @a minecraft:glowing 1000000')
            else:
                server.reply(info, '你没有权限执行这个指令')
        elif info.content.startswith('!!unleader all'):
            if is_admin(server, info.player):
                server.execute('effect clear @a minecraft:glowing')
            else:
                server.reply(info, '你没有权限执行这个指令')

def on_load(server: ServerInterface, old_module):
    server.register_help_message('!!leader', '高亮自己')
    server.register_help_message('!!unleader', '取消高亮')
    server.register_help_message('!!leader all', '让所有玩家发光（仅管理员可用）')
    server.register_help_message('!!unleader all', '取消让所有玩家发光（仅管理员可用）')
    server.register_event_listener('minecraft.console.info', on_user_info)