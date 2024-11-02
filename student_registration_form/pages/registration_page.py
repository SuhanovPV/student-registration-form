from selene import browser, be, have

from student_registration_form import resources
from student_registration_form.data import users


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def register(self, user: users.User):
        self._fill_first_name(user.first_name) \
            ._fill_last_name(user.last_name) \
            ._fill_email(user.email) \
            ._select_gender(user.gender) \
            ._fill_mobile(user.mobile) \
            ._fill_date_of_birth(**user.date_of_birth) \
            ._fill_subjects(user.subjects) \
            ._select_hobbies(user.hobbies) \
            ._upload_picture(user.picture) \
            ._fill_current_address(user.current_address) \
            ._select_state(user.state) \
            ._select_city(user.city) \
            ._submit()

    def should_have_registered(self, user:users.User):
        self._should_have_register_user_with(
            ('Student Name', f'{user.first_name} {user.last_name}'),
            ('Student Email', user.email),
            ('Gender', user.gender),
            ('Mobile', user.mobile),
            ('Date of Birth', f'{user.date_of_birth["day"]} {user.date_of_birth["month"]},{user.date_of_birth["year"]}'),
            ('Subjects', ', '.join(user.subjects)),
            ('Hobbies', ', '.join(user.hobbies)),
            ('Picture', user.picture),
            ('Address', user.current_address),
            ('State and City', f'{user.state} {user.city}')
        )

    def _fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def _fill_last_name(self, value):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def _fill_email(self, value):
        browser.element('#userEmail').should(be.blank).type(value)
        return self

    def _select_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()
        return self

    def _fill_mobile(self, value):
        browser.element('#userNumber').should(be.blank).type(value)
        return self

    def _fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(f'.react-datepicker__year-select > option[value="{year}"]').click()
        browser.element(f'.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def _fill_subjects(self, values):
        for value in values:
            browser.element('#subjectsInput').type(value)
            browser.element('#subjectsContainer div[id^="react-select"]').click()
        return self

    def _select_hobbies(self, values):
        for value in values:
            browser.all('[id^=hobbies-checkbox-]+label').element_by(have.exact_text(value)).click()
        return self

    def _fill_current_address(self, value):
        browser.element('#currentAddress').type(value)
        return self

    def _upload_picture(self, value):
        browser.element("#uploadPicture").send_keys(resources.path(value))
        return self

    def _select_state(self, value):
        browser.element('#state').click()
        browser.all('#state div[id^="react-select-"]').element_by(have.text(value)).click()
        return self

    def _select_city(self, value):
        browser.element('#city').click()
        browser.all('#city div[id^="react-select-"]').element_by(have.text(value)).click()
        return self

    def _submit(self):
        browser.element('#submit').click()
        return self

    def _should_have_register_user_with(self, *verification_data):
        for field, value in verification_data:
            browser.element(f'//td[preceding-sibling::td="{field}"]').should(have.exact_text(value))


