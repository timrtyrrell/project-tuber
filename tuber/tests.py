from django.test import TestCase
from request_help.models import HelpRequest
from register.models import UserProfile

class BasicTests(TestCase):
    def test_isTrue(self):
        self.assertEqual(True, True)
    def test_isFalse(self):
        self.assertEqual(False, False)
class helpRequestTests(TestCase):
    def test_isDefault(self):
        current_request = HelpRequest(class_name = "CS3240", topic = "I need help")
        self.assertEqual(current_request.location, "green")
    def test_isNewLocation(self):
        current_request = HelpRequest(class_name = "CS3240", topic = "I need help", location = "Clem Library")
        self.assertEqual(current_request.location, "Clem Library")
    def test_isTopic(self):
        current_request = HelpRequest(class_name = "CS3240", topic = "I need help", location = "Clem Library")
        self.assertEqual(current_request.topic, "I need help")
    def test_isClassName(self):
        current_request = HelpRequest(class_name = "CS3240", topic = "I need help", location = "Clem Library")
        self.assertEqual(current_request.class_name, "CS3240")

class tutorStatusTests(TestCase): 
    def test_isDefaultStatus(self):
        current_tutor = UserProfile(name="Bob", phone="434-123-4567")
        self.assertEqual(current_tutor.status, False)
    def test_isDefaultLocation(self):
        current_tutor = UserProfile(name="Bob", phone="434-123-4567")
        self.assertEqual(current_tutor.tutor_location, "Anywhere")
    def test_isNewLocation(self):
        current_tutor = UserProfile(name = "Bobby", phone="123-434-3567", tutor_location = "Clem Library")
        self.assertEqual(current_tutor.tutor_location, "Clem Library")

class registerTests(TestCase): 
    def test_isDefault(self):
        current_user = UserProfile()
        self.assertEqual(current_user.name, "")
    def test_isPhone(self):
        current_user = UserProfile(name="Bob", phone="434-123-4567")
        self.assertEqual(current_user.phone, "434-123-4567")
    def test_isName(self):
        current_user = UserProfile(name = "Bobby", phone="123-434-3567")
        self.assertEqual(current_user.name, "Bobby")