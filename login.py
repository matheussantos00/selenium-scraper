class Login:
    def __init__(self):
        try:
            file = open('login.txt', 'x')
            file.write(input('email: ') + '\n')
            file.write(input('senha: '))
            file.close()
        except:
            pass
        finally:
            file = open('login.txt', 'r')
            self.usuario = {'email': file.readline().replace('\n', ''),
                            'senha': file.readline()}
            file.close()

    def login_file(self):
        pass