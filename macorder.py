import os
import time
import colorama
from colorama import Fore,Style
colorama.init(autoreset=True)

class Product:
    def __init__(self,name,price,count) :
        self.name = name
        self.price = price
        self.count = count

genre = ["バーガー","サイドメニュー","スイーツ","マックカフェ","ドリンク"]
genreColor = [Fore.RED,Fore.GREEN,Fore.YELLOW,Fore.MAGENTA,Fore.CYAN]
goroFace = ["('ω')","( ε: )","(.ω.)","( :3 )","('ω')"]
returnHomepage = False
gameover = False
def homepage():#主畫面
    os.system('cls')
    print()
    print(Fore.BLUE + "********************天上マックへようこそ！********************\n")
    print(f"注文したい{Style.BRIGHT}ジャンル{Style.RESET_ALL}の番号を入力してください: \n")
    print(f"1) {Fore.RED}バーガー{Fore.RESET}\n2) {Fore.GREEN}サイドメニュー{Fore.RESET}\n3) {Fore.YELLOW}スイーツ{Fore.RESET}\n4) {Fore.MAGENTA}マックカフェ{Fore.RESET}\n5) {Fore.CYAN}ドリンク{Fore.RESET}\n6) お会計\n7){Style.DIM} ケンタが食いたいっす！{Style.RESET_ALL}\n\nあなたの選択: ",end='')
    global returnHomepage
    returnHomepage = False
    genreChoice = int(input())
    os.system('cls')
    if(genreChoice==6):#確認是否結帳畫面
        payCheck()
    elif(genreChoice==7):#goKFC
        rootKFC()

    return genreChoice

def printMenu(genreChoice):#印菜單
    os.system('cls')
    print()
    print(f"{genreColor[genreChoice-1]}************************ {genre[genreChoice-1]} ************************\n\n")
    print(f"注文したい {genre[genreChoice-1]} の番号を入力してください:\n")
    count = 1
    for i in list[genreChoice-1]:
        print(f"{count}) {i.name}", end='')
        for j in range(48-len(i.name)*2):#根據不同品項的名字長度印space,為了對齊
            print(" ", end='')
        print(f"{Fore.YELLOW}￥{i.price}")
        count += 1
        
    print(f"{count}) メインメニューに戻る")
    print("\nあなたの選択: ",end="")

    menuChoice = int(input())
    if(menuChoice==count):#回主畫面
        global returnHomepage 
        returnHomepage = True
    else:
        buy(genreChoice,menuChoice,list[genreChoice-1])
    
   
def buy(genreChoice,menuChoice,product):#買商品並記錄數量
    os.system('cls')
    print("\n")
    print(f"注文したい {Fore.YELLOW}{product[menuChoice-1].name}{Fore.RESET} の数を入力してください:\n\nほしい数: ",end='')
    productCount = int(input())
    product[menuChoice-1].count += productCount
    os.system('cls')
    print("\n")
    print(f"{Fore.YELLOW}{product[menuChoice-1].name}{Fore.RESET} を {Fore.YELLOW}{productCount}個{Fore.RESET} ショッピングカートに入れました！")
    time.sleep(0.3)
    os.system('cls')
    print("\n")
    time.sleep(0.3)
    print(f"{Fore.YELLOW}{product[menuChoice-1].name}{Fore.RESET} を {Fore.YELLOW}{productCount}個{Fore.RESET} ショッピングカートに入れました！")
    time.sleep(0.3)
    os.system('cls')
    print("\n")
    time.sleep(0.3)
    print(f"{Fore.YELLOW}{product[menuChoice-1].name}{Fore.RESET} を {Fore.YELLOW}{productCount}個{Fore.RESET} ショッピングカートに入れました！")
    time.sleep(2)
    printMenu(genreChoice)#購買完後回去該種類的菜單

def payCheck():#確認是否結帳
    os.system('cls')
    print("\n")
    print("お会計しますか？\n1) はい\n2) いいえ、メインメニューに戻る\n\nあなたの選択: ",end='')
    ans = int(input())
    if(ans==1):#進入結帳畫面
        global returnHomepage
        returnHomepage = True
        pay()
    elif(ans==2):#回到主畫面
        os.system('cls')
        returnHomepage = True

def pay():#確認結帳，結束程式
    os.system('cls')
    global gameover
    gameover = True

def receiptAnimation():#印發票前的動畫
    for i in range(5):
        os.system('cls')
        print()
        print(f"レシート作成中...",end='')
        for j in range(i):
            print("...",end='')
        print(f"{Fore.YELLOW}{goroFace[i]}")
        time.sleep(1)

def printSpace(price):#印發票時每個品項的最後依價錢的位數補上不同個數的space,為了對齊
    if(price>=100 and price<1000):
        for i in range(6):
            print(" ",end='')
    elif(price>=1000 and price<10000):
        for i in range(5):
            print(" ",end='')
    else:
        for i in range(4):
            print(" ",end='')

