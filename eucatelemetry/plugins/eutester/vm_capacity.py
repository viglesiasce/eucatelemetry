from eutester_base import EutesterBase
class VMCapacity(EutesterBase):
    """A very basic formatter.
    """

    def gather(self):
        """Gather the data and return an integer

        :returns: Hash of data to send.
        """
        vm_capacity_data = {}
        vm_types = [vm_type.name for vm_type in self.tester.ec2.get_all_instance_types()]
        for vm_type in vm_types:
            try:
                vm_capacity_data[vm_type.replace('.', '_')] = self.tester.get_available_vms(vm_type)
            except Exception:
                print 'Unable to find availability for: ' + vm_type
        return vm_capacity_data
