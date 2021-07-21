from . import OtakuDesu
import itertools
from time import sleep
from subprocess import call
from threading import Thread
from random import choice

otak = OtakuDesu()

class Base:

    def __init__(self):
        self.contact = "https://wa.me/6285892766102"
        self.clear = (lambda : call(["clear"]))

    def randco(self, text):
        lcol = ["\x1b[1;31m","\x1b[1;32m","\x1b[1;33m","\x1b[1;34m","\x1b[1;35m","\x1b[1;36m"]
        return "%s%s\x1b[0m" % (choice(lcol), text)

    def chotto(self):
        global matte
        matte = []
        for c in itertools.cycle(["■□□□□□□□□□","■■□□□□□□□□", "■■■□□□□□□□", "■■■■□□□□□□", "■■■■■□□□□□", "■■■■■■□□□□", "■■■■■■■□□□", "■■■■■■■■□□", "■■■■■■■■■□", "■■■■■■■■■■"]):
            if bool(matte) is True:
                break
            print(f"  ╳ Wait {self.randco(c)}\r", end="")
            sleep(0.1)

    def show(self, obj):
        # self.clear()
        print(f"""
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ➯ Title : {obj.title}
  ➯ Japanese Title : {obj.jp_title}
  ➯ Score : {obj.rating}
  ➯ Producers : {obj.producers}
  ➯ Studio : {obj.studio}
  ➯ Type : {obj.type}
  ➯ Status : {obj.status}
  ➯ Episodes : {obj.episodes}
  ➯ Duration : {obj.duration}
  ➯ Release Date : {obj.release_date}
  ➯ Genre : {', '.join(obj.genres)}
  ➯ Synopsis : {obj.synopsis}
  """)

    def showeps(self, obj):
        eps = list(obj.downloads.__dict__.keys())[::-1]
        for k, v in enumerate(eps, 1):
            print("  %s. %s" % (k, v.replace("eps","Episode ").replace("batch", "Batch")))
        chos = int(input("\n  ➯ Choose : "))
        if chos > 0 and chos-1 < len(eps):
            self.showdl(obj.downloads.__dict__.get(eps[chos-1]))
        else:
            print("  ╳ Invalid Input")

    def showdl(self, obj):
        qlt = list(obj.__dict__.keys())[::-1]
        print("\n")
        for k, v in enumerate(qlt, 1):
            print("  %s.%s" % (k, v.replace('_',' ')))
        chos = int(input("\n  ➯ Choose : "))
        if chos > 0 and chos-1 < len(qlt):
            self.showlink(obj.__dict__.get(qlt[chos-1]))
        else:
            print("  ╳ Invalid Input")

    def showlink(self, obj):
        deel = list(obj.__dict__.keys())
        print("\n")
        for k, v in enumerate(deel, 1):
            print("  %s. %s" % (k, v))
        chos = int(input("\n  ➯ Choose : "))
        if chos > 0 and chos-1 < len(deel):
            call(["termux-clipboard-set", obj.__dict__.get(deel[chos-1])])
            print("  ✓ Link Copied To Clipboard")
            exit(0)
        else:
            print("  ╳ Invalid Input")

class Main(Base):
    loads = (lambda x: Thread(target=Base().chotto).start())
    logo = """
   _ \   |           |                |
  |   |  __|   _` |  |  /  |   |   _` |   _ \   __|  |   |
  |   |  |    (   |    <   |   |  (   |   __/ \__ \  |   |
 \___/  \__| \__,_| _|\_\ \__,_| \__,_| \___| ____/ \__,_| .moe
  ⚘ MhankBarBar | © 2021
  ⚘ Search And Get Direct Download Link From Otakudesu.moe

  1. Search
  2. From Url
  3. From Schedule
  4. Contact
  """
    def __main__(self):
        self.clear()
        print(self.logo)
        try:
            if (mek := int(input("  ➯ Choose : "))):
                if mek == 1:
                    quer = input("  ➯ Query : ")
                    print("\n")
                    self.loads()
                    if(hasil := otak.search(quer).result):
                        matte.insert(0, True)
                        sus = []
                        for k, v in enumerate(hasil, 1):
                            print("  %s. %s" % (k, v.title))
                            sus.append(v)
                        print("  99. Back to main menu")
                        while(True):
                            if (pil := int(input("\n  ➯ Choose : "))):
                                if pil == 99:self.__main__()
                                if pil > 0 and pil-1 < len(sus):
                                    self.show(sus[pil-1])
                                    self.showeps(sus[pil-1])
                                else:
                                    print("  ╳ Invalid Input")
                            else:
                                print("  ╳ Invalid Input")
                    else:
                        matte.insert(0, True)
                        sleep(0.5)
                        print("  ╳ Anime not found")
                elif mek == 2:
                    url = input("  ➯ Url : ")
                    print("\n")
                    self.loads()
                    if (hasil := otak.byUrl(url)):
                        matte.insert(0, True)
                        # self.clear()
                        self.show(hasil)
                        self.showeps(hasil)
                    else:
                        matte.insert(0, True)
                        print("  ╳ Invalid Input")
                elif mek == 3:
                    exit("  I will added this on next version")
                    #print("\n")
                    #self.loads()
                    #if (hasil := otak.getSchedule)
                elif mek == 4:
                    call(["xdg-open", self.contact])
                    self.__main__()
                else:
                    pass
            else:
                print("  ╳ Invalid Input")
        except Exception as e:
            # print(e)
            exit("  ╳ An error occurred")

if __name__ == "__main__":
    Main().__main__()
