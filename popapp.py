from tg import expose, TGController, AppConfig
from controllers import RootController
from controllers import ArtistFileService

service = ArtistFileService.ArtistFileService('controllers/artists.json')
controller = RootController.RootController(service)

config = AppConfig(minimal=True, root_controller=controller)

application = config.make_wsgi_app()

from wsgiref.simple_server import make_server

print("Serving on port 8080...")
httpd = make_server('', 8080, application)
httpd.serve_forever()

