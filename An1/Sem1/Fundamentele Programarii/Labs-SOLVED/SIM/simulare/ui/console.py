from service.vacanta_service import BookingInquiry

class Console:
    def __init__(self,service):
        self.__service = service

    def __cerinta1(self):
        '''
        Functia de la cerinta1
        :return: None
        '''

        tip = input("Introduceti tipul: ")
        vacante = self.__service.search_tip(tip)
        for vacanta in vacante:
            print(vacanta)

    def __cerinta2(self):
        '''
        Functia de la cerinta 2
        :return: None
        '''
        id = input("Introduceti id-ul: ")
        try:
            buget = int(input("Introduceti buget: "))
        except ValueError:
            print("Bugetul trebuie sa fie numerar")

        locatie = self.__service.search_id(id)
        if locatie is None:
            print("Nu exista locatia cu acest id")
            return
        # print(locatie)
        rezervare = BookingInquiry(locatie,buget)
        print("Denumire: " + str(rezervare.get_denumire()) + ", Tipul: " + str(rezervare.get_tipul()) + ", Numarul de zile: " + str(rezervare.get_number_of_days()))
    def __getall(self):
        return self.__service.getall()

    def show_ui(self):

        # all_vacante = self.__getall()
        # for vacanta in all_vacante:
        #     print(vacanta)

        while True:
            print('1.Căutarea de locații pe baza tipului. Utilizatorul introduce un string, aplicația tipărește toate locațiile'
                  '\ndisponibile pentru care tipul conține stringul dat de utilizator.')
            print('2.Returnare informații privind rezervarea unei locatii. Utilizatorul introduce id-ul locatiei și'
                  '\nbugetul său. Aplicația tipărește numele locației, tipul, și numărul de zile pe care și-l poate permite'
                  '\nutilizatorul în acea locație.')
            print('3.Exit')
            ans = input("Comanda: ")

            if ans == '1':
                self.__cerinta1()
            elif ans == '2':
                self.__cerinta2()
            elif ans == '3':
                return