import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class addCutomers:
    mainLink_Cutomers_xpth = "//a[@href='#']//p[contains(text(),'Customers')]"
    subLink_Customers_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    link_AddNew_xpath = "//a[@class='btn btn-primary']"
    inputbox_Email_id = "Email"
    inputbox_Password_id = "Password"
    inputbox_FirstName_id = "FirstName"
    inputbox_LastName_id = "LastName"
    radioButton_Gender_Male_xpath = "//label[normalize-space()='Male']"
    radioButton_Gender_Female_xpath = "//label[normalize-space()='Female']"
    DOB_box_id = "DateOfBirth"
    inputbox_Company_name_id = "Company"
    checkbox_is_tax_exempt_id = "IsTaxExempt"
    link_NewsLetter_xpath = "//div[@class='input-group-append']//input[@role='listbox']"
    link_NewsLetter_your_store_name_xpath = "//div[@class='input-group-append']//div[@role='listbox']"
    link_NewsLetter_Test_store_2_xpath = "// li[normalize - space() = 'Test store 2']"
    link_Customer_roles_xpath = "// div[ @class ='k-multiselect-wrap k-floatwrap']"
    link_Customer_roles_Administrators_xpath = "// li[contains(text(), 'Administrators')]"
    link_Customer_roles_Forum_Moderators_xpath = "// li[contains(text(), 'Forum Moderators')]"
    link_Customer_roles_Guests_xpath = "// li[contains(text(), 'Guests')]"
    link_Customer_roles_Registered_xpath = "// li[contains(text(), 'Registered')]"
    link_Customer_roles_Vendors_xpath = "// li[contains(text(), 'Vendors')]"
    dropdown_Managerofvendor = "//select[@id='VendorId']"
    inputbox_AdminComment_id = "//textarea[@id='AdminComment']"
    button_save_name = "save"

    def __init__(self, driver):
        self.driver = driver

    def clickOn_mainLink_Cutomers(self):
        self.driver.find_element(By.XPATH, self.mainLink_Cutomers_xpth).click()

    def clickOn_subLink_Customers(self):
        self.driver.find_element(By.XPATH, self.subLink_Customers_xpath).click()

    def clickOn_link_AddNew(self):
        self.driver.find_element(By.XPATH, self.link_AddNew_xpath).click()

    def set_Email(self, email):
        self.driver.find_element(By.ID, self.inputbox_Email_id).clear()
        self.driver.find_element(By.ID, self.inputbox_Email_id).send_keys(email)

    def set_Password(self, password):
        self.driver.find_element(By.ID, self.inputbox_Password_id).clear()
        self.driver.find_element(By.ID, self.inputbox_Password_id).send_keys(password)

    def set_inputbox_FirstName(self, firstname):
        self.driver.find_element(By.ID, self.inputbox_FirstName_id).clear()
        self.driver.find_element(By.ID, self.inputbox_FirstName_id).send_keys(firstname)

    def set_inputbox_LastName(self, lastname):
        self.driver.find_element(By.ID, self.inputbox_LastName_id).clear()
        self.driver.find_element(By.ID, self.inputbox_LastName_id).send_keys(lastname)

    def set_radioButton_Gender(self, Gender):
        if Gender == "Male":
            self.driver.find_element(By.XPATH, self.radioButton_Gender_Male_xpath).click()

        elif Gender == "Female":
            self.driver.find_element(By.XPATH, self.radioButton_Gender_Female_xpath).click()

        else:
            self.driver.find_element(By.XPATH, self.radioButton_Gender_Male_xpath).click()

    def set_DOB_box(self, dob):
        self.driver.find_element(By.ID, self.DOB_box_id).clear()
        self.driver.find_element(By.ID, self.DOB_box_id).send_keys(dob)

    def set_inputbox_Company_name(self, cname):
        self.driver.find_element(By.ID, self.inputbox_Company_name_id).clear()
        self.driver.find_element(By.ID, self.inputbox_Company_name_id).send_keys(cname)

    def set_checkbox_is_tax_exempt(self, decision):
        if decision == "yes":
            self.driver.find_element(By.ID, self.checkbox_is_tax_exempt_id).click()

        elif decision == "no":
            self.driver.find_element(By.ID, self.checkbox_is_tax_exempt_id).clear()

        else:
            self.driver.find_element(By.ID, self.checkbox_is_tax_exempt_id).click()

    def set_link_NewsLetter(self, letter):
        self.driver.find_element(By.XPATH, self.link_NewsLetter_xpath).click()

        if letter == "your store name":
            self.driver.find_element(By.XPATH, self.link_NewsLetter_your_store_name_xpath).click()

        elif letter == "test store 2":
            self.driver.find_element(By.XPATH, self.link_NewsLetter_Test_store_2_xpath).click()

        else:
            self.driver.find_element(By.XPATH, self.link_NewsLetter_your_store_name_xpath).click()

    def set_link_Customer_roles(self, role):
        self.driver.find_element(By.XPATH, self.link_Customer_roles_xpath).click()
        time.sleep(3)

        if role == "Administrators":
            self.driver.find_element(By.XPATH, self.link_Customer_roles_Administrators_xpath).click()

        elif role == "Forum Moderators":
            self.driver.find_element(By.XPATH, self.link_Customer_roles_Forum_Moderators_xpath).click()

        elif role == "Guests":
            self.driver.find_element(By.XPATH, self.link_Customer_roles_Guests_xpath).click()

        elif role == "Registered":
            self.driver.find_element(By.XPATH, "span[title = 'delete']").click()
            self.driver.find_element(By.XPATH, self.link_Customer_roles_Registered_xpath).click()

        elif role == "Guests":
            self.driver.find_element(By.XPATH, self.link_Customer_roles_Guests_xpath).click()

        elif role == "Vendors":
            self.driver.find_element(By.XPATH, self.link_Customer_roles_Vendors_xpath).click()

        else:
            self.driver.find_element(By.XPATH, self.link_Customer_roles_Guests_xpath).click()

    def set_Managerofvendor(self, value):
        drp = Select(self.driver.find_element(By.XPATH, self.dropdown_Managerofvendor))
        drp.select_by_value(value)

    def set_inputbox_AdminComment(self, comment):
        self.driver.find_element(By.ID, self.inputbox_AdminComment_id).clear()
        self.driver.find_element(By.ID, self.inputbox_AdminComment_id).send_keys(comment)

    def set_button_save(self):
        self.driver.find_element(By.NAME, self.button_save_name)
