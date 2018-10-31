#!/usr/bin/python
# -*- coding: utf-8 -*-
from cloudshell.devices.runners.configuration_runner import ConfigurationRunner
from cloudshell.networking.cisco.flows.cisco_restore_flow import CiscoRestoreFlow
from cloudshell.networking.cisco.flows.cisco_save_flow import CiscoSaveFlow
from cloudshell.networking.cisco.helpers.remote_path import RemotePath
from cloudshell.shell.core.interfaces.save_restore import OrchestrationSavedArtifact


class CiscoConfigurationRunner(ConfigurationRunner):
    @property
    def restore_flow(self):
        return CiscoRestoreFlow(cli_handler=self.cli_handler, logger=self._logger)

    @property
    def save_flow(self):
        return CiscoSaveFlow(cli_handler=self.cli_handler, logger=self._logger)

    @property
    def file_system(self):
        return "flash:"

    def save(self, folder_path='', configuration_type='running', vrf_management_name=None, return_artifact=False):
        """Backup 'startup-config' or 'running-config' from device to provided file_system [ftp|tftp]
        Also possible to backup config to localhost
        :param folder_path:  tftp/ftp server where file be saved
        :param configuration_type: type of configuration that will be saved (StartUp or Running)
        :param vrf_management_name: Virtual Routing and Forwarding management name
        :return: status message / exception
        :rtype: OrchestrationSavedArtifact or str
        """

        if hasattr(self.resource_config, "vrf_management_name"):
            vrf_management_name = vrf_management_name or self.resource_config.vrf_management_name

        self._validate_configuration_type(configuration_type)
        path = RemotePath(remote_path=folder_path, configuration_type=configuration_type,
                          resource_config=self.resource_config, default_fs=self.file_system, api=self._api)
        self.save_flow.execute_flow(folder_path=path,
                                    configuration_type=configuration_type.lower(),
                                    vrf_management_name=vrf_management_name)

        if return_artifact:
            artifact_type = path.remote_path.split(':')[0]
            identifier = path.remote_path.replace("{0}:".format(artifact_type), "")
            return OrchestrationSavedArtifact(identifier=identifier, artifact_type=artifact_type)
        return path.filename
