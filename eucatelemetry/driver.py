import collectd
from eucaops import Eucaops
from stevedore.extension import ExtensionManager
CREDPATH = '/root'
PLUGINS = None
NAMESPACE = 'eucatelemetry'


def configure_callback(conf):
    """Receive configuration block"""
    global CREDPATH
    for node in conf.children:
        if node.key == 'Credpath':
            CREDPATH = node.values[0]
        else:
            collectd.warning('eucatelemetry plugin: Unknown config key: %s.'
                             % node.key)
    collectd.info('Configured eucatelemetry with credpath=%s' % (CREDPATH))


def init_callback():
    tester = Eucaops(credpath=CREDPATH)
    global PLUGINS
    PLUGINS = ExtensionManager(
        namespace=NAMESPACE,
        invoke_on_load=True,
        invoke_args=(tester,)
    )
    PLUGINS.propagate_map_exceptions = True


def send_data(ext):
    data = ext.obj.gather()
    for key in data:
        vl = collectd.Values(type='gauge')
        vl.plugin = NAMESPACE + '.' + ext.name + '.' + key
        collectd.info('Dispatching: ' + vl.plugin + ':' + str(data[key]))
        vl.dispatch(values=[data[key]])


def read_callback(data=None):
    collectd.info('Read called in eucatelemetry')
    PLUGINS.map(send_data)

collectd.register_config(configure_callback)
collectd.register_init(init_callback)
collectd.register_read(read_callback)
