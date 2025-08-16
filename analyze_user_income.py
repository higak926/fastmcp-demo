from fastmcp import FastMCP
import sqlalchemy
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from model import Base, UserIncome

mcp = FastMCP(name="Analyze User Income")


@mcp.tool
def analyze_user_income(user_id: int) -> str:
    engine = sqlalchemy.create_engine('sqlite:///sample_db.sqlite3', echo=True)
    Base.metadata.create_all(bind=engine)
    session = sessionmaker(bind=engine)()
    query_res = session.query(UserIncome).filter_by(user_id=user_id)
    result = ""
    if not session.query(query_res.exists()).scalar():
        return "not exists user income"
    for user_income in query_res:
        result += f"{user_income.to_dict()} "

    return result


if __name__ == "__main__":
    mcp.run()
