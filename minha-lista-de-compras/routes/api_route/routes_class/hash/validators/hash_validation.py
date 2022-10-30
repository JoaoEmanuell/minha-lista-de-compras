class HashValidation:
    def __init__(self, value : str) -> None:
        self.__value = value

    def _validate(self) -> str :
        if type(self.__value) != str :
            raise TypeError('Invalid query parameter')
        self.__value = self.__value.strip()
        self.__len_verification()
        self.__none_verification()
        return self.__value.encode('utf-8')
    
    def __len_verification(self):
        if len(self.__value) == 0 :
            raise ValueError('Value cannot be empty')

    def __none_verification(self):
        if self.__value is None :
            raise ValueError('Value cannot be None')