import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: dict[str, str]
    subjects: ()
    hobbies: ()
    picture: str
    current_address: str
    state: str
    city: str


student = User(
    first_name='Pavel',
    last_name='Sukhar',
    email='sukhar@mail.com',
    gender='Male',
    mobile='8800535653',
    date_of_birth={'year': '1988', 'month': 'April', 'day': '05'},
    subjects=('Maths', 'Computer Science'),
    hobbies=('Sports', 'Music'),
    picture='pic.png',
    current_address='Bawana Rd, Shahabad Daulatpur, Shahabad Daulatpur Village, Rohini',
    state='Rajasthan',
    city='Jaipur'
)
