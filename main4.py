from selenium import webdriver
from random import randint
from time import sleep

def random_sleep():
    sleep(randint(20, 100))

def card_info(card_url):
    driver.get(card_url)
    soldprice = driver.find_elements_by_tag_name('h3')
    solddate = driver.find_elements_by_xpath('//*[@class="time"]')
    print(cards.get(_)[0] + " " + cards.get(_)[1] + " " + cards.get(_)[2] + " " + cards.get(_)[3] + " Sold Price: $" +
          soldprice[0].get_attribute('data-soldandshipping') + " " + solddate[0].text)

def construct_url(_):
    card_url = 'https://mavin.io/search?q=' + cards.get(_)[2] + '+' + cards.get(_)[3] + '+' + cards.get(_)[0] + '+' \
               + cards.get(_)[1] + '+' + cards.get(_)[4] + \
               '+-tiffany+-autographed+-glossy+-signed+-iconic+-whited+-case+-dna+-auto+-nnof+-stickercard+-archives+-' \
               'rare+-name+-project+&bt=sold&sort=PricePlusShippingHighest&cat=213'
    return card_url

driver = webdriver.Firefox()

cards = {1: ['Kevin', 'Romine', '1989', 'Fleer', '98'],
         2: ['Will', 'Clark', '1989', 'Fleer', '325'],
         3: ['Greg', 'Maddux', '1989', 'Fleer', '431'],
         4: ['Don', 'Mattingly', '1989', 'Fleer', '258'],
         5: ['Wade', 'Boggs', '1989', 'Fleer', '81'],
         6: ['Ozzie', 'Smith', '1989', 'Fleer', '463'],
         7: ['Jose', 'Canseco', '1989', 'Fleer', '5'],
         8: ['Wally', 'Joyner', '1989', 'Fleer', '481'],
         9: ['Mark', 'McGwire', '1989', 'Fleer', '17'],
         10: ['Rickey', 'Henderson', '1989', 'Fleer', '254'],
         11: ['Power', 'Center', '1989', 'Fleer', '639'],
         12: ['Fernando', 'Valenzuela', '1989', 'Fleer', '76'],
         13: ['Ryan', 'Sandberg', '1989', 'Fleer', '437'],
         14: ['Bobby', 'Bonilla', '1989', 'Fleer', '203'],
         15: ['Roger', 'Clemens', '1989', 'Fleer', '85'],
         16: ['NL', 'ALL Stars', '1989', 'Fleer', '631'],
         17: ['Roberto', 'Alomar', '1989', 'Fleer', '299'],
         18: ['Like Father', 'Like Sons', '1989', 'Fleer', '630'],
         19: ['Carlton', 'Fisk', '1989', 'Fleer', '495'],
         20: ['Tom', 'Glavine', '1989', 'Fleer', '591'],
         21: ['Darryl', 'Strawberry', '1989', 'Fleer', '10'],
         22: ['Sandy', 'Alomar', '1989', 'Fleer', '300'],
         23: ['Cecil', 'Fielder', '1989', 'Fleer', '232'],
         24: ['John', 'Smoltz', '1989', 'Fleer', '602'],
         25: ['Dennis', 'Eckersley', '1989', 'Fleer', '7'],
         26: ['Speed', 'Power', '1989', 'Fleer', '628'],
         27: ['George', 'Brett', '1989', 'Fleer', '277'],
         28: [' ', ' ', '1989', 'Fleer', '632'],
         29: ['Robin', 'Yount', '1989', 'Fleer', '200'],
         30: ['Tony', 'Gwynn', '1989', 'Fleer', '305'],
         31: ['Kirby', 'Puckett', '1989', 'Fleer', '124'],
         32: ['Cal', 'Ripken JR', '1989', 'Fleer', '617'],
         33: ['Darryl', 'Strawberry', '1989', 'Fleer', '49'],
         34: ['Barry', 'Bonds', '1989', 'Fleer', '202'],
         35: ['Dwight', 'Gooden', '1989', 'Fleer', '36'],
         36: ['Orel', 'Hershiser', '1989', 'Fleer', '62'],
         37: ['Ken', 'Griffey JR', '1989', 'Fleer', '548'],
         38: ['Craig', 'Biggio', '1989', 'Fleer', '353'],
         39: ['Bill', 'Ripken ff', '1989', 'Fleer', '616'],
         40: ['Randy', 'Johnson green tint', '1989', 'Fleer', '381']
         }

