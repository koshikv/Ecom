from selenium.webdriver.common.by import By


class searchCustomer:
    Email_inputbox_name = "SearchEmail"
    First_Name_inputbox_id = "SearchFirstName"
    Last_Name_inputbox_id = "SearchLastName"
    Button_Search_id = "/search-customers"
    table_xpath = '// table[ @ id = "customers-grid"]'
    table_Rows_xpath = '// table[ @ id = "customers-grid"]// tr'
    table_Column_xpath = '// table[ @ id = "customers-grid"]/tr/ td'

    # initiating driver using constructor
    def __init__(self, driver):
        self.driver = driver

    #     creating action names
    def set_Email_inputbox(self, email):
        self.driver.find_element(By.NAME, self.Email_inputbox_name).clear()
        self.driver.find_element(By.NAME, self.Email_inputbox_name).send_keys(email)

    def set_First_Name_inputbox(self, fname):
        self.driver.find_element(By.ID, self.First_Name_inputbox_id).clear()
        self.driver.find_element(By.ID, self.First_Name_inputbox_id).send_keys(fname)

    def set_Last_Name_inputbox(self, lname):
        self.driver.find_element(By.ID, self.Last_Name_inputbox_id).clear()
        self.driver.find_element(By.ID, self.Last_Name_inputbox_id).send_keys(lname)

    def click_Button_Search(self):
        self.driver.find_element(By.ID, self.First_Name_inputbox_id).click()

    def get_rows_no(self):
        return len(self.driver.find_element(By.XPATH, self.table_Rows_xpath))

    def get_NoOfCloumn(self):
        return len(self.driver.find_element(By.XPATH, self.table_Column_xpath))

    def searchCustByEmail(self, email):
        flag = False
        for r in range(1, self.get_rows_no() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, '// table[@ id = "customers-grid"]/tr["+str(r)+"]/ td[2]')
            if emailid == email:
                flag = True
                break
        return flag
