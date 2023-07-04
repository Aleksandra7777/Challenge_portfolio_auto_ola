from pages.base_page import BasePage


class Dashboard(BasePage):
    logo_xpath = "//*[contains(@class, 'MuiCardMedia-root jss8')]"
    activity_xpath = "//*[text()='Activity']"
    shortcuts_xpath = "//*[text()='Shortcuts']"
    add_player_xpath = "//*[text()='Add player']"
    sign_out_xpath = "//*[text()='Sign out']"
    players_xpath = "//*[text()='Players']"
    main_page_xpath = "//*[text()='Main page']"
    players_count_xpath = "//*[text()='Players count']"
    dev_team_contact_xpath = "//*[text()='Dev team contact']"
    scotus_panel_xpath = "//*[contains(@class, 'MuiTypography-root jss144')]"
    pass