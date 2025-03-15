from src.database.schema import User
from sqlmodel import Session, select

def test_read_main(test_client, test_db_session: Session):

    user = User(username="test", password="test", is_admin=0)
    test_db_session.add(user)
    test_db_session.commit()
    test_db_session.refresh(user)

    statement = select(User)
    user: User = test_db_session.exec(statement).first()
    assert user is not None
    assert user.username == "test"
    assert user.password == "test"

    response = test_client.get("/")
    assert response.status_code == 200