def rootKFC():
    os.system('cls')
    print("\n")
    print(f"うるせぇ！！\nマック来てケンタ食いたいって言う奴には、そこら辺の{Fore.GREEN}草{Fore.RESET}でも食わせておけ！")
    time.sleep(5)
    global returnHomepage
    returnHomepage = True

def printReceipt(list):#印發票
    receiptAnimation()
    os.system('cls')
    print()
    print(f"{Fore.BLUE}--------------------------------------------------------------")#62-
    print(f"{Fore.BLUE}|",end='')
    for i in range(60):#印space對齊
        print(" ",end='')
    print(f"{Fore.BLUE}|")
    print(f"{Fore.BLUE}|{Fore.RESET}                 M  天上マック台湾支店  M                   {Fore.BLUE}|")
    for i in range(2):
        print(f"{Fore.BLUE}|",end='')
        for j in range(60):
            print(" ",end='')
        print(f"{Fore.BLUE}|")

    print(f"{Fore.BLUE}|{Fore.RESET} レジNO 87                          2023年11月11日(土)11:11 {Fore.BLUE}|")
    print(f"{Fore.BLUE}|{Fore.RESET} ---------------------------------------------------------- {Fore.BLUE}|")#58-
    sum = 0 #總價錢
    genreProductCount = [] #各種類商品的陣列，每格數字代表該種類商品的種類數 ex genreProductCount[0] = 漢堡種類的數量
    temp = 0
    for obj in list:
        genreProductCount.append(0) #新增一個種類
        for i in obj:
            genreProductCount[temp] +=1 #每有一個obj，該種類的數量+1 
        temp += 1

    temp = 0
    for obj in list:
        for i in range(genreProductCount[temp]): #走訪每個商品
            if(obj[i].count>0): #如果該商品的個數>0，印出該商品資訊
                print(f"{Fore.BLUE}|{Fore.RESET} ",end='')
                print(obj[i].name, end="") #商品名稱
                for j in range(30-len(obj[i].name)*2): #為了對齊印space
                    print(" ", end="")
                print(obj[i].price, end="") #價錢
                for j in range(6):
                    print(" ",end="")
                print(f"{obj[i].count}個",end="") #購買數量
                for j in range(6):
                    print(" ",end="")
                print(f"{Fore.YELLOW}￥{obj[i].price*obj[i].count}",end="") #單項商品購買總價錢
                sum += obj[i].price*obj[i].count
                printSpace(obj[i].price*obj[i].count)
                print(f"{Fore.BLUE}|")
        temp +=1
                
    for i in range(7): #印發票下半
        print(f"{Fore.BLUE}|",end='')
        for j in range(60):
            print(" ",end='')
        print(f"{Fore.BLUE}|")
    print(f"{Fore.BLUE}|{Fore.RESET} ---------------------------------------------------------- {Fore.BLUE}|")#58-
    print(f"{Fore.BLUE}|{Fore.RESET}                           小計                  {Fore.YELLOW}￥{sum}",end='')
    printSpace(sum)
    print(f"{Fore.BLUE}|")
    
    for i in range(4): #印發票最後部分
        print(f"{Fore.BLUE}|",end='')
        for j in range(60):
            print(" ",end='')
        print(f"{Fore.BLUE}|")   
    print(f"{Fore.BLUE}--------------------------------------------------------------")#62-

"""
list[0] → バーガー(5)
list[1] → サイドメニュー(5)
list[2] → スイーツ(4)
list[3] → マックカフェ(4)
list[4] → ドリンク(5)
"""
list = [[],[],[],[],[]]
list[0].append(Product("てりやきマックバーガー",370,0))
list[0].append(Product("フィレオフィッシュ",370,0))
list[0].append(Product("ビッグマック",450,0))
list[0].append(Product("ベーコンレタスバーガー",380,0))
list[0].append(Product("ダブルチーズバーガー",400,0))

list[1].append(Product("マックフライポテト",380,0))
list[1].append(Product("サイドサラダ",300,0))
list[1].append(Product("えだまめコーン",250,0))
list[1].append(Product("ヨーグルト",200,0))
list[1].append(Product("シャカシャカポテト三種のチーズ味",420,0))
                          
list[2].append(Product("三角チョコパイいちごカスタード",180,0))
list[2].append(Product("三角チョコパイ黒",160,0))
list[2].append(Product("マックシェイクバニラ",220,0))
list[2].append(Product("マックフルーリーオレオクッキー",260,0))

list[3].append(Product("オレオクッキーチョコフラッペ",470,0))
list[3].append(Product("マンゴースムージー",450,0))
list[3].append(Product("ホワイトチョコストロベリーフラッペ",490,0))
list[3].append(Product("マカロンチョコレート",190,0))

list[4].append(Product("コカコーラゼロ",270,0))
list[4].append(Product("スプライト",270,0))
list[4].append(Product("ファンタグレープ",270,0))
list[4].append(Product("ファンタメロン",270,0))
list[4].append(Product("爽健美茶",270,0))


#main
while(gameover==False):
    firstChoice = homepage()
    while(returnHomepage!=True):
        printMenu(firstChoice)
printReceipt(list)
       