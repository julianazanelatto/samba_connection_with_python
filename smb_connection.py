import smbclient


class SmbConnection:
    
    def __init__(self, server=None, workgroup="WORKGROUP", user=None, passwd=None):
        """
            Método de inicialização da classe de conexão via protocolo smb
        :param server:
        :param workgroup:
        :param user:
        :param passwd:
        """
        self._server = server
        self._user = user
        self._workgroup = workgroup
        self._passwd = passwd
        self._path = None
        self._folders = []
        self.smb = smbclient

        print("Novos parâmetros de conexão instânciados")

    def _get_connection_parameters(self):
        """
            Método interno da classe
        :return:
        """
        return self._server, self._user, self._passwd

    def get_parameters(self):
        """
            Retorna os parâmetros atuais da conexão
        :return:
        """
        print(self._server, self._user, self._workgroup)

    def set_new_parameters(self, server, user, workgroup, passwd):
        """
            Método de redefinição da conexão
        :param server:
        :param user:
        :param workgroup:
        :param passwd:
        :return:
        """
        self._server = server
        self._user = user
        self._workgroup = workgroup
        self._passwd = passwd

        print("Reconectando ao servidor")
        self.connecting()

    # def set_path_and_folders(self, path, folders):

    def get_path(self):
        """
            Método para definição da string caminho para acesso remoto.
            O caminho é composto pelo server e path dentro do servidor samba

        :return: lista dos caminhos relacionados aos diretórios
        """
        # self._path = path
        self._path = "/sambashare/"
        # self._folders = ["raiz/", "backup/", "docs/"]

        full_paths = ([] if type(self._folders) == list else "")

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
        """
            Método de conexão via procolo smb
        :return: smbclient, registro da sessão
        """
        # expecting server, user, passwd
        _server, _user, _passwd = self._get_connection_parameters()
    
        # return client and session
        return self.smb, self.smb.register_session(_server, _user, _passwd)

    def smb_reading(self, paths):
        """
            Método para varredura do diretório utilizando o protocolo smb

        :param paths: caminhoh do diretório principal
        :return: print de informações
        """
        if type(paths) != list:
            self._list_files(paths)
        else:
            for folders in paths:
                print("Location:", folders)
                self._list_files(folders)

    def _list_files(self, folder):
        """
            Método interno para recuperação de informações do diretório corrente
        :param folder: caminho para o diretório
        :return: sem retorno, print de informações
        """
        dirs = self.smb.listdir(folder)  # every kind of file
        print("Diretório vazio" if len(dirs) == 0 else ("Number of Folders:", len(dirs)))
