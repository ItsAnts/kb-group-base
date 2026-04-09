def require_role(role: str):
    def wrap(func): 
        def called(*args, **kwargs):
            user_role = args[0]["role"]
            if user_role != role:
                raise PermissionError
            result = func(*args, **kwargs)
            return result
        return called
    return wrap
    
@require_role("admin")
def delete_user(user: dict[str, str]) -> None:
    print("User deleted")

@require_role("view")
def create_post(user: dict[str, str], post: dict[str, str]) -> None:
    print("User create post")

user = {"role": "admin"}
user_no = {"role": "view"}
delete_user(user)
delete_user(user_no)