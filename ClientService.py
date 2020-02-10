class ClientService:
    __services = {}

    def __init__(self):
        self.services = {}

    def get_services(self):
        return self.services

    def set_services(self, davy_services):
        i = 0
        while True:
            i += 1
            print('Type 1 to quit or')
            service = input("Select %d service:" % i)
            if service == '1':
                break
            if service in davy_services.keys():
                self.services[service] = davy_services[service]
            else:
                print('There is no services such you input')

    def print_shop_invoice(self):
        print("\nDavy's auto shop invoice")
        total_price = 0
        for service in self.services:
            index = list(self.services.keys()).index(service) + 1
            print("Service %d: %s, $%d" % (index, service, self.services[service]))
            total_price += self.services[service]

        print("\nTotal: $%d" % total_price)
