from student_registration_form.pages.registration_page import RegistrationPage


def test_fill_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Pavel')
    registration_page.fill_last_name('Sukhar')
    registration_page.fill_email('sukhar@mail.com')
    registration_page.select_gender('Male')
    registration_page.fill_mobile('8800535653')
    registration_page.fill_date_of_birth('1988', '3', '05')
    registration_page.fill_subjects('Maths')
    registration_page.fill_subjects('Computer Science')
    registration_page.select_hobbies('Sports')
    registration_page.select_hobbies('Music')
    registration_page.fill_current_address('Bawana Rd, Shahabad Daulatpur, Shahabad Daulatpur Village, Rohini')
    registration_page.upload_picture('pic.png')
    registration_page.select_state('Rajasthan')
    registration_page.select_city('Jaipur')
    registration_page.submit()

    # THEN
    registration_page.should_have_register_user_with(
        "Pavel Sukhar",
        'sukhar@mail.com',
        'Male',
        '8800535653',
        '05 April,1988',
        'Maths, Computer Science',
        'Sports, Music',
        'pic.png',
        'Bawana Rd, Shahabad Daulatpur, Shahabad Daulatpur Village, Rohini',
        'Rajasthan Jaipur'
    )
