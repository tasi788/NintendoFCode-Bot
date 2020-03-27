from bot.functions import db_tools


def test_db_tools():
    assert db_tools.use_mongo()
