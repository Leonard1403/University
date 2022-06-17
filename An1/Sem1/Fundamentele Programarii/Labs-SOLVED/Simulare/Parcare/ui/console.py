class Console:
    def __init__(self,service):
        self.__service = service

    def __cerinta1(self):
        strada = input("Introduceti strada: ")
        iduri = self.__service.search_strada(strada)
        for id in iduri:
            print(id)

    def __cerinta2(self):


    def show_ui(self):

        parcari = self.__service.get_all()
        for parcare in parcari:
            print(parcare)

        while True:

            print("1.Dându-se o stradă, să se afișeze toate locurile care se află pe strada respectivă, ordonate"
                    "descrescător după nume. Să se afișeze un mesaj special în caz că nu există locuri pe"
                    "acea stradă")
            print("2.Pentru fiecare stradă, afișați numele celui mai utilizat loc de pe strada respectivă")
            print("3.Exit")

            ans = input("Introduceti cerinta: ")
            if ans == '1':
                self.__cerinta1()
            elif ans == '2':
                self.__cerinta2()
            elif ans == '3':
                return
