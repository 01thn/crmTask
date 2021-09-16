from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestModels:

    def testAddCompany(self):
        mixer.blend('companies.Companies', quantity=1)