# This is a sample Python script.
import smbclient
import smbprotocol
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

SERVER = "192.168.1.5"
PATH = "/sambashare/"
FULL_PATH = ''.join(["//", SERVER, PATH])


def connecting(parameters: list[str]):
    # expecting server, user, passwd
    _server, _user, _passwd = parameters
    smb = smbclient

    # return client and session
    return smb, smbclient.register_session(_server, _user, _passwd)


# Press the green button in the gutter to run the script.2
if __name__ == '__main__':
    # open()
    smb_client, smb_session = connecting(["192.168.1.5",
                                          "user@WORKGROUP",
                                          "123456"])

    if smb_session.session_id:
        dirs = smb_client.listdir(FULL_PATH)  # every kind of file
        print(dirs)
