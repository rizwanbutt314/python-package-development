from src.sampleworld import sample_world


def test_without_param():
    assert sample_world() == 'Name missing !'


def test_with_param():
    assert sample_world(name='Rizwan') == 'Given Name: Rizwan'
