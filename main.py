import smbclient
import smbprotocol
from smb_connection import SmbConnection


# Press the green button in the gutter to run the script.2
if __name__ == '__main__':
    # open()
    smbConn = SmbConnection()
    smbConn.get_parameters()
    smb_client, smb_session = smbConn.connecting()

    if smb_session.session_id:
        paths = smbConn.get_path()
        if type(paths) != list:
            dirs = smb_client.listdir(paths)  # every kind of file
            print(dirs)
        else:
            for folders in paths:
                dirs = smb_client.listdir(folders)  # every kind of file
                print("Location:", folders)
                print("Number of Folders:", len(dirs))
