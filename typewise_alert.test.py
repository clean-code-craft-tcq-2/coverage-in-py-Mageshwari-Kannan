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
        self.assertTrue(typewise_alert.coolingtype_range('PASSIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 35})
    def test_classify_temperature_breach_for_HI_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.coolingtype_range('HI_ACTIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 45})
    def test_classify_temperature_breach_for_MED_ACTIVE_COOLING(self):
        self.assertTrue(typewise_alert.coolingtype_range('MED_ACTIVE_COOLING') == {"lowerLimit" : 0, "upperLimit" : 40})
    def test_classify_temperature_breachs_for_OUT_OF_LIMITS(self):
        self.assertTrue(typewise_alert.coolingtype_range('OUT_OF_LIMITS') == {"lowerLimit" : 'Not in limits', "upperLimit" : 'Not in limits'})
        
    def test_classify_temperature_breach_for_TOO_LOW(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', -50)=='TOO_LOW') 
    def test_classify_temperature_breach_for_NORMAL(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 36)=='NORMAL')  
    def test_classify_temperature_breach_for_TOO_HIGH(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 47)=='TOO_HIGH')    
    def test_classify_temperature_breach_for_TOO_HIGH(self):
        self.assertTrue(typewise_alert.classify_temperature_breach('NO_COOLING', 80)=='WARNING')

        
if __name__ == '__main__':
  unittest.main()
