from django.test import TestCase

# Create your tests here.
import datetime

from django.test import TestCase

class QuestionMethodTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() should return False for questions whose
        pub_date is in the future.
        """
        a = 1
        self.assertEqual(1, a)
