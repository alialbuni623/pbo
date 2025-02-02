from django.test import TestCase
from .models import Activity, FoodIntake, VitalSigns
from django.urls import reverse

class ActivityModelTest(TestCase):
    def setUp(self):
        self.activity = Activity.objects.create(
            user_id=1,
            date='2023-01-01',
            steps=1000,
            distance=1.5,
            calories_burned=100
        )

    def test_activity_creation(self):
        self.assertEqual(self.activity.steps, 1000)

class FoodIntakeModelTest(TestCase):
    def setUp(self):
        self.food_intake = FoodIntake.objects.create(
            user_id=1,
            date='2023-01-01',
            food_item='Apple',
            calories=95,
            nutrients={'carbs': 25, 'protein': 0.5}
        )

    def test_food_intake_creation(self):
        self.assertEqual(self.food_intake.food_item, 'Apple')

class VitalSignsModelTest(TestCase):
    def setUp(self):
        self.vital_signs = VitalSigns.objects.create(
            user_id=1,
            date='2023-01-01',
            blood_pressure='120/80',
            weight=70.0,
            blood_sugar=90.0
        )

    def test_vital_signs_creation(self):
        self.assertEqual(self.vital_signs.blood_pressure, '120/80')

class IndexViewTest(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'health/index.html')
