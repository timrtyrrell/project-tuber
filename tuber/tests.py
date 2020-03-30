from django.test import TestCase
from request_help.models import HelpRequest

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
        self.assertEqual(current_request.location, "CS3240")