from abc import ABC, abstractmethod

class DataSource(ABC):
    @abstractmethod
    def writeData(self, data):
        pass

    @abstractmethod
    def readData(self) -> str:
        pass


class FileDataSource(DataSource):
    def __init__ (self, filename):
        self._file = filename

    def writeData(self, data):
        with open(self._file, "w") as f:
            f.write(data + "\n")


    def readData(self) -> str:
        with open(self._file, "r") as f:
            return f.read()


class EncryptionDecorator(DataSource):
    def __init__ (self, wrapee: DataSource):
        self._wrapee = wrapee

    def writeData(self,data):
        encrypted_data = self._encrypt(data)
        self._wrapee.writeData(encrypted_data)


    def readData(self) -> str:
        encrypted_data = self._wrapee.readData()
        return self._decrypt(encrypted_data)

    def _encrypt(self, data):
        return "".join([chr(ord(ch) + 1) for ch in data])

    def _decrypt(self, data):
        return "".join([chr(ord(ch) - 1) for ch in data])

data_source = FileDataSource("example.txt")
data_exporter = EncryptionDecorator(data_source)
data_source.writeData("Hello world")
print("Data from file: ", data_source.readData())

encrypted_data_source = EncryptionDecorator(data_source)
encrypted_data_source.writeData("Hello world")
print("Encrypted data from file: ", data_source.readData())
print("Decrypted data from file: ", encrypted_data_source.readData())

