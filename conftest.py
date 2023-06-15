from pytest_factoryboy import register

import dbfactory

register(dbfactory.ItemFactory)
register(dbfactory.UserFactory)
