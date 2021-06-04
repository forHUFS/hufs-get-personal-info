from config                   import URL
from worker.sql               import update_user_type
from worker.driver            import WebDriver


def check_user_graduated(user_pk, user_id, password):
    driver = WebDriver()
    driver.get(URL)

    user_id_element  = driver.find_element_by_xpath(
        "/html/body/div[1]/form[3]/div[2]/div/div[2]/div/input[1]"
    )
    user_id_element.send_keys(user_id)

    password_element = driver.find_element_by_xpath('//*[@id="password"]')
    password_element.send_keys(password)

    login_btn = driver.find_element_by_xpath(
        "/html/body/div[1]/form[3]/div[2]/div/div[2]/div/a"
    )
    login_btn.click()

    left = driver.find_element_by_name("left")
    driver.switch_to.frame(left)

    menu_frame = driver.find_element_by_name("MenuFrame")
    driver.switch_to.frame(menu_frame)

    personal_info_menu = driver.find_element_by_xpath("/html/body/div/a[1]")
    personal_info_menu.click()

    get_personal_info_btn = driver.find_element_by_xpath(
        '//*[@id="div1"]/a[1]'
    )
    get_personal_info_btn.click()

    driver.switch_to.default_content()

    body = driver.find_element_by_name("body")
    driver.switch_to.frame(body)

    graduate_btn = driver.find_element_by_xpath('//*[@id="ui-id-3"]').text

    if graduate_btn == '졸업':
        update_user_type(user_pk=user_pk)
        return True

    elif graduate_btn == '성적/전공':
        return False
    
    else:
        raise Exception