class Login:
    def __init__(self):
        pass

    def login_file(self):
        try:
            file = open('login.txt', 'x')
            file.write(input('login: ') + '\n')
            file.write(input('senha: '))
            file.close()
        except:
            pass
        finally:
            file = open('login.txt', 'r')
            self.usuario = {'login': file.readline().replace('\n', ''),
                            'password': file.readline()}
            file.close()