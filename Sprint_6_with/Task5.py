import json
import pickle
from enum import Enum


class FileType(Enum):
    BYTE = 1
    JSON = 2


class SerializeManager:
    def __init__(self, filename, fileType):
        self.filename = filename
        self.fileType = fileType

    def __enter__(self):
        if self.fileType == FileType.BYTE:
            self.file = open(self.filename, 'wb')

        elif self.fileType == FileType.JSON:
            self.file = open(self.filename, 'w')
        return self

    def serialize(self, obj):
        if self.fileType == FileType.BYTE:
            pickle.dump(obj, self.file)

        elif self.fileType == FileType.JSON:
            json.dump(obj, self.file)

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


def serialize(obj, filename, fileType):
    with SerializeManager(filename, fileType) as manager:
        manager.serialize(obj)


if __name__ == "__main__":
    user_dict = {'name': 'Roman', 'id': 8}
    serialize(user_dict, "1", FileType.BYTE)
