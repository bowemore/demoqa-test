from selene import have, be, command
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def test_submit_form():
    browser.open('/text-box')
    browser.should(have.title('ToolsQA'))
    s('.main-header').should(have.exact_text('Text Box'))

    s('//*[@id="userName"]').type('Mike')
    s('#userEmail').type('m@m.ru')
    s('#currentAddress').type('moscow')
    s('#permanentAddress').type('tver')
    s('#submit').perform(command.js.click)

    # asserts
    ss('//*[@id = "output"]//p').should(have.exact_texts(
        'Name:Mike',
        'Email:m@m.ru',
        'Current Address :moscow',
        'Permananet Address :tver'
    ))
