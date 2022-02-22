
def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  elif value > upperLimit:
    return 'TOO_HIGH'
  else:
    return 'NORMAL'


def classify_temperature_breach(coolingType, temperatureInC):
	lowerLimit = 0
	coolingType_dict={"PASSIVE":35,"HI_ACTIVE":45,"MED_ACTIVE":40}
	cool_range = coolingtype_range(coolingType)
	for cooling_type in cool_range.keys(): 
		if cooling_type==coolingType: 
			upperLimit=cool_range[cooling_type] 
	breachType=infer_breach(temperatureInC,lowerLimit,upperLimit) 
	return breachType 


def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType =\
    classify_temperature_breach(batteryChar['coolingType'], temperatureInC)
  if alertTarget == 'TO_CONTROLLER':
    send_to_controller(breachType)
  elif alertTarget == 'TO_EMAIL':
    send_to_email(breachType)


def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')


def send_to_email(breachType):
  recepient = "a.b@c.com"
  if breachType == 'TOO_LOW':
    print(f'To: {recepient}')
    print('Hi, the temperature is too low')
  elif breachType == 'TOO_HIGH':
    print(f'To: {recepient}')
    print('Hi, the temperature is too high')
