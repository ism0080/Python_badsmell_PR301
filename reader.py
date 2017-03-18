class FileReader(object):
    def __init__(self):
        pass

    def read(self, filename):
        try:
            with open(filename, 'r') as file:
                file_data = file.read()
                # splits on newline
                group = file_data.split('\n')
                line = []
                list_of_dictionaries = []
                i = 0
                for x in group:
                    line.extend([group[i].split(', ')])
                    list_of_dictionaries.extend([i])
                    i += 1
                for empty in list_of_dictionaries:
                    list_of_dictionaries[empty] = dict(e.split('=') for e in line[empty])
            return list_of_dictionaries
        except IOError as err:
            print("The exception is: ", err)
            pass

