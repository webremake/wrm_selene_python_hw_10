import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile_phone: str
    year_of_birth: str
    month_of_birth: str
    day_of_birth: str
    subjects: str
    hobbies: str
    picture: str
    current_address: str
    state: str
    city: str


student = User(
    first_name='Jon',
    last_name='Dir',
    email='jondir@example.com',
    gender='Male',
    mobile_phone='5296846163',
    year_of_birth='1957',
    month_of_birth='May',
    day_of_birth='12',
    subjects='Commerce',
    hobbies='Reading',
    picture='gl.jpg',
    current_address='This is my current address in New York USA',
    state='Haryana',
    city='Karnal'
)
