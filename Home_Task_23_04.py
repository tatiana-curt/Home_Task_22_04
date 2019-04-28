import datetime

class FileCreator:
    def __init__(self, path):
        self.path = path
        self.create_time = datetime.datetime.now()

    def __enter__(self):
        self.file = open(self.path)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        self.end_time = datetime.datetime.now()
        print('Время работы кода: ', self.end_time - self.create_time)

# Тест на запись:
# if __name__ == '__main__':
#
#     with FileCreator ('recipes2.txt') as file:
#         file.write('Print')




