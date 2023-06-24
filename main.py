import json
import logging
import os
import pprint

from model import Game, Team, Event, Player


def process_events_from_files(directory):
    logging.info("Started")
    events_json = []

    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            try:
                with open(os.path.join(directory, filename), 'r') as f:
                    event = json.load(f)
                    events_json.append(event)
            except ValueError:
                logging.error("Invalid JSON: {}".format(filename))
            except Exception as error:
                logging.error(error)

    match_start_event = next((event for event in events_json if event['type'] == 'MATCH_START'), None)
    match_end_event = next((event for event in events_json if event['type'] == 'MATCH_END'), None)

    if match_start_event is None:
        raise Exception("No 'MATCH_START' event found.")

    if match_end_event is None:
        raise Exception("No 'MATCH_END' event found.")

    events_json.remove(match_start_event)
    events_json.remove(match_end_event)

    game = Game(
        match_start_event['matchID'],
        match_start_event['payload']['fixture'],
        [Team(team['teamID'], [Player(**player) for player in team['players']]) for team in match_start_event['payload']['teams']]
    )

    for event_json in events_json:
        event = Event(event_json['type'], event_json['payload'])
        event.apply(game)

    match_end_event = Event(match_end_event['type'], match_end_event['payload'])
    match_end_event.apply(game)
    logging.info("Completed")

    pprint.pprint(game.to_dict())

    return game

folder_path = "/Users/vadim/workspace/python_coding_challenge_bayes 3/data"
process_events_from_files(folder_path)
