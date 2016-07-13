from unittest import TestCase
from cloudshell.networking.cisco.autoload.cisco_generic_snmp_autoload import CiscoGenericSNMPAutoload
from cloudshell.core.logger.qs_logger import get_qs_logger
from cloudshell.snmp.quali_snmp import QualiSnmp


class TestCiscoAutoload(TestCase):
    SUPPORTED_OS = ['NXOS', 'NX-OS', 'IOS', 'Cat OS', 'IOS XR', 'IOSXR', 'IOS-XR']

    def test_is_loads_router_7600_correctly(self):
        print '-----------7600------------'
        ip = '192.168.73.8'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        port_channels = [resource for resource in result.resources if resource.model == 'Generic Port Channel']
        power_ports = [resource for resource in result.resources if resource.model == 'Generic Power Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(ports) == 5)
        self.assertTrue(len(modules) == 2)
        self.assertTrue(len(sub_modules) == 1)
        self.assertTrue(len(port_channels) == 0)
        self.assertTrue(len(power_ports) == 1)
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)
        print len(port_channels)
        print len(power_ports)

    def test_is_loads_router_7609_correctly(self):
        print '-----------7609------------'
        ip = '192.168.73.10'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        port_channels = [resource for resource in result.resources if resource.model == 'Generic Port Channel']
        power_ports = [resource for resource in result.resources if resource.model == 'Generic Power Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 6)
        self.assertTrue(len(ports) == 73)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(len(port_channels) == 5)
        self.assertTrue(len(power_ports) == 1)
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)
        print len(port_channels)
        print len(power_ports)

    def test_is_loads_router_4948_correctly(self):
        print '-----------4948e------------'
        ip = '172.29.168.4'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 1)
        self.assertTrue(len(ports) == 48)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_router_n7k_correctly(self):
        print '-----------n7k------------'
        ip = '172.29.168.5'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 5)
        self.assertTrue(len(ports) == 240)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_router_n3k_correctly(self):
        print '-----------n3k------------'
        ip = '172.29.168.6'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 1)
        self.assertTrue(len(ports) == 54)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_router_ASR9k_correctly(self):
        print '-----------ASR9k------------'
        ip = '172.29.168.7'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 2)
        self.assertTrue(len(ports) == 16)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_router_n7k7010_correctly(self):
        print '-----------n7k7010------------'
        ip = '172.29.168.9'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 0)
        self.assertTrue(len(ports) == 0)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_router_6509_correctly(self):
        print '-----------6509------------'
        ip = '172.29.168.11'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 4)
        self.assertTrue(len(ports) == 68)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_router_7609f12_correctly(self):
        print '-----------7609f12------------'
        ip = '172.29.168.10'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 6)
        self.assertTrue(len(ports) == 73)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_router_7609s_correctly(self):
        print '-----------7609s------------'
        ip = '172.29.168.13'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 6)
        self.assertTrue(len(ports) == 72)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_router_7609s15_correctly(self):
        print '-----------7609sf15------------'
        ip = '172.29.168.14'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 2)
        self.assertTrue(len(ports) == 5)
        self.assertTrue(len(sub_modules) == 1)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_router_6509f12_correctly(self):
        print '-----------6509f12(33)------------'
        ip = '172.29.168.15'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 3)
        self.assertTrue(len(ports) == 30)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_router_7606_correctly(self):
        print '-----------7606------------'
        ip = '172.29.168.17'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 6)
        self.assertTrue(len(ports) == 106)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_router_12816_correctly(self):
        print '-----------12816------------'
        ip = '172.29.168.18'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 10)
        self.assertTrue(len(ports) == 29)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))

    def test_is_loads_router_12416_correctly(self):
        print '-----------12416------------'
        ip = '172.29.168.19'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 10)
        self.assertTrue(len(ports) == 18)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def _check_relative_path(self, resources):
        relative_path = []
        for resource in resources:
            if resource.relative_address in relative_path:
                return False
            else:
                relative_path.append(resource.relative_address)
        return True

    def test_is_loads_n6k_correctly(self):
        print '-----------n6k------------'
        ip = '172.29.168.3'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 2)
        self.assertTrue(len(ports) == 54)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_2950_correctly(self):
        print '-----------2950------------'
        ip = '192.168.42.235'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='Cisco', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 0)
        self.assertTrue(len(ports) == 26)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_n7k_144_correctly(self):
        print '-----------n7k-144------------'
        ip = '172.29.168.29'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 0)
        self.assertTrue(len(ports) == 0)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_n7k_147_correctly(self):
        print '-----------n7k-147------------'
        ip = '172.29.168.30'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 0)
        self.assertTrue(len(ports) == 0)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_n7k_150_correctly(self):
        print '-----------n7k-150------------'
        ip = '172.29.168.31'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 0)
        self.assertTrue(len(ports) == 0)
        self.assertTrue(len(sub_modules) == 0)
        self.assertTrue(self._check_relative_path(result.resources))
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_2951_correctly(self):
        print '-----------2951------------'
        ip = '172.29.168.37'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertTrue(self._check_relative_path(result.resources))
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 1)
        self.assertTrue(len(ports) == 5)
        self.assertTrue(len(sub_modules) == 2)
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_3945_correctly(self):
        print '-----------3945------------'
        ip = '172.29.168.38'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertTrue(self._check_relative_path(result.resources))
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 1)
        self.assertTrue(len(ports) == 6)
        self.assertTrue(len(sub_modules) == 1)
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_isr_4451_correctly(self):
        print '-----------isr_4451------------'
        ip = '172.29.168.39'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertTrue(self._check_relative_path(result.resources))
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 1)
        self.assertTrue(len(ports) == 4)
        self.assertTrue(len(sub_modules) == 1)
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)

    def test_is_loads_asr_1004_correctly(self):
        print '-----------asr_1004------------'
        ip = '172.29.168.40'
        logger = get_qs_logger(log_file_prefix=ip)
        snmp = QualiSnmp(ip=ip, snmp_community='public', logger=logger)
        handler = CiscoGenericSNMPAutoload(logger=logger, snmp_handler=snmp, supported_os=self.SUPPORTED_OS)
        result = handler.discover()
        self.assertIsNotNone(result)
        self.assertIsNotNone(result.resources)
        self.assertIsNotNone(result.attributes)
        chassis = [resource for resource in result.resources if 'Chassis' in resource.name]
        modules = [resource for resource in result.resources if resource.model == 'Generic Module']
        ports = [resource for resource in result.resources if resource.model == 'Generic Port']
        sub_modules = [resource for resource in result.resources if 'Sub Module' in resource.name]
        trash_chrs = [attribute for attribute in result.attributes if type(attribute.attribute_value) is str and
                      '\\s' in attribute.attribute_value]
        if len(trash_chrs) > 0:
            for char in trash_chrs:
                print char.relative_address + ': ' + char.attribute_name + ' = ' + char.attribute_value
        self.assertTrue(self._check_relative_path(result.resources))
        self.assertFalse(len(trash_chrs) > 0)
        self.assertTrue(len(chassis) == 1)
        self.assertTrue(len(modules) == 2)
        self.assertTrue(len(ports) == 6)
        self.assertTrue(len(sub_modules) == 2)
        print len(chassis)
        print len(ports)
        print len(modules)
        print len(sub_modules)
