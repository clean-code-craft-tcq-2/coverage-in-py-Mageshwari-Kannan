import unittest
import typewise_alert

class TypewiseTest(unittest.TestCase):
    def test_infers_breach_as_per_low_limits(self):
        self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    def test_infers_breach_as_per_high_limits(self):
        self.assertTrue(typewise_alert.infer_breach(110, 50, 100) == 'TOO_HIGH')
    def test_infers_breach_as_per_normal_limits(self):
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
        
    def test_send_to_controller_too_high_breachType(self):
        self.assertTrue(typewise_alert.send_to_controller('TOO_HIGH') == f'{0xfeed}, TOO_HIGH')
    def test_send_to_controller_too_low_breachType(self):
        self.assertTrue(typewise_alert.send_to_controller('TOO_LOW') == f'{0xfeed}, TOO_LOW')

    def test_check_and_alert_to_controller(self):
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER',-5,"PASSIVE_COOLING") == f'{0xfeed}, TOO_LOW')
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 100, "PASSIVE_COOLING")==f'{0xfeed}, TOO_HIGH')
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 16, "PASSIVE_COOLING")==f'{0xfeed}, NORMAL')
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER',-18, "HI_ACTIVE_COOLING")==f'{0xfeed}, TOO_LOW')
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 260, "HI_ACTIVE_COOLING")==f'{0xfeed}, TOO_HIGH')
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 40, "HI_ACTIVE_COOLING")==f'{0xfeed}, NORMAL')
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', -28, "MED_ACTIVE_COOLING")==f'{0xfeed}, TOO_LOW')
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 136, "MED_ACTIVE_COOLING")==f'{0xfeed}, TOO_HIGH')
        self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER',30, "MED_ACTIVE_COOLING")==f'{0xfeed}, NORMAL')        
        
if __name__ == '__main__':
  unittest.main()
