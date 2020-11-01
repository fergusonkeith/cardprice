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
               'rare+-name+-autograph+-project+&bt=sold&sort=PricePlusShippingHighest&cat=213'
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
         40: ['Randy', 'Johnson green tint', '1989', 'Fleer', '381'],
         41: ['Barry', 'Bonds', '1989', 'Fleer', '202'],
         42: ['Nolan', 'Ryan', '1989', 'Fleer', '368'],
         43: ['Bobby', 'Bonilla', '1989', 'Fleer', '203'],
         44: ['Gary', 'Sheffield', '1989', 'Fleer', '196'],
         45: ['Dual', 'Heat', '1989', 'Fleer', '635'],
         46: ['Cannon', 'Arms', '1989', 'Fleer', '637'],
         47: ['Fred', 'McGriff', '1989', 'Fleer', '240'],
         48: ['Dennis', 'Eckersley', '1989', 'Fleer', '7'],
         49: ['Dale', 'Murphy', '1989', 'Fleer', '596'],
         50: ['Ruben', 'Sierra', '1989', 'Fleer', '532'],
         51: ['Orel', 'Hershiser', '1989', 'Fleer', '7'],
         52: ['Will', 'Clark', '1989', 'Fleer', '3'],
         53: ['Bobby', 'Bonilla', '1989', 'Fleer', '1'],
         54: ['Jose', 'Canseco', '1989', 'Fleer', '2'],
         55: ['Darryl', 'Strawberry', '1989', 'Fleer', '10'],
         56: ['Randy', 'Johnson blacked', '1989', 'Fleer', '381']
         }

#for _ in cards:
#    card_url = construct_url(_)
#    card_info(card_url)
#    random_sleep()

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
         22: ['Carlton', 'Fisk', '1990', 'Topps', '420'],
         23: ['Robin', 'Yount', '1990', 'Topps', '389'],
         24: ['Ozzie', 'Smith', '1990', 'Topps', '590'],
         25: ['Ozzie', 'Smith', '1990', 'Topps', '400'],
         26: ['Orel', 'Hershiser', '1990', 'Topps', '780'],
         27: ['Barry', 'Bonds', '1990', 'Topps', '220'],
         28: ['Cal', 'Ripken', '1990', 'Topps', '388'],
         29: ['Juan', 'Gonzalez', '1990', 'Topps', '331'],
         30: ['Dave', 'Winfield', '1990', 'Topps', '380'],
         31: ['Fernando', 'Valenzuela', '1990', 'Topps', '340'],
         32: ['Eric', 'Davis', '1990', 'Topps', '402'],
         33: ['Will', 'Clark', '1990', 'Topps', '397'],
         34: ['Deion', 'Sanders', '1990', 'Topps', '61'],
         35: ['Rafael', 'Palmeiro', '1990', 'Topps', '755'],
         36: ['Kirby', 'Puckett', '1990', 'Topps', '391'],
         37: ['Ruben', 'Sierra', '1990', 'Topps', '390'],
         38: ['Don', 'Mattingly', '1990', 'Topps', '200'],
         39: ['Nolan', 'Ryan', '1990', 'Topps', '2'],
         40: ['George', 'Brett', '1990', 'Topps', '60'],
         41: ['Jose', 'Canseco', '1990', 'Topps', '250'],
         42: ['Eric', 'Davuc', '1990', 'Topps', '260'],
         43: ['Kirby', 'Puckett', '1990', 'Topps', '700'],
         44: ['Gary', 'Sheffield', '1990', 'Topps', '718'],
         45: ['Record', 'Breaker', '1990', 'Topps', '7'],
         46: ['Sammy', 'Sosa', '1990', 'Topps', '692'],
         47: ['Robin', 'Yount', '1990', 'Topps', '290'],
         48: ['Darryl', 'Strawberry', '1990', 'Topps', '600'],
         49: ['Will', 'Clark', '1990', 'Topps', '100'],
         50: ['Larry', 'Walker', '1990', 'Topps', '757'],
         51: ['Record', 'Breaker', '1990', 'Topps', '8'],
         52: ['Ken', 'Griffey', '1990', 'Topps', '581'],
         53: ['Carlos', 'Martinez', '1990', 'Topps', '461'],
         54: ['Greg', 'Vaughn', '1990', 'Topps', '57'],
         }

