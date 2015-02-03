import abc
class EutesterBase(object):
    __metaclass__ = abc.ABCMeta
    def __init__(self, tester):
        self.tester = tester
        self.propagate_map_exceptions = True

    @abc.abstractmethod
    def gather(self):
        """Gather the data and return an integer

        :returns: Hash of data to send.
        """
