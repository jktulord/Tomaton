import peewee

db = peewee.SqliteDatabase('users.db')


class User(peewee.Model):
    chat_id = peewee.IntegerField(unique=True)
    state = peewee.IntegerField(default = 0)

    class Meta:
        database = db


def init():
    db.connect()
    db.create_tables([User], safe=True)
    db.close()


def get_state(chat_id):
    user = User.get_or_none(chat_id=chat_id)
    if user is None:
        return None

    return user.state


def set_state(chat_id,state):
    user, created = User.get_or_create(chat_id=chat_id)

    user.state = state
    user.save()


init()
