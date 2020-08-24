import os
from faker import Faker
from routes import get_token, get_user_Id

EMAIL = os.environ['LEAF_EMAIL']
PASS = os.environ['LEAF_PASS']
TOKEN = get_token(EMAIL, PASS)
USER_ID = get_user_Id(TOKEN)

fake = Faker()
Faker.seed(4321)
valid_field_id = fake.uuid4()

valid_coords = [[[[-1.0, -1.0],
                  [-1.0, +1.0],
                  [+1.0, +1.0],
                  [+1.0, -1.0],
                  [-1.0, -1.0]]]]
