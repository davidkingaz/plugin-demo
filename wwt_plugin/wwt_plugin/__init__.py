from extras.plugins import PluginConfig

class WWTPluginConfig(PluginConfig):
    name = 'wwt_plugin'
    verbose_name = ' WWT Analytics for Networks'
    description = 'Gain Network Insights with WWT Analytics'
    version = '0.1'
    author = 'Dave King'
    author_email = 'dave.king@wwt.com'
    base_url = 'wwt-plugin'

config = WWTPluginConfig