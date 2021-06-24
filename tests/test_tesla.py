tesla2 = Tesla("S", "blue", autopilot=True)


def test_color():
    assert tesla2.color == "blue"


def test_autopilot():
    assert tesla2.autopilot("tree") == "Tesla model S avoids tree"
