class FileManager:

    def __init__(self,filename,mode,encd):
        self.filename = filename
        self.mode = mode
        self.encd = encd
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode,encoding=self.encd)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
