from pages.base_page import BasePage


class AddAMatchForm(BasePage):
    add_match_xpath = "//*[text()='Add match']"
    my_team_xpath = "// *[text() = 'My team']"
    my_team_score_xpath = "// *[text() = 'My team score']"
    enemy_team_score_xpath = "// *[text() = 'Enemy team score']"
    enemy_team_xpath = "// *[text() = 'Enemy team']"
    date_team_xpath = "// *[text() = 'Date']"
    time_played_xpath = "// *[text() = 'Time played']"
    rating_xpath = "// *[text() = 'Rating']"
    author_xpath = "// *[text() = 'Author']"
    actions_xpath = "// *[text() = 'Actions']"
    pass