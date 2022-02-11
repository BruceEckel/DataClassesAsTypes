def check(exp: bool, err_msg: str) -> None:
    if not exp:
        print(f"Type failure: {err_msg} out of range")
