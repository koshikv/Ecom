from selenium.webdriver.common.by import By


class Login:
    Email_inputbox_id = "Email"
    Password_inputbox_id = "Password"
    Login_button_Xpath = "//button[@type='submit']"
    Logout_link_linltext = "Logout"

    # initiating driver using constructor
    def __init__(self, driver):
        self.driver = driver

    #     creating action names
    def SetUsername(self, username):
        self.driver.find_element(By.ID, self.Email_inputbox_id).clear()
        self.driver.find_element(By.ID, self.Email_inputbox_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.Password_inputbox_id).clear()
        self.driver.find_element(By.ID, self.Password_inputbox_id).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.Login_button_Xpath).click()

    def ClickLogout(self):
        self.driver.find_element(By.LINK_TEXT, self.Logout_link_linltext).click()
