send_email_receipent = { recepient  :  'a.b@c.com',
						 message : {'TOO_LOW'  :  'Hi, the temperature is too low',
						 'TOO_HIGH' :  'Hi, the temperature is too high' } }

def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'
	
def classify_temperature_breach(coolingType, temperatureInC):
	lowerLimit = 0
	cooling_limit_dict = { 'PASSIVE_COOLING'    : 35 ,
						             'HI_ACTIVE_COOLING'  : 45 , 
						             'MED_ACTIVE_COOLING' :  40 }	
	for cooling_value in cooling_limit_dict.keys():
		if cooling_value == coolingType : 
			upperLimit = cooling_limit_dict[cooling_value]
			return infer_breach(temperatureInC, lowerLimit, upperLimit)
		else :
			not_in_range = { 'lowerLimit' : 'Not in range', "upperLimit" : 'Not in range'}
			return not_in_range

def IsbatteryCharValid(batteryChar): 
	batteryChar_types = ['PASSIVE_COOLING', 'HI_ACTIVE_COOLING', 'MED_ACTIVE_COOLING'] 
	if batteryChar in batteryChar_types: 
		return True 
	return False 

def GetBreachType(batteryChar, temperatureInC): 
	if IsbatteryCharValid(batteryChar):
		return classify_temperature_breach(batteryChar, temperatureInC)	
	 else:
		return 	'ERROR' 
		
def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType = GetBreachType(batteryChar, temperatureInC) 
	if breachType!='ERROR' :
		alert = alertTarget(breachType)
	else:
		False 
	return(breachType)

def send_to_controller(breachType): 
	header = 0xfeed 
	command_to_controller = (f'{header}, {breachType}') 
	print(command_to_controller) 
	return(command_to_controller) 
	
def Generate_email_content(breachtype, email_messages): 
	return email_messages[breachtype] 
	
def send_to_email(breachType): 
	mail_content = Generate_email_content(breachType, send_email_receipent['messages']) 
	sending_email = f"To: {send_email_receipent['recepient']} : {mail_content}" 
	print(sending_email) 
	return(sending_email) 


