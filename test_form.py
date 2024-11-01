import os

from selene import browser, be, have, command


def test_fill_form():
    browser.open('/')

    browser.element('#firstName').should(be.blank).type('Pavel')
    browser.element('#lastName').should(be.blank).type('Sukhar')
    browser.element('#userEmail').should(be.blank).type('sukhar@mail.com')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('9876543210')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select > option[value="1988"]').click()
    browser.element('.react-datepicker__month-select > option[value="3"]').click()
    browser.element('.react-datepicker__day--005:not(.react-datepicker__day--outside-month)').click()

    "Проскролить страницу до элемента"
    browser.element('#subjectsInput').perform(command.js.scroll_into_view)

    browser.element('#subjectsInput').type('Maths')
    browser.element('#subjectsContainer div[id^="react-select"]').click()
    browser.element('#subjectsInput').type('Computer Science')
    browser.element('#subjectsContainer div[id^="react-select"]').click()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('label[for="hobbies-checkbox-2"]').click()
    browser.element('label[for="hobbies-checkbox-3"]').click()
    browser.element('#currentAddress').type('Bawana Rd, Shahabad Daulatpur, Shahabad Daulatpur Village, Rohini')
    browser.element("#uploadPicture").send_keys(os.path.abspath("pic.png"))
    browser.element('#state').click()
    browser.all('#state div[id^="react-select-"]').element_by(have.text('Rajasthan')).click()
    browser.element('#city').click()
    browser.all('#city div[id^="react-select-"]').element_by(have.text('Jaipur')).click()
    browser.element('#submit').click()

    browser.element('//td[preceding-sibling::td="Student Name"]').should(have.exact_text("Pavel Sukhar"))
    browser.element('//td[preceding-sibling::td="Student Email"]').should(have.exact_text("sukhar@mail.com"))
    browser.element('//td[preceding-sibling::td="Gender"]').should(have.exact_text("Male"))
    browser.element('//td[preceding-sibling::td="Mobile"]').should(have.exact_text("9876543210"))
    browser.element('//td[preceding-sibling::td="Date of Birth"]').should(have.exact_text("05 April,1988"))
    browser.element('//td[preceding-sibling::td="Subjects"]').should(have.exact_text("Maths, Computer Science"))
    browser.element('//td[preceding-sibling::td="Hobbies"]').should(have.exact_text("Sports, Reading, Music"))
    browser.element('//td[preceding-sibling::td="Picture"]').should(have.exact_text("pic.png"))
    browser.element('//td[preceding-sibling::td="Address"]') \
        .should(have.exact_text("Bawana Rd, Shahabad Daulatpur, Shahabad Daulatpur Village, Rohini"))
    browser.element('//td[preceding-sibling::td="State and City"]').should(have.exact_text("Rajasthan Jaipur"))