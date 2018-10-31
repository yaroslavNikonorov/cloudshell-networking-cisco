import re

import time

from os.path import join

from cloudshell.devices.networking_utils import UrlParser


class RemotePath(object):
    def __init__(self, remote_path, default_fs, resource_config, api, configuration_type="running"):
        self._remote_path = remote_path
        if not self._remote_path:
            self._parsed_remote_path = UrlParser.parse_url(resource_config.backup_location)
        else:
            self._parsed_remote_path = UrlParser.parse_url(remote_path)
        self._api = api
        self._default_file_system = default_fs
        self._configuration_type = configuration_type
        self._password = None
        self._host = None
        self._user = None
        self._scheme = None
        self._filename = None
        self._resource_config = resource_config

    @property
    def remote_path(self):
        if not self._remote_path:
            self._remote_path = UrlParser.build_url(self._parsed_remote_path.update({UrlParser.HOSTNAME: self.host,
                                                                                     UrlParser.USERNAME: self.username,
                                                                                     UrlParser.PASSWORD: self.password
                                                                                     }))
            if not self._remote_path:
                self._remote_path = self._default_file_system
        return join(self._remote_path, self.filename)

    @property
    def username(self):
        if not self._user:
            self._user = self._parsed_remote_path.get(UrlParser.USERNAME) or self._resource_config.backup_user
        return self._user

    @property
    def password(self):
        if not self._password:
            self._password = self._parsed_remote_path.get(UrlParser.PASSWORD) or \
                             self._api.DecryptPassword(self._resource_config.backup_password).Value
        return self._password

    @property
    def host(self):
        if not self._host:
            self._host = self._parsed_remote_path.get(UrlParser.HOSTNAME)
        return self._parsed_remote_path.get(UrlParser.HOSTNAME) or self._resource_config.backup_location

    @property
    def scheme(self):
        if not self._scheme:
            self._scheme = self._parsed_remote_path.get(UrlParser.SCHEME) or self._resource_config.backup_scheme
        return self._scheme

    @property
    def filename(self):
        if not self._filename:
            system_name = re.sub('\s+', '_', self._resource_config.name)[:23]
            time_stamp = time.strftime("%d%m%y-%H%M%S", time.localtime())
            self._filename = '{0}-{1}-{2}'.format(system_name, self._configuration_type.lower(), time_stamp)
        return self._filename

    @filename.setter
    def filename(self, value):
        self._filename = value

    @property
    def config_type(self):
        return self._configuration_type
