def describe_city(city, country='Switzerland'): #This defines the variable
    msg = f"{city.title()} is in {country.title()}." #This assigns the variable "msg" the statement and the "city" and "country"
    print(msg)

describe_city('Bern') #This stores the data to the variable "describe_city"
describe_city('Budapest', 'Hungray') #This stores the data to the variable "describe_city"
describe_city('Lugano') #This stores the data to the variable "describe_city"