#for _ in cards:
#    card_url = construct_url(_)
#    card_info(card_url)
#    random_sleep()

cards = {1: ['Tom', 'Herr', '1989', 'Topps Traded', '49T'],
         2: ['Jimmy', 'Jones', '1989', 'Topps Traded', '58T'],
         3: ['Chuck', 'Cary', '1989', 'Topps Traded', '17T'],
         4: ['Dwight', 'Smith', '1989', 'Topps Traded', '113T'],
         5: ['Gregg', 'Olson', '1989', 'Topps Traded', '89T'],
         6: ['Ken', 'Griffey', '1989', 'Topps Traded', '40T'],
         7: ['Deion', 'Sanders', '1989', 'Topps Traded', '110T'],
         9: ['Andy', 'Hawkins', '1989', 'Topps Traded', '47T'],
         10: ['Lance', 'McCullers', '1989', 'Topps Traded', '77T'],
         12: ['Jesse', 'Barfield', '1989', 'Topps Traded', '7T'],
         13: ['Todd', 'Benzinger', '1989', 'Topps Traded', '9T'],
         14: ['John', 'Kruk', '1989', 'Topps Traded', '63T'],
         15: ['Len', 'Dykstra', '1989', 'Topps Traded', '27T'],
         16: ['Rick', 'Mahler', '1989', 'Topps Traded', '74T'],
         17: ['Steve', 'Sax', '1989', 'Topps Traded', '111T'],
         18: ['Kenny', 'Rogers', '1989', 'Topps Traded', '104T'],
         19: ['Ken', 'Hill', '1989', 'Topps Traded', '50T'],
         20: ['Juan', 'Samuel', '1989', 'Topps Traded', '108T'],
         21: ['Milt', 'Thompson', '1989', 'Topps Traded', '118T'],
         24: ['Dave', 'Lapoint', '1989', 'Topps Traded', '67T'],
         25: ['Jamie', 'Moyer', '1989', 'Topps Traded', '85T'],
         26: ['Steve', 'Balboni', '1989', 'Topps Traded', '6T'],
         27: ['Terry', 'Francona', '1989', 'Topps Traded', '35T'],
         28: ['Mike', 'Devereaux', '1989', 'Topps Traded', '23T'],
         32: ['Eddie', 'Murray', '1989', 'Topps Traded', '87T'],
         34: ['Shane', 'Rawley', '1989', 'Topps Traded', '101T'],
         35: ['Bert', 'Blyleven', '1989', 'Topps Traded', '11T'],
         36: ['Wally', 'Backman', '1989', 'Topps Traded', '5T'],
         38: ['Kent', 'Tekulve', '1989', 'Topps Traded', '116T'],
         39: ['Omar', 'Vizquel', '1989', 'Topps Traded', '122T'],
         40: ['Jerome', 'Walton', '1989', 'Topps Traded', '123T'],
         41: ['Willie', 'Randolph', '1989', 'Topps Traded', '100T'],
         42: ['Ken', 'Griffey JR', '1989', 'Topps Traded', '41T'],
         43: ['Nolan', 'Ryan', '1989', 'Topps Traded', '106T'],
         44: ['Randy', 'Johnson', '1989', 'Topps Traded', '57T'],
         45: ['Rickey', 'Henderson', '1989', 'Topps Traded', '48T']
         }

#for _ in cards:
#    card_url = construct_url(_)
#    card_info(card_url)
#    random_sleep()

