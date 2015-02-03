from eutester_base import EutesterBase
import timeit
class APILatency(EutesterBase):
    """A very basic formatter.
    """

    def gather(self):
        """Gather the data and return an integer

        :returns: Hash of data to send.
        """
        resource_hash = {'ec2': ['instances', 'volumes'],
                         'elb': ['load_balancers']}
        resource_latency_data = {}
        for service, resource_types in resource_hash.iteritems():
            service_connection = getattr(self.tester, service)
            for resource_type in resource_types:
                function = getattr(service_connection, 'get_all_' + resource_type)
                resource_latency_data[resource_type] = timeit.timeit(function, number=1)
        print resource_latency_data
        return resource_latency_data
