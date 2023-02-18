import dataclasses

from database.postrgres import Postgres


@dataclasses.dataclass
class Shop:
    owner: int
    shop_name: str
    shop_link: str
    client_id: str
    api_token: str


def create_shop_db(owner, shop_name, shop_link, client_id, api_token):
    with Postgres() as pg:
        pg.insert(
            f"INSERT INTO shops (owner, shop_name, shop_link, client_id, api_token) VALUES (%s, %s, %s, %s, %s)",
            (
                owner,
                shop_name,
                shop_link,
                client_id,
                api_token
            ),
        )


def get_shop_list():
    with Postgres() as pg:
        data = pg.select_all("SELECT * FROM shops", ())
    res = []
    for i in data:
        res.append(Shop(i[0], i[1], i[2], i[3], i[4]))
    return res


def get_shop_info(api_token):
    with Postgres() as pg:
        i = pg.select_one("SELECT * FROM shops WHERE api_token=%s", (api_token,))
        return Shop(i[0], i[1], i[2], i[3], i[4])