cards = {1: ['Will', 'Clark', '1986', 'Topps Traded', '24T'],
         2: ['Kevin', 'Mitchell', '1986', 'Topps Traded', '74T'],
         3: ['Randy', 'Niemann', '1986', 'Topps Traded', '78T'],
         4: ['Mike', 'Easler', '1986', 'Topps Traded', '33T'],
         6: ['Don', 'Baylor', '1986', 'Topps Traded', '6T'],
         7: ['Hal', 'Lanier', '1986', 'Topps Traded', '60T'],
         8: ['Tim', 'Conroy', '1986', 'Topps Traded', '28T'],
         9: ['Bob', 'Tewksbury', '1986', 'Topps Traded', '110T'],
         10: ['Claudell', 'Washington', '1986', 'Topps Traded', '122T'],
         11: ['Tim', 'Teufel', '1986', 'Topps Traded', '109T'],
         12: ['Bob', 'Walk', '1986', 'Topps Traded', '120T'],
         13: ['Phil', 'Niekro', '1986', 'Topps Traded', '77T'],
         14: ['Paul', 'Zuvella', '1986', 'Topps Traded', '131T'],
         15: ['Mike', 'Heath', '1986', 'Topps Traded', '46T'],
         16: ['Dick', 'Williams', '1986', 'Topps Traded', '124T'],
         17: ['Ken', 'Griffey', '1986', 'Topps Traded', '41T'],
         18: ['Ted', 'Simmons', '1986', 'Topps Traded', '102T'],
         19: ['Bobby', 'Bonilla', '1986', 'Topps Traded', '12T'],
         20: ['Jim', 'Leyland', '1986', 'Topps Traded', '66T'],
         21: ['Kurt', 'Stillwell', '1986', 'Topps Traded', '104T'],
         22: ['Gary', 'Roenicke', '1986', 'Topps Traded', '94T'],
         23: ['Dale', 'Sveum', '1986', 'Topps Traded', '106T'],
         24: ['Tom', 'Hume', '1986', 'Topps Traded', '47T'],
         25: ['Bob', 'Ojeda', '1986', 'Topps Traded', '81T'],
         26: ['Robby', 'Thompson', '1986', 'Topps Traded', '113T'],
         27: ['John', 'Kruk', '1986', 'Topps Traded', '56T'],
         28: ['Lou', 'Piniella', '1986', 'Topps Traded', '86T'],
         29: ['Todd', 'Worrell', '1986', 'Topps Traded', '127T'],
         31: ['Andres', 'Galarraga', '1986', 'Topps Traded', '40T'],
         32: ['Bo', 'Jackson', '1986', 'Topps Traded', '50T'],
         33: ['Wally', 'Joyner', '1986', 'Topps Traded', '51T'],
         34: ['Barry', 'Bonds', '1986', 'Topps Traded', '11T'],
         35: ['Jose', 'Canseco', '1986', 'Topps Traded', '20T'],
         }

#for _ in cards:
#    card_url = construct_url(_)
#    card_info(card_url)
#    random_sleep()

cards = {1: ['Nolan', 'Ryan', '1991', 'Topps Stadium Club', '200'],
         2: ['Craig', 'Biggio', '1991', 'Topps Stadium Club', '176'],
         3: ['Bo', 'Jackson', '1991', 'Topps Stadium Club', '224'],
         4: ['Juan', 'Gonzalez', '1991', 'Topps Stadium Club', '237'],
         5: ['Barry', 'Bonds', '1991', 'Topps Stadium Club', '220'],
         6: ['Rickey', 'Henderson', '1991', 'Topps Stadium Club', '120'],
         7: ['Sammy', 'Sosa', '1991', 'Topps Stadium Club', '6'],
         8: ['George', 'Brett', '1991', 'Topps Stadium Club', '159'],
         9: ['Dave', 'Justice', '1991', 'Topps Stadium Club', '26'],
         10: ['Frank', 'Thomas', '1991', 'Topps Stadium Club', '57'],
         11: ['Ken', 'Griffey JR', '1991', 'Topps Stadium Club', '270'],
         12: ['Wade', 'Boggs', '1991', 'Topps Stadium Club', '170'],
         13: ['Don', 'Mattingly', '1991', 'Topps Stadium Club', '21'],
         14: ['Eddie', 'Murray', '1991', 'Topps Stadium Club', '177'],
         15: ['Dale', 'Murphy', '1991', 'Topps Stadium Club', '243'],
         16: ['Ozzie', 'Smith', '1991', 'Topps Stadium Club', '154'],
         17: ['Greg', 'Maddux', '1991', 'Topps Stadium Club', '126'],
         18: ['Wade', 'Boggs', '1991', 'Topps Stadium Club', '170'],
         19: ['Cecil', 'Fielder', '1991', 'Topps Stadium Club', '186'],
         20: ['Wally', 'Joyner', '1991', 'Topps Stadium Club', '2'],
         21: ['Kirby', 'Puckett', '1991', 'Topps Stadium Club', '110'],
         23: ['Orel', 'Hershiser', '1991', 'Topps Stadium Club', '244'],
         24: ['Gary', 'Sheffield', '1991', 'Topps Stadium Club', '95'],
         25: ['Junior', 'Ortiz', '1991', 'Topps Stadium Club', '13'],
         26: ['Jose', 'Canseco', '1991', 'Topps Stadium Club', '155'],
         27: ['Dave', 'Winfield', '1991', 'Topps Stadium Club', '263']
         }

