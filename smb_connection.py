import smbclient


class SmbConnection:
    
    def __init__(self, server=None, workgroup="WORKGROUP", user=None, passwd=None):
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
        # self._folders = ["raiz/", "backup/", "docs/"]

        if type(self._folders) == list:
            full_paths = []
        else:
            full_paths = ""

        if self._folders:
            for folder in self._folders:
                element = ''.join(["//", self._server, self._path, folder])
                full_paths.append(element)
        else:
            full_paths = ''.join(["//", self._server, self._path])

        if full_paths:
            return full_paths

    # def _get_fullpath(self, final_element):

    def connecting(self):
        # expecting server, user, passwd
        _server, _user, _passwd = self._get_connection_parameters()
    
        # return client and session
        return self.smb, self.smb.register_session(_server, _user, _passwd)

    def smb_reading(self, paths, smb_client: smbclient):
        if type(paths) != list:
            self._list_files(smb_client, paths)
        else:
            for folders in paths:
                print("Location:", folders)
                self._list_files(smb_client, folders)

    def _list_files(self, smb_client: smbclient, folder):
        dirs = smb_client.listdir(folder)  # every kind of file
        print("Diretório vazio" if len(dirs) == 0 else ("Number of Folders:", len(dirs)))
