from prueba1_gha.main import build_hi


def test_build_hi():
    assert build_hi("More") == "Hi, More"
