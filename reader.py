class FileReader(object):
    def __init__(self):
        self.line = []
        self.list_of_dictionaries = []

    def read(self, filename):
        # COMMENT SMELL
        try:
            with open(filename, 'r') as file:
                file_data = file.read()
                # splits on newline
                group = file_data.split('\n')
                i = 0
                # splits on comma separation
                for x in group:
                    self.line.extend([group[i].split(', ')])
                    self.list_of_dictionaries.extend([i])
                    i += 1
                # adds each dictionary to a dictionary to create a list of dictionaries
                for empty in self.list_of_dictionaries:
                    self.list_of_dictionaries[empty]\
                        = dict(e.split('=') for e in self.line[empty])
            return self.list_of_dictionaries
        except IOError as err:
            print("The exception is: ", err)
            pass

