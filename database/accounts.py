import random

from database.postrgres import Postgres
import dataclasses


@dataclasses.dataclass
class Account:
    id: int
    name: str
    is_code_used: bool
    code: int


def is_user_registered(index: int) -> bool:
    with Postgres() as pg:
        if pg.select_one(f"SELECT * FROM accounts WHERE id = %s", (index,)):
            return True
    return False


def register_user(index: int, name: str):
    code = random.randint(100000, 1000000)
    is_code_used = False
    with Postgres() as pg:
        pg.insert(
            f"INSERT INTO accounts (id, name, is_code_used, code) VALUES (%s, %s, %s, %s)",
            (
                index,
                name,
                is_code_used,
                code,
            ),
        )


def get_new_code(index: int) -> int:
    code = random.randint(100000, 1000000)
    with Postgres() as pg:
        pg.update(
            f"UPDATE accounts SET code=%s, is_code_used=%s WHERE id=%s",
            (code, False, index),
        )
    return code


def get_info_about_user(code: int) -> Account:
    with Postgres() as pg:
        info = pg.select_one(f"SELECT * FROM accounts WHERE code = %s", (code,))
    return Account(id=info[0], name=info[1], is_code_used=info[2], code=info[3])


def disable_code(index: int):
    with Postgres() as pg:
        pg.update(
            "UPDATE accounts SET is_code_used=%s WHERE id=%s",
            (
                True,
                index,
            ),
        )


def try_login(code: int) -> bool:
    with Postgres() as pg:
        info = pg.select_one(
            "SELECT id, is_code_used FROM accounts WHERE code=%s", (code,)
        )
        if not info:
            return False
        if info[1] is True:
            return False
        disable_code(info[0])
        return True
