from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import DirectButton, DirectLabel
from panda3d.core import AmbientLight, DirectionalLight, Vec4, Vec3, TextNode, loadPrcFileData
import math

loadPrcFileData("", "window-title Stickman World\nwin-size 960 540\nload-display pandagles2\naux-display pandagles\naudio-library-name null\nshow-frame-rate-meter 0")

class Game(ShowBase):
    def __init__(self):
        super().__init__()
        self.disableMouse()
        self.setBackgroundColor(0.55, 0.72, 0.84, 1)
        self.player = self.render.attachNewNode("player")
        self.keys = {k: False for k in ("f","b","l","r")}
        self.phase = 0.0
        self.inside = False
        self.make_lights()
        self.make_world()
        self.make_player()
        self.make_ui()
        self.taskMgr.add(self.update, "update")
        for key, action in [("w","f"),("arrow_up","f"),("s","b"),("arrow_down","b"),
                             ("a","l"),("arrow_left","l"),("d","r"),("arrow_right","r")]:
            self.accept(key, self.set_key, [action, True])
            self.accept(key+"-up", self.set_key, [action, False])
        self.accept("escape", self.userExit)

    def make_lights(self):
        a=AmbientLight("ambient"); a.setColor(Vec4(.65,.68,.72,1))
        self.render.setLight(self.render.attachNewNode(a))
        d=DirectionalLight("sun"); d.setColor(Vec4(1,.94,.83,1))
        n=self.render.attachNewNode(d); n.setHpr(-35,-55,0); self.render.setLight(n)

    def box(self, name, pos, scale, color, parent=None):
        n=self.loader.loadModel("models/box"); n.reparentTo(parent or self.render)
        n.setName(name); n.setPos(*pos); n.setScale(*scale); n.setColor(*color)
        return n

    def sign(self, text, pos):
        t=TextNode(text); t.setText(text.upper()); t.setAlign(TextNode.ACenter)
        t.setTextColor(.12,.12,.12,1)
        n=self.render.attachNewNode(t); n.setPos(*pos); n.setScale(.42)

    def building(self, name, x, y, w, h, d, color):
        self.box(name,(x,y,h/2),(w/2,d/2,h/2),color)
        self.box(name+" door",(x,y+d/2+.03,1),(.55,.07,1),(.25,.16,.11,1))
        self.box(name+" entry",(x,y+d/2+1.2,.04),(1.1,1.1,.05),(.94,.78,.25,1))
        self.sign(name,(x,y+d/2+.22,h+.5))
        if name=="Cami":
            dome=self.loader.loadModel("models/misc/sphere"); dome.reparentTo(self.render)
            dome.setPos(x,y,h+.7); dome.setScale(1.5,1.5,.85); dome.setColor(.24,.48,.43,1)
            self.box("minaret",(x-2,y,h+1.4),(.22,.22,1.7),(.82,.77,.63,1))

    def make_world(self):
        self.box("grass",(0,0,-.35),(60,60,.3),(.36,.53,.34,1))
        self.box("road",(0,0,-.12),(2.5,60,.12),(.2,.21,.23,1))
        for y in range(-55,60,9): self.box("road marking",(0,y,.02),(.06,2,.02),(.95,.85,.62,1))
        self.building("Cami",-9,-5,6,5,5,(.85,.81,.69,1))
        self.building("Hayalhanem",10,-5,7,4,5,(.77,.70,.59,1))
        self.building("Ev",-11,12,5,3.5,4.5,(.77,.58,.47,1))
        self.building("Kafe",11,12,5.5,3.8,4.5,(.56,.70,.75,1))
        self.building("Dükkan",0,-23,6,3.5,4,(.73,.71,.55,1))
        for x,y in [(-18,3),(18,3),(-18,20),(18,20),(-18,-18),(18,-18)]:
            self.box("tree trunk",(x,y,.8),(.18,.18,.8),(.36,.23,.13,1))
            s=self.loader.loadModel("models/misc/sphere"); s.reparentTo(self.render)
            s.setPos(x,y,2); s.setScale(1); s.setColor(.22,.43,.25,1)

    def make_player(self):
        self.torso=self.box("body",(0,0,1.15),(.34,.22,.48),(.20,.42,.72,1),self.player)
        head=self.loader.loadModel("models/misc/sphere"); head.reparentTo(self.player)
        head.setPos(0,0,1.92); head.setScale(.29,.27,.31); head.setColor(.88,.69,.54,1)
        self.limbs=[]
        for x in (-.36,.36):
            a=self.box("arm",(x,0,1.18),(.11,.12,.39),(.88,.69,.54,1),self.player); self.limbs.append(a)
        for x in (-.14,.14):
            a=self.box("leg",(x,0,.48),(.14,.15,.48),(.16,.18,.22,1),self.player); self.limbs.append(a)

    def make_ui(self):
        DirectLabel(text="STICKMAN WORLD",scale=.055,pos=(0,0,.91),
                    text_fg=(1,1,1,1),frameColor=(.08,.12,.16,.65))
        self.status=DirectLabel(text="Şehrini keşfet!",scale=.043,pos=(0,0,.80),
                    text_fg=(1,1,1,1),frameColor=(.08,.12,.16,.5))
        DirectLabel(text="WASD / ok tuşları: hareket",scale=.032,pos=(0,0,-.93),
                    text_fg=(1,1,1,1),frameColor=(.08,.12,.16,.5))
        for text,xy,key in [("▲",(-1.05,-.58),"f"),("▼",(-1.05,-.82),"b"),
                            ("◀",(-1.27,-.70),"l"),("▶",(-.83,-.70),"r")]:
            DirectButton(text=text,scale=.065,pos=(xy[0],0,xy[1]),
                         command=self.set_key,extraArgs=[key,True])
        DirectButton(text="Yaklaş / Gir",scale=.05,pos=(1,0,-.68),command=self.enter)
        DirectButton(text="Dışarı çık",scale=.05,pos=(1,0,-.84),command=self.leave)

    def set_key(self,k,v): self.keys[k]=v

    def enter(self):
        if self.inside: return
        places=[("Cami",(-9,-5)),("Hayalhanem",(10,-5)),("Ev",(-11,12)),("Kafe",(11,12)),("Dükkan",(0,-23))]
        p=self.player.getPos()
        name,xy=min(places,key=lambda a:(p.x-a[1][0])**2+(p.y-a[1][1])**2)
        if (p.x-xy[0])**2+(p.y-xy[1])**2 < 30:
            self.inside=True; self.status["text"]=name+" içindesin (örnek iç mekân)"
            self.player.setPos(0,0,0)
            self.box("interior floor",(0,0,-.1),(7,7,.1),(.70,.65,.55,1))
        else: self.status["text"]="Bir binanın giriş karesine yaklaş."

    def leave(self):
        if self.inside:
            self.inside=False; self.player.setPos(0,5,0); self.status["text"]="Şehrini keşfet!"

    def update(self,task):
        dt=min(globalClock.getDt(),.05)
        v=Vec3(float(self.keys["r"])-float(self.keys["l"]),
               float(self.keys["f"])-float(self.keys["b"]),0)
        if v.lengthSquared()>0:
            v.normalize(); self.player.setPos(self.player,self.player.getQuat(self.render).xform(v)*4*dt)
            self.phase+=dt*9; self.player.setH(math.degrees(math.atan2(v.x,v.y)))
            self.limbs[0].setR(math.sin(self.phase)*18); self.limbs[1].setR(-math.sin(self.phase)*18)
            self.limbs[2].setR(-math.sin(self.phase)*22); self.limbs[3].setR(math.sin(self.phase)*22)
        target=self.player.getPos()+Vec3(0,-7,4.2)
        self.camera.setPos(self.camera.getPos()+(target-self.camera.getPos())*min(1,dt*4))
        self.camera.lookAt(self.player.getPos()+Vec3(0,0,1))
        return task.cont

Game().run()
