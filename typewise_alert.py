def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

def coolingtype_range(coolingType):
  lowerLimit=0
  coolingType_dict={'PASSIVE_COOLING':{"upperLimit":35},'HI_ACTIVE_COOLING':{"upperLimit":45},'MED_ACTIVE_COOLING':{"upperLimit":40}}					   
  if cooling_Type in coolingType_dict.keys():
    return(coolingType_dict[cooling_Type]) 
  else:
    default={"lowerLimit" : 'Not in limits', "upperLimit" : 'Not in limits'}
    return(default) 

def classify_temperature_breach(coolingType, temperatureInC):
  cooling_limits  = coolingtype_range(coolingType)
  breach = infer_breach(temperatureInC, limits['lowerLimit'], limits['upperLimit'])	
  if 'Not in limits' in cooling_limits.values():
    return "WARNING !!!" 
  else:
    return breach 

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
