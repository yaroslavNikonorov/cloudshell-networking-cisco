from collections import OrderedDict
import re

from cloudshell.networking.cisco.cisco_command_actions import CiscoCommandActions
from cloudshell.networking.devices.flows.configuration_flows import SaveConfigurationFlow


class CiscoSaveFlow(SaveConfigurationFlow):
    def __init__(self, cli_handler, logger, resource_name):
        super(CiscoSaveFlow, self).__init__(cli_handler, logger, resource_name)
        self._command_actions = CiscoCommandActions()

    def save_config(self, configuration_type, full_path, vrf_management_name):
        action_map = self._prepare_action_map(source_file=configuration_type, destination_file=full_path)
        with self._cli_handler.get_cli_operations(self._cli_handler.enable_mode) as session:
            self._command_actions.copy(session, self._logger, configuration_type, full_path,
                                       vrf_management_name, action_map)

    def _prepare_action_map(self, source_file, destination_file):
        action_map = OrderedDict()
        host = None
        if '://' in destination_file:
            destination_file_data_list = re.sub('/+', '/', destination_file).split('/')
            host = destination_file_data_list[1]
            source_file_name = source_file.split(':')[-1].split('/')[-1]
            action_map[r'[\[\(]{}[\)\]]'.format(
                destination_file_data_list[-1])] = lambda session, logger: session.send_line('', logger)

            action_map[r'[\[\(]{}[\)\]]'.format(source_file_name)] = lambda session, logger: session.send_line('',
                                                                                                               logger)
        else:
            destination_file_name = destination_file.split(':')[-1].split('/')[-1]
            source_file_name = source_file.split(':')[-1].split('/')[-1]
            action_map[r'(?!/)[\[\(]{}[\)\]]'.format(
                destination_file_name)] = lambda session, logger: session.send_line('', logger)
            action_map[r'(?!/)[\[\(]{}[\)\]]'.format(
                source_file_name)] = lambda session, logger: session.send_line('', logger)
        if host:
            if '@' in host:
                storage_data = re.search(r'^(?P<user>\S+):(?P<password>\S+)@(?P<host>\S+)', host)
                if storage_data:
                    storage_data_dict = storage_data.groupdict()
                    host = storage_data_dict['host']
                    password = storage_data_dict['password']

                    action_map[r'[Pp]assword:'.format(
                        source_file)] = lambda session, logger: session.send_line(password, logger)

                else:
                    host = host.split('@')[-1]
            action_map[r"(?!/){}(?!/)".format(host)] = lambda session, logger: session.send_line('', logger)
        return action_map
