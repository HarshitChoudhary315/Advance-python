class RoleBean:
    def __init__(self):
        self.__id= 0
        self.__name = ''
        self.description = ''

    def get_id(self):
        return self.__id

    def set_id(self,id):
        self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self,name):
        self.__name = name

    def get_description(self):
        return self.__description

    def set_description(self,description):
        self.__set_description = description

