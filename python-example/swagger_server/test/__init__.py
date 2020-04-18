import logging
import os

from flask_testing import TestCase

from swagger_server.__main__ import create_app


class BaseTestCase(TestCase):

    os.environ["APPLICATION_ENV"] = "Testing"

    def create_app(self):
        logging.getLogger("connexion.operation").setLevel("ERROR")
        app = create_app()

        return app.app
