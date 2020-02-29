from django.test import TestCase
from request_help.models import HelpRequest

class BasicTests(TestCase):
    def isTrue(self):
        self.assertEqual(True, True)
    def isFalse(self):
        self.assertEqual(False, False)
class helpRequestTests(TestCase):
    def isDefault(self):
        current_request = HelpRequest(class_name = "CS3240", topic_text = "I need help")
        self.assertEqual(current_request.location, "Rice Hall")
    def isNewLocation(self):
        current_request = HelpRequest(class_name = "CS3240", topic_text = "I need help", location = "Clem Library")
        self.assertEqual(current_request.location, "Clem Library")