"""Tests that always fail -- used to verify --fail-fast behavior."""

import time


def test_fail_1():
    time.sleep(0.5)
    assert False, "intentional failure 1"


def test_fail_2():
    time.sleep(0.5)
    assert False, "intentional failure 2"


def test_fail_3():
    time.sleep(0.5)
    assert False, "intentional failure 3"


def test_fail_4():
    time.sleep(0.5)
    assert False, "intentional failure 4"


def test_fail_5():
    time.sleep(0.5)
    assert False, "intentional failure 5"


def test_fail_6():
    time.sleep(0.5)
    assert False, "intentional failure 6"


def test_fail_7():
    time.sleep(0.5)
    assert False, "intentional failure 7"


def test_fail_8():
    time.sleep(0.5)
    assert False, "intentional failure 8"


def test_fail_9():
    time.sleep(0.5)
    assert False, "intentional failure 9"


def test_fail_10():
    time.sleep(0.5)
    assert False, "intentional failure 10"
