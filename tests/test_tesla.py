from Tesla import Tesla

tesla1 = Tesla("S", "blue", autopilot=True)


def test_color():
    assert tesla1.color == "blue"


def test_autopilot():
    assert tesla1.autopilot("tree") == "Tesla model S avoids tree"
