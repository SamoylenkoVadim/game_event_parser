import pytest
from main import Game, Player, Team


@pytest.fixture
def game():
    # team 1
    player1 = Player(playerID=1, gold=100, name="Player 1", alive=True)
    player2 = Player(playerID=2, gold=200, name="Player 2", alive=True)
    player3 = Player(playerID=3, gold=300, name="Player 3", alive=True)
    player4 = Player(playerID=4, gold=400, name="Player 4", alive=True)
    player5 = Player(playerID=5, gold=500, name="Player 5", alive=True)

    # team 2
    player6 = Player(playerID=6, gold=100, name="Player 6", alive=True)
    player7 = Player(playerID=7, gold=200, name="Player 7", alive=True)
    player8 = Player(playerID=8, gold=300, name="Player 8", alive=True)
    player9 = Player(playerID=9, gold=400, name="Player 9", alive=True)
    player10 = Player(playerID=10, gold=500, name="Player 10", alive=True)

    team1 = Team(teamID=1, players=[player1, player2, player3, player4, player5])
    team2 = Team(teamID=2, players=[player6, player7, player8, player9, player10])
    game = Game(matchID=1, fixture="Game 1", teams=[team1, team2])
    return game
