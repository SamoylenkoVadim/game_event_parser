from model import Event


def test_apply_dragon_kill_event(game):
    event_payload = {
        "killerID": "player1",
        "goldGranted": 100
    }
    event = Event(event_type='DRAGON_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player("player1")

    assert killer.dragon_kills == 1
    assert killer.gold == 200


def test_apply_dragon_kill_event_invalid_killer(game):
    event_payload = {
        "killerID": "1",
        "goldGranted": 100
    }
    event = Event(event_type='DRAGON_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player("1")

    assert killer is None


def test_apply_dragon_kill_event_invalid_killer_type(game):
    event_payload = {
        "killerID": 1,
        "goldGranted": 100
    }
    event = Event(event_type='DRAGON_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)

    assert killer is None


def test_apply_dragon_kill_event_invalid_killer_type_2(game):
    event_payload = {
        "killerID": [1],
        "goldGranted": 100
    }
    event = Event(event_type='DRAGON_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)

    assert killer is None


def test_apply_dragon_kill_event_none_killer(game):
    event_payload = {
        "killerID": None,
        "goldGranted": 100
    }
    event = Event(event_type='DRAGON_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)

    assert killer is None


def test_apply_dragon_kill_event_no_killer(game):
    event_payload = {
        "goldGranted": 100
    }
    event = Event(event_type='DRAGON_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)

    assert killer is None


def test_apply_dragon_kill_event_no_gold_granted(game):
    event_payload = {
        "killerID": "player1",
    }
    event = Event(event_type='DRAGON_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player("player1")

    assert killer.dragon_kills == 1
    assert killer.gold == 100


def test_apply_dragon_kill_event_gold_granted_is_none(game):
    event_payload = {
        "killerID": "player1",
        "goldGranted": None
    }
    event = Event(event_type='DRAGON_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player("player1")

    assert killer.dragon_kills == 1
    assert killer.gold == 100


def test_apply_dragon_kill_event_invalid_gold_granted(game):
    event_payload = {
        "killerID": "player1",
        "goldGranted": "a"
    }
    event = Event(event_type='DRAGON_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player("player1")

    assert killer.dragon_kills == 1
    assert killer.gold == 100


def test_apply_dragon_kill_event_invalid_type_gold_granted(game):
    event_payload = {
        "killerID": "player1",
        "goldGranted": "100"
    }
    event = Event(event_type='DRAGON_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player("player1")

    assert killer.dragon_kills == 1
    assert killer.gold == 100


def test_apply_dragon_kill_event_invalid_type_gold_granted_2(game):
    event_payload = {
        "killerID": "player1",
        "goldGranted": [1000]
    }
    event = Event(event_type='DRAGON_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player("player1")

    assert killer.dragon_kills == 1
    assert killer.gold == 100

