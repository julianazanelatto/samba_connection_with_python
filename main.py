from smb_connection import SmbConnection


# Press the green button in the gutter to run the script.2
if __name__ == '__main__':
    # open()
    smbConn = SmbConnection(server="192.168.1.5",
                            user="jm",
                            passwd="123456")
    smbConn.get_parameters()
    smb_client, smb_session = smbConn.connecting()

    if smb_session.session_id:

        paths = smbConn.get_path()
        smbConn.smb_reading(paths, smb_client)


