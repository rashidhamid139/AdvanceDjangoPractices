


class Foo:
    def __init__(self):
        print('init called')
        self.init_var = 0

    def __enter__(self):
        print('enter called')
        return self


    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('exxit called')
        if exc_type:
            print(f"exc_type: {exc_type}")
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_traceback}')


    def add_two(self):
        self.init_var =+ 2


class File:
    def __init__(self, filename, method):
        self.file_obj = open(filename, method)


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        
        print("Exception has been handled")
        self.file_obj.close()
        print(exc_traceback())
        return True


with File('test.txt', 'r') as f:
    f.weeen()