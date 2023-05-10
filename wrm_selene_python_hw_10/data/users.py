import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    full_name: str = dataclasses.field(init=False)
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

    def __post_init__(self):
        self.full_name = f'{self.first_name} {self.last_name}'


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
