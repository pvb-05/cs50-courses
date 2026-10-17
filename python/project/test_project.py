import pomodoro
import pytest

def test_valid_time():
    assert pomodoro.valid_time(1) == True
    assert pomodoro.valid_time(30) == True
    with pytest.raises(ValueError):
        pomodoro.valid_time(-1)

def test_format_time():
    assert pomodoro.format_time(60) == '01:00'
    assert pomodoro.format_time(59) == '00:59'
    assert pomodoro.format_time(1500) == '25:00'
    assert pomodoro.format_time(0) == '00:00'

def  test_category_message():
    assert pomodoro.category_message("POMODORO CLOCK STOPPED.") == False
    assert pomodoro.category_message("WORK HOURS OVER! IT'S BREAK OUT TIME.") == True
    assert pomodoro.category_message("LONG BREAK OVER! TIME TO GET BACK TO WORK.") == True
    assert pomodoro.category_message("SHORT BREAK OVER! TIME TO GET BACK TO WORK.") == True
