
import eel

# getcwdにより初期フォルダ確認済み
eel.init("eel_project/web")
eel.start("index.html")

# javascript側から呼び出す
@eel.expose
def test_python_func():
    return "Test"

 



