from selene import browser, be, have

from student_registration_form import resources


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)

    def fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)

    def select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def fill_mobile(self, value):
        browser.element('#userNumber').should(be.blank).type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(f'.react-datepicker__year-select > option[value="{year}"]').click()
        browser.element(f'.react-datepicker__month-select > option[value="{month}"]').click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').type(value)
        browser.element('#subjectsContainer div[id^="react-select"]').click()

    def select_hobbies(self, value):
        browser.all('[id^=hobbies-checkbox-]+label').element_by(have.exact_text(value)).click()

    def fill_current_address(self, value):
        browser.element('#currentAddress').type(value)

    def upload_picture(self, value):
        browser.element("#uploadPicture").send_keys(resources.path(value))

    def select_state(self, value):
        browser.element('#state').click()
        browser.all('#state div[id^="react-select-"]').element_by(have.text(value)).click()

    def select_city(self, value):
        browser.element('#city').click()
        browser.all('#city div[id^="react-select-"]').element_by(have.text(value)).click()

    def submit(self):
        browser.element('#submit').click()

    def should_have_register_user_with(self, full_name, email, gender, mobile, date_of_birth, subjects, hobbies,
                                       picture, current_address, state_and_city):
        browser.element('//td[preceding-sibling::td="Student Name"]').should(have.exact_text(full_name))
        browser.element('//td[preceding-sibling::td="Student Email"]').should(have.exact_text(email))
        browser.element('//td[preceding-sibling::td="Gender"]').should(have.exact_text(gender))
        browser.element('//td[preceding-sibling::td="Mobile"]').should(have.exact_text(mobile))
        browser.element('//td[preceding-sibling::td="Date of Birth"]').should(have.exact_text(date_of_birth))
        browser.element('//td[preceding-sibling::td="Subjects"]').should(have.exact_text(subjects))
        browser.element('//td[preceding-sibling::td="Hobbies"]').should(have.exact_text(hobbies))
        browser.element('//td[preceding-sibling::td="Picture"]').should(have.exact_text(picture))
        browser.element('//td[preceding-sibling::td="Address"]').should(have.exact_text(current_address))
        browser.element('//td[preceding-sibling::td="State and City"]').should(have.exact_text(state_and_city))
