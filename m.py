import pyautogui
import time

# 啟用防止故障保護機制
pyautogui.FAILSAFE = True

### to do 
### 1.*判定*雷電的視窗
### 2.找到釣魚的按鈕 並*判定*此時為閒置狀態
### 2-1.判定失敗 -> exit
### 2-2.判定成功 -> 按下按鈕
### 3.拋竿成功*判定* (跳過，未來預定)
### 4.開始釣魚 並等待 (*判定*是否上鉤的迴圈)
### 5.*判定*是否為大成功
### 5-1.大成功 -> 按下按鈕
### 5-2.一般魚 -> 放掉 並回到3.
### 6.開始釣魚 並且保持拉桿 (*判定*拉桿)
### 7.拉桿同時判定是否釣上魚
### 8.同時BOSS戰狀況
### 8-1.QTE放棄 (未來預定)
### 8-2.拉魚判定
### 9.釣魚成功 按下難紐結束
### 10.移動鍵盤滑鼠 則退出腳本 -> exit

## ----變量字典---- ##
FData={
    "posX": 0,"posY": 0,
    "fromX": 0,"fromY": 0,"toX": 0,"toY": 0,
    "nowRGB": (0, 0 ,0 ),
    "LDplayer": (-16, -16),
    "Auto": (290,150),
    "FBtn": (286, 182),
    "Loading": (160,120),
    "Femoji": (52, 120),
    "FemojiRGB": (255,255,239),
    "Heroface": (52,150)
}

def posINI():
    FData["Auto"] = PosMove(FData["LDplayer"],FData["Auto"])
    print("+ Auto按鈕初始化，座標為：", FData["Auto"])

    FData["FBtn"] = PosMove(FData["LDplayer"],FData["FBtn"])
    print("+ 釣魚按鈕初始化，座標為：", FData["FBtn"])

    FData["Loading"] = PosMove(FData["LDplayer"],FData["Loading"])
    print("+ Loading位置初始化，座標為：", FData["Loading"])

    FData["Femoji"] = PosMove(FData["LDplayer"],FData["Femoji"])
    print("+ 釣魚泡泡框位置初始化，座標為：", FData["Femoji"])

    FData["Heroface"] = PosMove(FData["LDplayer"],FData["Heroface"])
    print("+ 英雄臉部位置初始化，座標為：", FData["Heroface"])

## ----找點用函數---- ##
def nowPosCheck(x):
    if str(x) == "None" :
        print("畫面中找不到圖片： nowPos is",x)
        print("\n:::結束程式:::")
        exit()
    else:
        print("... Check Done, nowPos not None")

## ----找色用函數---- ##
def getRGB(x):
    im = pyautogui.screenshot(region=(PosRange(x,1)))
    nowRGB = im.getpixel((1, 1))
    FData["nowRGB"] = nowRGB
    
## ----計算座標相加用函數(座標1, 座標2)---- ##
def PosMove(a, b):
    x1, y1 = a
    x2, y2 = b
    #print("x1:",x1 ," y1:", y1 ," x2:",x2," y2:",y2)
    c = (x1+x2, y1+y2)
    #print("PosMove計算結果:",c)
    FData["posX"], FData["posY"] = c
    return c

## ----計算範圍用函數(中心點, 半徑)---- ##
def PosRange(pos, n):
    FData["posX"], FData["posY"] = pos
    x, y = pos

    fromX = x - n
    fromY = y - n
    toX = x + n
    toY = y + n

    R = (fromX, fromY, toX, toY)
    FData["fromX"], FData["fromY"], FData["toX"], FData["toY"] = R
    
    #print("PosRange計算結果: (",FData["fromX"],", ",FData["fromY"],") to (",FData["toX"],", ",FData["toY"],")")
    return R

## ----點擊事件函數---- ##
def clickEven(posClk):
    posX, posY = posClk
    FData["posX"], FData["posY"] = posClk
    # 移动鼠标
    pyautogui.moveTo(posX, posY, duration=0.1)
    # 点击
    pyautogui.click()
    print("*click*")

## ----等待顏色匹配迴圈函數---- ##
def waitingRGBnotMatch(findRGB,pos):
    while 1:
        getRGB(pos)
        #print("... nowRGB is",FData["nowRGB"],"pastRGB is", pastRGB)
        if findRGB == FData["nowRGB"]:
            print("... waitting")
            time.sleep(0.5)
            continue
        else:
            #print("- Done -")
            break

## ----Loading檢查用函數(按哪邊會開始Loading)---- ##
def loadingChecking(x):
    # 移動滑鼠到LOADING位置
    pyautogui.moveTo(FData["Loading"], duration=0.1)

    # 找色函數
    getRGB(FData["Loading"])
    pastRGB = FData["nowRGB"]
    #print("+ 獲取Loading前RGB：", FData["nowRGB"],"位置：",FData["Loading"])

    # 按下釣魚按鈕
    pyautogui.moveTo(x, duration=0.1)
    clickEven(x)
    
    print("now Loading ...")
    ## Loading框框出現了 ##
    waitingRGBnotMatch(pastRGB,FData["Loading"])
    ## Loading框框消失了 ##
    waitingRGBnotMatch(pastRGB,FData["Loading"])
    print("Loading finish ...")

