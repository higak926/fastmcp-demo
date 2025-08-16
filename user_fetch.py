import requests
from fastmcp import FastMCP
import random
import datetime
import sqlalchemy
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model import Base, UserIncome

mcp = FastMCP(name="User Fetch")


@mcp.tool
def user_fetch(user_id: int) -> str:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    response = requests.get(url)
    user_info = response.json()
    print(user_info, "user_info")
    engine = sqlalchemy.create_engine('sqlite:///sample_db.sqlite3', echo=True)
    Base.metadata.create_all(bind=engine)
    session = sessionmaker(bind=engine)()
    user_income = UserIncome()
    user_income.user_id = user_id
    user_income.name = user_info["name"]
    user_income.email = user_info["email"]
    user_income.income = random.randint(0, 10000)
    user_income.created_at = datetime.datetime.now()
    user_income.updated_at = datetime.datetime.now()
    session.add(instance=user_income)
    session.commit()
    return response.text


if __name__ == "__main__":
    mcp.run()
