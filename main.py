import json
import logging
import os
import pprint
from model import Game, Team, Event, Player

logging.getLogger().setLevel(logging.WARNING)


def process_events_from_files(directory):
    logging.info("Started")
    events_json = {}

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            try:
                with open(os.path.join(directory, filename), 'r') as f:
                    event = json.load(f)
                    events_json[filename] = event
            except ValueError:
                logging.error("Invalid JSON: {}".format(filename))
            except Exception as error:
                logging.error(error)

    events_to_remove = []
    match_start_event = None
    match_end_event = None

    for filename, event in events_json.items():
        if event.get('type') == 'MATCH_START':
            match_start_event = event
            events_to_remove.append(filename)
        elif event.get('type') == 'MATCH_END':
            match_end_event = event
            events_to_remove.append(filename)

    if match_start_event is None:
        raise Exception("No 'MATCH_START' event found.")

    if match_end_event is None:
        raise Exception("No 'MATCH_END' event found.")

    for filename in events_to_remove:
        del events_json[filename]

    teams = match_start_event.get('payload', {}).get('teams', [])
    game = Game(
        match_start_event.get('matchID'),
        match_start_event.get('payload', {}).get('fixture', {}),
        [Team(team.get('teamID'), [Player(**player) for player in team.get('players', [])]) for team in teams]
    )

    for filename, event_json in events_json.items():
        logging.info("Processing file: {}".format(filename))
        event = Event(event_json.get('type', "UNKNOWN"), event_json.get('payload', {}))
        event.apply(game, filename)

    match_end_event = Event(match_end_event.get('type'), match_end_event.get('payload'))
    match_end_event.apply(game)
    logging.info("Completed")

    pprint.pprint(game.to_dict())

    return game


data_folder = os.path.join(os.path.dirname(__file__), 'data')
process_events_from_files(data_folder)
