from survey import NoNanmeSurvey
import unittest

class TestNONameSurvey(unittest.TestCase):
    def setUp(self):
        question="what language do you want to learn first?"
        self.my_survey=NoNanmeSurvey(question)
        self.responses=["chinese","english","yueyu"]
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    def test_three_response(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)
unittest.main()