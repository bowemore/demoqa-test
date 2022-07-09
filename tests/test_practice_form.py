from selene import have, command
from selene.support.shared import browser
import calendar

firstName = 'Mike'
lastName = 'Tyson'
userEmail = 'mike@tyson.com'
gender = 'Male'
userNumber = '9876543210'
dayOfBirth = "30th"
mothOfBirth = "6"
mothOfBirthName = calendar.month_name[int(mothOfBirth)]
yearOfBirth = '1966'
subject = 'English'
hobbies = 'Sports'
currentAddress = "10250 Constellation Blvd., 9th Floor, Los Angeles"
uploadPicture = r'C:\Users\WALLE\PycharmProjects\lesson5_selene\test\1.png'
state = 'NCR'
city = 'Delhi'


def test_submit_form():
    browser.open('/automation-practice-form')

    browser.element('#firstName').type(firstName)
    browser.element('#lastName').type(lastName)
    browser.element('#userEmail').type(userEmail)
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type(userNumber)
    browser.element('#dateOfBirthInput').click()
    browser.element(f'[value="{yearOfBirth}"]').click()
    browser.element(f'[value="{mothOfBirth}"]').click()
    browser.element(f'div[aria-label="Choose Thursday, {mothOfBirthName} {dayOfBirth}, {yearOfBirth}"]').click()
    browser.element('#subjectsInput').type(subject).press_enter()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('#uploadPicture').type(uploadPicture)
    browser.element('#currentAddress').type(currentAddress).press_tab()
    browser.element('#state input').type(state).press_tab()
    browser.element('#city input').type(city).press_enter()
    browser.element('#submit').perform(command.js.scroll_into_view).click()

    browser.all('table tr').should(have.exact_texts(
        'Label Values',
        f'Student Name {firstName} {lastName}',
        f'Student Email {userEmail}',
        f'Gender {gender}',
        f'Mobile {userNumber}',
        f'Date of Birth {dayOfBirth[:-2]} {mothOfBirthName},{yearOfBirth}',
        f'Subjects {subject}',
        f'Hobbies {hobbies}',
        f'Picture {uploadPicture[-5:]}',
        f'Address {currentAddress}',
        f'State and City {state} {city}'
    ))




















