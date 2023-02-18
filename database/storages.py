import dataclasses

from database.postrgres import Postgres


@dataclasses.dataclass
class Storage:
    owner: int
    storage_name: str
    storage_descr: str

def create_storage_db(owner, storage_name, storage_descr):
    with Postgres() as pg:
        pg.insert(
            f"INSERT INTO storages (owner_id, name, description) VALUES (%s, %s, %s)",
            (
                owner,
                storage_name,
                storage_descr,
            ),
        )


def get_storage_list():
    with Postgres() as pg:
        data = pg.select_all("SELECT * FROM storages", ())
    res = []
    for i in data:
        res.append(Storage(i[0], i[1], i[2]))
    return res


def get_storage_info(name):
    with Postgres() as pg:
        i = pg.select_one("SELECT * FROM storages WHERE name=%s", (name,))
        return Storage(i[0], i[1], i[2])
