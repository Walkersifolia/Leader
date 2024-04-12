from mcdreforged.api.all import *

from leader import my_lib


def on_load(server: PluginServerInterface, old):
    server.logger.info(server.tr('my_plugin.a_message'))
    my_lib.do_something()
