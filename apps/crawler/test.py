from certifi import *
from selenium import webdriver


def testSouthWest():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.southwest.com/air/booking/select.html?adultPassengersCount=1&departureDate=2019-02-13&departureTimeOfDay=ALL_DAY&destinationAirportCode=BOS&fareType=USD&originationAirportCode=SJC&passengerType=ADULT&promoCode=&reset=true&returnDate=2019-03-08&returnTimeOfDay=ALL_DAY&seniorPassengersCount=0&tripType=roundtrip')
    f = open('siteContents.txt', 'w')
    f.write(str(driver.page_source))
    print(driver.page_source)


    f.close()
    return driver


browser = testSouthWest() 
