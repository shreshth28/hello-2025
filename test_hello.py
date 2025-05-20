import subprocess

def test_default():
    out = subprocess.run(["python3", "hello.py"], capture_output=True, text=True).stdout
    assert out.strip() == "Hello, world!"
