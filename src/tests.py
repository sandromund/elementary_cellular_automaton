from src.Automat import rule_to_bin_array


def test_rule_to_bin_array_30():
    assert list(rule_to_bin_array(30)) == [0, 0, 0, 1, 1, 1, 1, 0]


def test_rule_to_bin_array_126():
    assert list(rule_to_bin_array(126)) == [0, 1, 1, 1, 1, 1, 1, 0]


def test_rule_to_bin_array_220():
    assert list(rule_to_bin_array(220)) == [1, 1, 0, 1, 1, 1, 0, 0]
