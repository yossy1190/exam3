import eel
import desktop
import search

app_name="C:/Users/Yoshi/Project2/study-03-desktop-01-master/study-03-desktop-01-master/html"
end_point="C:/Users/Yoshi/Project2/study-03-desktop-01-master/study-03-desktop-01-masterhtml/index.html"
size=(700,600)

#js側から、kimetsu_search関数が呼び出せるように@eel.exposeでデコレートする
@ eel.expose
def kimetsu_search(val):
    # searchファイルのなかのkimetsu_search関数を呼び出している
    # ＝＞jsからkimetsu_searchが呼び出せるようになる。
    # search.kimetsu_search(word)
    return val
desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)