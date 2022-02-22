import unittest
import typewise_alert

class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(typewise_alert.infer_breach(110, 50, 100) == 'TOO_HIGH')
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(typewise_alert.infer_breach(80, 50, 100) == 'NORMAL')
    def test_classify_temperature_breach_for_PASSIVE_COOLING(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 35})
    def test_classify_temperature_breach_for_HI_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 45})
    def test_classify_temperature_breach_for_MED_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 40})
    def test_classify_temperature_breachs_for_WRONG_KEY(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('WRONG_KEY') == {"lowerLimit" : 'Not in limits', "upperLimit" : 'Not in limits'})
    def test_classify_temperature_breach_for_NORMAL(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 38)=='NORMAL')
    def test_classify_temperature_breach_for_TOO_LOW(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', -30)=='TOO_LOW')   
    def test_classify_temperature_breach_for_TOO_HIGH(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 50)=='TOO_HIGH')
    def test_classify_temperature_breach_for_WRONG_PARAM(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('WRONG_COOLING', 30)=='WARNING')

        
if __name__ == '__main__':
  unittest.main()
