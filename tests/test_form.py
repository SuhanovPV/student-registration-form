from student_registration_form.pages.registration_page import RegistrationPage
from student_registration_form.data import users

def test_fill_form():
    student = users.student
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.register(student)
    registration_page.should_have_registered(student)
