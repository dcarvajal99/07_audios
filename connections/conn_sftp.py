import paramiko


class Sftp():

    def __init__(self, host , port, username, password):
        self.host = host 
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(self.host, port=self.port, username=self.username, password=self.password)
        self.sftp = self.client.open_sftp()

    def close(self):
        self.sftp.close()
        self.client.close()

    def get(self, remote_path, local_path):
        self.sftp.get(remote_path, local_path)

    def put(self, local_path, remote_path):
        self.sftp.put(local_path, remote_path)

    def listdir(self, path):
        return self.sftp.listdir(path)
    
    def chdir(self, path):
        self.sftp.chdir(path)
    
    def mkdir(self, path):
        self.sftp.mkdir(path)
