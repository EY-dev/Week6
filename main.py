from ClientService import ClientService
from DavesService import DavyService

davyService = DavyService()
clientServices = ClientService()

davyService.print_services()
clientServices.set_services(davyService.get_services())

clientServices.print_shop_invoice()




