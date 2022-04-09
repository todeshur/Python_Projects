import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random



driver = webdriver.Chrome()
driver.get("http://www.natrading.com/contact/index")


#Randomize Names
first_name = ["James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda", "William", "Elizabeth", "David", "Barbara", "Richard", "Susan", "Joseph", "Jessica"]
last_name = ["Brown", "Smith", "Johnson", "Anderson", "Taylor", "Lee"]

#Random.choice picks a random name from the list
F_name = random.choice(first_name)
L_name = random.choice(last_name)

#This is for the Name Field
elem = driver.find_element_by_id("Name")
elem.clear()
elem.send_keys(f'{F_name} {L_name}')
elem.send_keys(Keys.TAB)

#Randomize Company Name
company_name = ["Pixel", "Razzi", "Officecog", "Campering", "Remedie", "Logic Space", "Copy Suppies", "Office World", "Spaceava", "Intrepid"]
company_suffix = ["inc", "corporation", "supplier", "trading", "studio", ""]

C_name = random.choice(company_name)
C_suffix = random.choice(company_suffix)

#This is for Company Name Field
elem = driver.find_element_by_id("CompanyName")
elem.clear()
elem.send_keys(f'{C_name} {C_suffix}')
elem.send_keys(Keys.TAB)

#Randomize Email
#Mail = ["monster", "bang", "target"]

#E_Mail = random.choice(Mail)

#This is for the Email Field
elem = driver.find_element_by_id("Email")
elem.clear()
elem.send_keys(f'{L_name}@{C_name}.com')
elem.send_keys(Keys.TAB)

#Randomize Phone number
N1 = random.randint(100, 999)
N2 = random.randint(100, 999)
N3 = random.randint(1000, 9999)

#This is for the Phone Number Field
elem = driver.find_element_by_id("PhoneNumber")
elem.clear()
elem.send_keys(f'{N1}-{N2}-{N3}')
elem.send_keys(Keys.TAB)

#Randomize Question/Comment 
Coms = ["some times i supper glue my thumbs to my nipples and pretend im a t rex", "You think it's funny to take screenshots of people's NFTS, huh? Property theft is a joke to you? l'll have you know that the blockchain doesn't lie. I own it. Even if you save it, it's my property. You are mad that you don't own the art that I own. Delete that screenshot.", "I have gotten the covid vaccine about 20 times now. 4 Pfizer, 12 moderna, 4 Johnson. Once I got my first vaccine, I started cravings for it. There is something so great knowing I am reducing the spread of the coronavirus with each of them. I am feeling so empowered. I think I may be addicted ngl. At least it won't kill me.", "If you shit in the sink at exactly 4:20 am and yell “amogus” 69 times,a shadowy figured called mom will come to beat you up and you will wake up in a place called the orphanage", "This does not change the fact that in Antarctica there are 21 million penguins and in Malta there are 502,653 inhabitants. So if the penguins decide to invade Malta, each Maltese will have to fight 42 penguins.", "Writing's not easy. That's why Grammarly can help. This sentence is grammatically correct, but it's wordy, and hard to read. It undermines the writer's message and the word choice is bland. Grammarly's cutting edge technology helps you craft compelling, understandable writing that makes an impact on your reader. Much better. Are you ready to give it a try? Installation is simple and free. Visit Grammarly.com today!", "YOOO IS THAT A SQUIDWARD REFERANCE??? JOE  JOE  BIDEN  HAHA  STINKY!", "NA TRADING IS SO FLY. BUT WHERE IS PRICE? ME NO BUY! "] 

Q1 = random.choice(Coms)


#This is for the Question/Comment Field
elem = driver.find_element_by_id("QuestionComment")
elem.clear()
elem.send_keys(f'{Q1}')
elem.send_keys(Keys.TAB)

#This is for Submition
elem = driver.find_element_by_name("btnSubmit")
elem.send_keys(Keys.RETURN)

print(driver.title)
print(driver.current_url)

time.sleep(5)


driver.quit()
