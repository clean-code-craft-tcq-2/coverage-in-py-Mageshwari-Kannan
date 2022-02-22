import unittest
import typewise_alert

class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(typewise_alert.infer_breach(110, 50, 100) == 'TOO_HIGH')
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(typewise_alert.infer_breach(80, 50, 100) == 'NORMAL')
    def test_infers_breach_as_per_limits(self):
        self.assertTrue(typewise_alert.infer_breach(80, 50, 100) == 'NORMAL')
    def test_classify_temperature_breach_for_PASSIVE_COOLING(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 35})	
    def test_classify_temperature_breach_for_HI_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING') == {"lowerLimit" : 41, "upperLimit" : 45})	  
    def test_classify_temperature_breach_for_MED_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING') == {"lowerLimit" : 35, "upperLimit" : 40})		
    
if __name__ == '__main__':
  unittest.main()
