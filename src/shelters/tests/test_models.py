from django.test import TestCase
from shelters.tests import factories


class ShelteryTest(TestCase):

    def test_shelter_str(self):
        shelter = factories.ShelterFactory()
        expected = f'{shelter.name} ({shelter.city.name})'
        self.assertEqual(expected, str(shelter))