def AAfish():
    print(
        "   　＼　　　　　　　＿＿＿＿＿＿＿＿＿＿__／ゝ                      ",
        "\n　　　 ＼　,,ー‐‐丶;;;;;;;;;;;ヽ;;;;;;;;;;;ヽ' 　ゝ              ",
        "\n　　　　　X/~゜`＼ヾ （●）;;;;;;ヽ;;;;;;;;;;;;;ヽ' ゝ             ",
        "\n　　　　　ヽ＼　　 ＼ゝ;;;;;;;;;;;|;;;　＿＿;;;;;ヽ' ゝ            ",
        "\n　　　　　　 | |＼　　 》　　　　;;;丿;;／　 ,／;;;;;＼/           ",
        "\n　　　　　　//,,　＼〃ゝ　 　　丿(〆　 _／;i|!|;;;;;;;;＼          ",
        "\n　　　　　（二二ノゾ　 　 　 ノ　　 ⌒￣;;;;;;|!|i;;;;;;;;|         ",
        "\n　　　　　　ヽー-ニニーーー'''''´　　　　　　　 ;;;;!|i|;|        ",
        "\n　　　　　　　　　ヽーーヽ_　_　　  　　　　　　 ;;|!|!;;|         ",
        "\n　　　　　　´ 　　　　　　　   ＼_ ＜￣,,/ 　 　 ;;;i|!;;;|         ",
        "\n　　　　　　　゜ 　　　　　　　　 　｀＼_　＼/　　　.;;;|i|        ",
        "\n　　　　　　;　　　　　 　 　'　　　　 　 ｀`ヽ　　　 　.;;/　　　　",
        "\n　　　　　　　　　、　 　　 　゜　　　　　　　 ｀`ヽ　　,/　　｀　　 ",
        "\n　　　　　。　 　　　　　　　　　　　　　　_＿＿__ソ　, /　　　。     ",
        "\n　　　　　　　　　　　　　　　　　　　　　＼;;;;;　 ,  /　;゜　 、    ",
        "\n　　　　　　　　　　;´　　　　　　　゜　。　　 ゞ,;;;;/              ",
        "\n‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

###--------------------------------------------
###============     主程式開始    ==============
###--------------------------------------------
### 1.*判定*雷電的視窗
print("------------------1.初始化")
nowPos = pyautogui.locateCenterOnScreen('LDPlayerIcon.png')
nowPosCheck(nowPos) # 確認不為None
print("以 LDPlayerIcon.png 找到遊戲視窗位置\n座標為：", nowPos)

pyautogui.moveTo(nowPos, duration=0.1)

# 將找到的中心點位置重新歸零
FData["LDplayer"] = PosMove(nowPos,FData["LDplayer"])
print("+ 定位視窗的左上角，座標為：", FData["LDplayer"])

### 重新初始化字典內座標 ###
print("開始初始化字典座標")
posINI()

### 2.找到自動釣魚的按鈕 並*判定*此時為閒置狀態
print("------------------2.確認Auto按鈕狀態")

nowPos = pyautogui.locateCenterOnScreen('AutoBtn.png', region=(PosRange(FData["Auto"],20)), confidence=0.9)
nowPosCheck(nowPos) # 確認不為None
print("以 AutoBtn.png 自動釣魚按鈕\n座標為", nowPos)

pyautogui.moveTo(nowPos, duration=1)
time.sleep(1)

while 1:
    ### 3.拋竿成功*判定* (跳過，未來預定)
    print("------------------3.拋竿")
    #按下按鈕並等待Loading結束
    loadingChecking(FData["FBtn"])

    print("...拋竿大成功*判定*函數未編寫，等待 3 秒後跳過")
    time.sleep(3)

    #按下按鈕並等待Loading結束
    loadingChecking(FData["FBtn"])
  
    ### 4.開始釣魚 並等待 (*判定*是否上鉤的迴圈)
    print("------------------4.開始釣魚")
    print("... fly fishing bait")

    #移動滑鼠到Loading上
    pyautogui.moveTo(FData["Loading"], duration=3.5)
    
    print("... now waitting for fish")
    ## 判定釣魚泡泡出現了 ##
    waitingRGBnotMatch(FData["FemojiRGB"],FData["Femoji"])
    ## 判定出現了驚嘆號 ##
    waitingRGBnotMatch(FData["FemojiRGB"],FData["Femoji"])
    print("- 魚上鉤了 -")

    ## 用臉判斷魚的大小 ##
    for i in range(3):
        nowPos = pyautogui.locateCenterOnScreen('BossFishFace.png', region=(PosRange(FData["Heroface"],10)), confidence=0.9)
        print("以 BossFishFace.png 判斷魚的大小，座標為--", nowPos)
        if str(nowPos) == "None":
            time.sleep(0.5)
            continue 
        else:
            print("\n                  ::::【大雞雞魚】::::")
            AAfish()
            clickEven(FData["FBtn"])
            exit()

    print("\n【小雞雞魚】\n  <。)))>< ...\n")
    pyautogui.moveTo(FData["FBtn"], duration=4)
    

### 5.*判定*是否為大成功
### 5-1.大成功 -> 按下按鈕
### 5-2.一般魚 -> 放掉 並回到3.
### 6.開始釣魚 並且保持拉桿 (*判定*拉桿)
### 7.拉桿同時判定是否釣上魚
### 8.同時BOSS戰狀況
### 8-1.QTE放棄 (未來預定)
### 8-2.拉魚判定
### 9.釣魚成功 按下難紐結束
### 10.移動鍵盤滑鼠 則退出腳本 -> exit


print("\n\n::::程式結束::::")
exit()