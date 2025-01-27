from src.genai_beispiele.funktionen_module import ping_pong


def test_ping_pong():
    assert ping_pong(3) == "Ping"
    assert ping_pong(5) == "Pong"
    assert ping_pong(15) == "Ping Pong"
    assert ping_pong(7) == 7
    assert ping_pong(30) == "Ping Pong"
    assert ping_pong(9) == "Ping"
    assert ping_pong(10) == "Pong"


