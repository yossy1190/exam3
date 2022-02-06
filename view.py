import eel
# desktop.pyの関数を利用するため、importする
import desktop
import search
import pandas as pd


# eel_projectの直下にhtmlフォルダあり
app_name="eel_project/html"
# htmlフォルダの直下にあるindex.htmlを参照
end_point="index.html"
size=(700,600)

@eel.expose
def python_function2(val):
    return val

@ eel.expose
def kimetsu_search(word):
    search.kimetsu_search(word)
    df=pd.read_csv("eel_project/source.csv")
    source=list(df["name"])
    if word in source:
        return "『{}』はリストにあります".format(word)
    else:
        source.append(word)
        # CSV書き込み
        df=pd.DataFrame(source,columns=["name"])
        df.to_csv("eel_project/source.csv",encoding="utf_8-sig")
        return "『{}』はリストにありません。リストに追加します。".format(word)

        
desktop.start(app_name,end_point,size)


