from socializr.base import SocializrConfig, register


class FacebookConfig(SocializrConfig):
    def collect(self):
        pass


register(FacebookConfig)

