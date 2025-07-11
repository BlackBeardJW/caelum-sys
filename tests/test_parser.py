from caelum_sys.parser import parse_command

def test_parse_open():
    assert parse_command("Open Notepad")[0] == "open_app"

def test_parse_kill():
    assert parse_command("kill spotify")[0] == "kill_process"

def test_parse_list():
    assert parse_command("list processes")[0] == "list_processes"

def test_parse_unknown():
    assert parse_command("foobar")[0] == "unknown"
