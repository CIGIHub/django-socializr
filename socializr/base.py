from collections import Iterable

class SocializrConfig(object):
    '''
    Base behavoir class for integrating social media
    apps with socializr
    '''

    def collect(self):
        '''
        Should be called daily to collect analytics data
        '''
        raise NotImplementedError


_registry = [] # list of SocializrConfig classes


def register(config_or_iterable):
    global _registry

    if not isinstance(config_or_iterable, Iterable):
        config_or_iterable = [config_or_iterable]

    for config in config_or_iterable:
        if config not in _registry:
            _registry.append(config)


def unregister(config_or_iterable):
    global _registry

    if not isinstance(config_or_iterable, Iterable):
        config_or_iterable = [config_or_iterable]

    for config in config_or_iterable:
        if config in _registry:
            _registry.remove(config)

def get_socializr_configs():
    global _registry
    return _registry

