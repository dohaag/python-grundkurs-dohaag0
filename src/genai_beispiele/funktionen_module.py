# Ping Pong Funktion
# Erstelle eine Funktion die als Parameter eine Zahl erhält.
# Ist die Zahl ein Vielfaches von 3, so soll die Funktion "Ping" zurückgeben.
#  Ist
# die Zahl ein Vielfaches von 5, so soll die Funktion "Pong" zurückgeben. Ist
#  die
# Zahl ein Vielfaches von 3 und 5, so soll die Funktion "Ping Pong"
# zurückgeben.
# Ansonsten gibt die Zahl zurück. Erstelle Unit Tests für die Funktion.

from typing import Union


def ping_pong(number: int) -> Union[str, int]:
    """
    Gibt "Ping", "Pong" oder "Ping Pong" zurück, abhängig davon, ob die
    Eingabezahl
    durch 3, 5 oder beide teilbar ist.

    Args:
        number (int): Die zu prüfende Zahl.

    Returns:
        str | int: "Ping", wenn die Zahl durch 3 teilbar ist, "Pong", wenn die
          Zahl durch 5 teilbar ist,
                   "Ping Pong", wenn die Zahl durch 3 und 5 teilbar ist,
                     ansonsten die Eingabezahl.
    """
    if number % 3 == 0 and number % 5 == 0:
        return "Ping Pong"
    elif number % 3 == 0:
        return "Ping"
    elif number % 5 == 0:
        return "Pong"
    else:
        return number


# Unit tests

# Listen Invertieren
# Erstelle eine Funktion die als Parameter eine Liste erhält. Die Funktion soll
# die Liste invertieren und zurückgeben. Beispiel: [1, 2, 3] -> [3, 2, 1].
# Erstelle Unit Tests für die Funktion.

# Finde den Höchsten zahlenwert Unabhängig vom Vorzeichen
# Erstelle eine Funktion die als Parameter eine Liste erhält. Die Funktion soll
# das Element mit dem größten Zahlenwert zurückgeben. Dabei soll der Vorzeichen
# nicht berücksichtigt werden. Beispiel: [1, -2, 3, -4] -> 4. Erstelle Unit Tests.
