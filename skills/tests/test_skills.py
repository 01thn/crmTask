from mixer.backend.django import mixer
import pytest


@pytest.mark.django_db
class TestModels:

    def testAddPerson(self):
        mixer.blend('skills.Skills', quantity=1)