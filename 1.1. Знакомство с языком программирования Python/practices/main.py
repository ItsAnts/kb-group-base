import json

class User:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def get_dict(self) -> dict[str, str]:
        return {"username": self.username, "password": self.password}
    
def get_user(username: str) -> User | None:
    with open("data.json", "r", encoding="utf-8") as file:
        data: list[dict[str, str]] = json.load(fp=file)
        for account in data:
            if account.get(username):
                return User(account["username"], account["password"])

def create_user(new_user: User) -> User | None:
    user = get_user(username=new_user.username)
    if user is None:
        with open("data.json", "w", encoding="utf-8") as file:
            json.dump(obj=new_user.get_dict(), fp=file)
        return new_user
    
new_account = User(username="Yury", password="test2026")
create_user(new_user=new_account)