#for _ in cards:
#    card_url = construct_url(_)
#    card_info(card_url)
#    random_sleep()


cards = {1: ['Barry', 'Bonds foil', '1992', 'Bowman', '590'],
         2: ['Kirby', 'Puckett', '1992', 'Bowman', '80'],
         3: ['David', 'Justice', '1992', 'Bowman', '312'],
         4: ['Dave', 'Stewart', '1992', 'Bowman', '280'],
         5: ['Juan', 'Gonzalez', '1992', 'Bowman', '84'],
         6: ['Tom', 'Glavine', '1992', 'Bowman', '699'],
         7: ['Eddie', 'Murray', '1992', 'Bowman', '433']
         }

#for _ in cards:
#    card_url = construct_url(_)
#    card_info(card_url)
#    random_sleep()

cards = {1: ['Tony', 'Gwynn', '1993', 'Leaf', '2'],
         2: ['Cal', 'Ripken Jr', '1993', 'Leaf', '5'],
         3: ['Eddie', 'Murray', '1993', 'Leaf', '4'],
         4: ['Ryan', 'Sandberg', '1993', 'Leaf', '8'],
         5: ['Tim', 'Salmon', '1993', 'Leaf', '10'],
         6: ['Nolan', 'Ryan', '1993', 'Leaf', '1'],
         7: ['Robin', 'Yount', '1993', 'Leaf', '3'],
         8: ['Frank', 'Thomas', '1993', 'Leaf', '10'],
         9: ['Nolan', 'Ryan', '1993', 'Leaf', '115'],
         10: ['Don', 'Mattingly', '1993', 'Leaf', '2'],
         11: ['Tony', 'Gwynn', '1993', 'Leaf', '28'],
         12: ['Jose', ' Canseco', '1993', 'Leaf', '9'],
         13: ['Travis', 'Fryman', '1993', 'Leaf', '16'],
         14: ['Ivan', 'Rodriguez', '1993', 'Leaf', '5'],
         15: ['Jeff', 'Bagwell', '1993', 'Leaf', '125'],
         16: ['Eddie', 'Murray', '1993', 'Leaf', '167'],
         17: ['Ken', 'Griffey Jr', '1993', 'Leaf', '319'],
         18: ['Frank', 'Thomas', '1993', 'Leaf', '195'],
         19: ['Ken', 'Griffey Jr', '1993', 'Leaf', '7'],
         20: ['Frank', 'Thomas', '1993', 'Leaf', '2'],
         21: ['Mike', 'Piazza', '1993', 'Leaf', '35'],
         22: ['Frank', 'Thomas', '1993', 'Leaf', '1'],
         23: ['Robin', 'Yount', '1993', 'Leaf', '188'],
         24: ['David', 'Justice', '1993', 'Leaf', '50'],
         25: ['Steve', 'Avery', '1993', 'Leaf', '121']
         }

for _ in cards:
    card_url = construct_url(_)
    card_info(card_url)
    random_sleep()

cards = {1: ['Ken', 'Griffey Jr PSA', '1991', 'Donruss', '49'],
         2: ['Ken', 'Griffey Jr PSA', '1991', 'Donruss', '77'],
         3: ['Frank', 'Thomas', '1991', 'Donruss', '477'],
         4: ['Nolan', 'Ryan', '1991', 'Donruss', '89']
         }


for _ in cards:
    card_url = construct_url(_)
    card_info(card_url)
#    random_sleep()