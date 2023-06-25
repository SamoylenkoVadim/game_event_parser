from main import Event


def test_apply_player_kill_event(game):
    event_payload = {
        "killerID": 1,
        "victimID": 6,
        "assistants": [2],
        "goldGranted": 100,
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(6)
    assistant = game.get_player(2)

    assert killer.player_kills == 1
    assert killer.gold == 200
    assert victim.alive is False
    assert assistant.assists == 1
    assert assistant.gold == 250


def test_apply_player_kill_event_invalid_killer(game):
    event_payload = {
        "killerID": 100,
        "victimID": 2,
        "assistants": [6],
        "goldGranted": 100,
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(100)
    victim = game.get_player(2)
    assistant = game.get_player(6)

    assert killer is None
    assert victim.alive is False
    assert assistant.assists == 1
    assert assistant.gold == 150


def test_apply_player_kill_event_no_killer(game):
    event_payload = {
        "victimID": 2,
        "assistants": [6],
        "goldGranted": 100,
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    victim = game.get_player(2)
    assistant = game.get_player(6)

    assert victim.alive is False
    assert assistant.assists == 1
    assert assistant.gold == 150


def test_apply_player_kill_event_invalid_killer_2(game):
    event_payload = {
        "killerID": "1",
        "victimID": 2,
        "assistants": [6],
        "goldGranted": 100,
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(2)
    assistant = game.get_player(6)

    assert killer.player_kills == 0
    assert victim.alive is False
    assert assistant.assists == 1
    assert assistant.gold == 150


def test_apply_player_kill_event_invalid_victim(game):
    event_payload = {
        "killerID": 1,
        "victimID": 100,
        "assistants": [2],
        "goldGranted": 100,
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(100)
    assistant = game.get_player(2)

    assert killer.player_kills == 1
    assert victim is None
    assert assistant.assists == 1
    assert assistant.gold == 250


def test_apply_player_kill_event_no_victim(game):
    event_payload = {
        "killerID": 1,
        "assistants": [2],
        "goldGranted": 100,
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    assistant = game.get_player(2)

    assert killer.player_kills == 1
    assert assistant.assists == 1
    assert assistant.gold == 250


def test_apply_player_kill_event_invalid_victim_2(game):
    event_payload = {
        "killerID": 1,
        "victimID": "6",
        "assistants": [2],
        "goldGranted": 100,
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(6)
    assistant = game.get_player(2)

    assert killer.player_kills == 1
    assert victim.alive is True
    assert assistant.assists == 1
    assert assistant.gold == 250


def test_apply_player_kill_event_invalid_assistants(game):
    event_payload = {
        "killerID": 1,
        "victimID": 6,
        "assistants": ["a", 2],
        "goldGranted": 100,
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(6)
    assistant1 = game.get_player("a")
    assistant2 = game.get_player(2)

    assert killer.player_kills == 1
    assert victim.alive is False
    assert assistant1 is None
    assert assistant2.assists == 1
    assert assistant2.gold == 250


def test_apply_player_kill_event_invalid_assistants_2(game):
    event_payload = {
        "killerID": 1,
        "victimID": 6,
        "assistants": ["3", 2],
        "goldGranted": 100,
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(6)
    assistant1 = game.get_player("3")
    assistant2 = game.get_player(2)

    assert killer.player_kills == 1
    assert victim.alive is False
    assert assistant1 is None
    assert assistant2.assists == 1
    assert assistant2.gold == 250


def test_apply_player_kill_event_invalid_assistants_type(game):
    event_payload = {
        "killerID": 1,
        "victimID": 6,
        "assistants": 2,
        "goldGranted": 100,
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(6)
    assistant = game.get_player(2)

    assert killer.player_kills == 1
    assert victim.alive is False
    assert assistant.assists == 0
    assert assistant.gold == 200


def test_apply_player_kill_event_no_assistants(game):
    event_payload = {
        "killerID": 1,
        "victimID": 6,
        "goldGranted": 100,
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(6)

    assert killer.player_kills == 1
    assert killer.gold == 200
    assert victim.alive is False


def test_apply_player_kill_event_no_gold_granted(game):
    event_payload = {
        "killerID": 1,
        "victimID": 6,
        "assistants": [2],
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(6)
    assistant = game.get_player(2)

    assert killer.player_kills == 1
    assert killer.gold == 100
    assert victim.alive is False
    assert assistant.assists == 1
    assert assistant.gold == 250


def test_apply_player_kill_event_none_gold_granted(game):
    event_payload = {
        "killerID": 1,
        "victimID": 6,
        "assistants": [2],
        "goldGranted": None,
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(6)
    assistant = game.get_player(2)

    assert killer.player_kills == 1
    assert killer.gold == 100
    assert victim.alive is False
    assert assistant.assists == 1
    assert assistant.gold == 250


def test_apply_player_kill_event_invalid_gold_granted(game):
    event_payload = {
        "killerID": 1,
        "victimID": 6,
        "assistants": [2],
        "goldGranted": "100",
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(6)
    assistant = game.get_player(2)

    assert killer.player_kills == 1
    assert killer.gold == 100
    assert victim.alive is False
    assert assistant.assists == 1
    assert assistant.gold == 250


def test_apply_player_kill_event_invalid_gold_granted_2(game):
    event_payload = {
        "killerID": 1,
        "victimID": 6,
        "assistants": [2],
        "goldGranted": "a",
        "assistGold": 50
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(6)
    assistant = game.get_player(2)

    assert killer.player_kills == 1
    assert killer.gold == 100
    assert victim.alive is False
    assert assistant.assists == 1
    assert assistant.gold == 250


def test_apply_player_kill_event_no_assist_gold(game):
    event_payload = {
        "killerID": 1,
        "victimID": 6,
        "assistants": [2],
        "goldGranted": 100
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(6)
    assistant = game.get_player(2)

    assert killer.player_kills == 1
    assert killer.gold == 200
    assert victim.alive is False
    assert assistant.assists == 1
    assert assistant.gold == 200


def test_apply_player_kill_event_invalid_assist_gold(game):
    event_payload = {
        "killerID": 1,
        "victimID": 6,
        "assistants": [2],
        "goldGranted": 100,
        "assistGold": "50"
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(6)
    assistant = game.get_player(2)

    assert killer.player_kills == 1
    assert killer.gold == 200
    assert victim.alive is False
    assert assistant.assists == 1
    assert assistant.gold == 200


def test_apply_player_kill_event_invalid_assist_gold_2(game):
    event_payload = {
        "killerID": 1,
        "victimID": 6,
        "assistants": [2],
        "goldGranted": 100,
        "assistGold": "a"
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(6)
    assistant = game.get_player(2)

    assert killer.player_kills == 1
    assert killer.gold == 200
    assert victim.alive is False
    assert assistant.assists == 1
    assert assistant.gold == 200


def test_apply_player_kill_event_none_assist_gold(game):
    event_payload = {
        "killerID": 1,
        "victimID": 6,
        "assistants": [2],
        "goldGranted": 100,
        "assistGold": None
    }
    event = Event(event_type='PLAYER_KILL', payload=event_payload)

    event.apply(game)

    killer = game.get_player(1)
    victim = game.get_player(6)
    assistant = game.get_player(2)

    assert killer.player_kills == 1
    assert killer.gold == 200
    assert victim.alive is False
    assert assistant.assists == 1
    assert assistant.gold == 200
