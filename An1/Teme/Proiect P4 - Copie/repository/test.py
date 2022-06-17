from domain.entities import Clienti

class ClientiFileRepository:
    """
    In clasa Repo vom depozita toate datele pentru clienti si carti
    """
    def __init__(self,filename):
        self.__filename = filename

    def __load_from_file(self):

        try:
            f = open(self.__filename,'r')
        except ValueError as ve:
            print(colored(ve,'red'))

        all_clienti = []
        lines = f.readlines()

        for line in lines:
            client_id , client_nume , client_cnp = [token.strip() for token in line.split(';')]
            client_id = int(client_id)
            clienti = Clienti(client_id,client_nume,client_cnp)
            all_clienti.append(clienti)
        f.close()
        return all_clienti

    def get_all(self):
        return self.__load_from_file()

def test():
    da_test = ClientiFileRepository('test_clienti_repo.txt')
    print(len(da_test.get_all()))

def TEST():
    test()

TEST()