for _ in cards:
    card_url = construct_url(_)
    card_info(card_url)
    random_sleep()

cards = {1: ['Rickey', 'Henderson', '1990', 'Topps', '450'],
         2: ['Bo', 'Jackson', '1990', 'Topps', '300'],
         3: ['Randy', 'Johnson', '1990', 'Topps', '431'],
         4: ['Larry', 'Walker', '1990', 'Topps', '757'],
         5: ['Nolan', 'Ryan', '1990', 'Topps', '1'],
         6: ['Nolan', 'Ryan', '1990', 'Topps', '3'],
         7: ['Nolan', 'Ryan', '1990', 'Topps', '4'],
         8: ['Nolan', 'Ryan', '1990', 'Topps', '5'],
         9: ['Frank', 'Thomas', '1990', 'Topps', '414'],
         10: ['Tom', 'Glavine', '1990', 'Topps', '506'],
         11: ['Joe', 'Magrane', '1990', 'Topps', '406'],
         12: ['Mark', 'McGwire', '1990', 'Topps', '690'],
         13: ['Ozzie', 'Smith', '1990', 'Topps', '400'],
         14: ['Curt', 'Schilling', '1990', 'Topps', '97'],
         15: ['Randy', 'Johnson', '1990', 'Topps', '431'],
         16: ['Fred', 'McGriff', '1990', 'Topps', '385'],
         17: ['Craig', 'Biggio', '1990', 'Topps', '157'],
         18: ['Tony', 'Gwynn', '1990', 'Topps', '730'],
         19: ['Craig', 'Biggio', '1990', 'Topps', '404'],
         20: ['Howard', 'Johnson', '1990', 'Topps', '399'],
         21: ['Wade', 'Boggs', '1990', 'Topps', '760'],
         22: ['Ryan', 'Sandberg', '1990', 'Topps', '210'],
         23: ['Carlton', 'Fisk', '1990', 'Topps', '420'],
         24: ['Robin', 'Yount', '1990', 'Topps', '389'],
         25: ['Ozzie', 'Smith', '1990', 'Topps', '590'],
         26: ['Ozzie', 'Smith', '1990', 'Topps', '400'],
         27: ['Orel', 'Hershiser', '1990', 'Topps', '780'],
         28: ['Barry', 'Bonds', '1990', 'Topps', '220'],
         29: ['Cal', 'Ripken', '1990', 'Topps', '388'],
         30: ['Juan', 'Gonzalez', '1990', 'Topps', '331'],
         31: ['Dave', 'Winfield', '1990', 'Topps', '380'],
         32: ['Fernando', 'Valenzuela', '1990', 'Topps', '340'],
         33: ['Eric', 'Davis', '1990', 'Topps', '402'],
         34: ['Will', 'Clark', '1990', 'Topps', '397'],
         35: ['Deion', 'Sanders', '1990', 'Topps', '61'],
         36: ['Rafael', 'Palmeiro', '1990', 'Topps', '755'],
         37: ['Kirby', 'Puckett', '1990', 'Topps', '391'],
         38: ['Ruben', 'Sierra', '1990', 'Topps', '390'],
         39: ['Don', 'Mattingly', '1990', 'Topps', '200'],
         40: ['George', 'Brett', '1990', 'Topps', '60']
         }

for _ in cards:
    card_url = construct_url(_)
    card_info(card_url)
    random_sleep()
