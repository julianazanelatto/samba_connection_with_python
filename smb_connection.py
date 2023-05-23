import smbclient


class SmbConnection:
    
    def __init__(self, server=None, workgroup=None, user=None, passwd=None):
        self._server = server
        self._user = user
        self._workgroup = workgroup
        self._passwd = passwd
        self._path = None
        self._folders = []
        self.smb = smbclient

        print("Novos parâmetros de conexão instânciados")

    def _get_connection_parameters(self):
        return self._server, self._user, self._passwd

    def get_parameters(self):
        print(self._server, self._user, self._workgroup)

    def set_new_parameters(self, server, user, workgroup, passwd):
        self._server = server
        self._user = user
        self._workgroup = workgroup
        self._passwd = passwd

    # def set_path_and_folders(self, path, folders):

    def get_path(self):
        # self._path = path
        self._path = "/sambashare/"
        self._folders = ["raiz/", "backup/", "docs/"]

        if type(self._folders) == list:
            full_paths = []
        else:
            full_paths = ""

        for folder in self._folders:
            element = ''.join(["//", self._server, self._path, folder])
            full_paths.append(element)

        if full_paths:
            return full_paths

    # def _get_fullpath(self, final_element):

    def connecting(self):
        # expecting server, user, passwd
        _server, _user, _passwd = self._get_connection_parameters()
    
        # return client and session
        return self.smb, self.smb.register_session(_server, _user, _passwd)
