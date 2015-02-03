from eutester_base import EutesterBase
class ResourceCount(EutesterBase):
    """Get count of each type of cloud resource.
    """

    def gather(self):
        """Gather the data and return an integer

        :returns: Hash of data to send.
        """
        resource_hash = {'ec2': ['instances', 'volumes'],
                         'elb': ['load_balancers']}
        resource_capacity_data = {}
        for service, resource_types in resource_hash.iteritems():
            service_connection = getattr(self.tester, service)
            for resource_type in resource_types:
                function = getattr(service_connection, 'get_all_' + resource_type)
                resource_capacity_data[resource_type] = len(function('verbose'))
        return resource_capacity_data
