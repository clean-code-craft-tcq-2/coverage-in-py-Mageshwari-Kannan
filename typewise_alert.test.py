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
        self.assertTrue(typewise_alert.classify_temperature_breach(-2, 'PASSIVE_COOLING') == 'TOO_LOW')	
    def test_classify_temperature_breach_for_PASSIVE_COOLING(self):
        self.assertTrue(typewise_alert.classify_temperature_breach(100, 'PASSIVE_COOLING') == 'TOO_HIGH')	
    def test_classify_temperature_breach_for_PASSIVE_COOLING(self):
        self.assertTrue(typewise_alert.classify_temperature_breach(10, 'PASSIVE_COOLING') == 'NORMAL')	
        
    def test_classify_temperature_breach_for_HI_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.classify_temperature_breach(-15, 'HI_ACTIVE_COOLING') == 'TOO_LOW')	
    def test_classify_temperature_breach_for_HI_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.classify_temperature_breach(120, 'HI_ACTIVE_COOLING') == 'TOO_HIGH')
    def test_classify_temperature_breach_for_HI_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.classify_temperature_breach(26, 'HI_ACTIVE_COOLING') == 'NORMAL')
        
    def test_classify_temperature_breach_for_MED_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.classify_temperature_breach(-5, 'MED_ACTIVE_COOLING') == 'TOO_LOW')		
    def test_classify_temperature_breach_for_MED_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.classify_temperature_breach(110, 'MED_ACTIVE_COOLING') == 'TOO_HIGH')	
    def test_classify_temperature_breach_for_MED_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.classify_temperature_breach(20, 'MED_ACTIVE_COOLING') == 'NORMAL')	
        
if __name__ == '__main__':
  unittest.main()
