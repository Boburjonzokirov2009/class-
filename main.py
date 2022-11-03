from flask import Flask,render_template
from postt import posts

pos=[
    {
        "id":"1",
        "title":"Adliya vazirligida",
        "subtitle":"jismoniy va yuridik shaxslarning vakillarini qabul qilish: jarayonlar va tartiblar",
        "body":"Adliya vazirligining “Ishonch telefoni”ga 2022-yil 9-oyligi davomida jami 54 541 ga yaqin jismoniy va yuridik shaxslar tomonidan qoʻngʻiroqlar qilingan boʻlib, shundan 48 914 ta murojaatlarga malakali mutaxassislar tomonidan tegishli huquqiy maslahatlar berildi, 5 627 ta murojaatlar oʻrganish talab qilganligi sababli ijroga qaratildi."
    },
    {
        "id":"2",
        "title":"Jizzax viloyatida",
        "subtitle":"ikki nafar notariusning litsenziyalari vaqtincha to'xtatildi",
        "body":'''O'zbekiston Respublikasi “Notariat to'g'risida”gi Qonunining 15-2 -moddasiga muvofiq Jizzax viloyat adliya boshqarmasi boshlig‘ining 2022-yil 13-sentabrdagi 181-um-son buyrug‘iga asosan,Zomin tumanida xususiy amaliyot bilan shug‘ullanuvchi notarius Sh.Amanlikovga berilgan xususiy notarial faoliyat bilan shug‘ullanish huquqini beruvchi litsenziyaning amal qilishi 1 oy muddatga (3-oktabrdan 3-noyabrgacha),Zarbdor tumanida xususiy amaliyot bilan shug‘ullanuvchi notarius I.Artikmurodovaga berilgan xususiy notarial faoliyat bilan shug‘ullanish huquqini beruvchi litsenziyaning amal qilishi 1 oy muddatga (3-oktabrdan 3-noyabrgacha) to‘xtatildi.''',
    },
    {
        "id":"3",
        "title":"Тошкентда",
        "subtitle":" 26 ёшли ҳайдовчи қасддан ўлдирилди. Жиноий гуруҳда мактаб ўқувчиси ҳам бор",
        "body":"Сирдарё — Тошкент йўналишида йўловчи ташиш фаолияти билан шуғулланувчи фуқаро А.Эрназаров (1996 й.т)ни уларни Бўстонлиқ тумани ҳудудига олиб бориб келишга кўндиришган. Сўнг унинг бошқарувидаги “Lasetti” русумли автомашинасига ўтиришган. Автомашинада почта сифатида олинган 14 млн. сўм пул маблағи борлигини билишгач эса А.Эрназаровни алдов йўли билан Қуйичирчиқ тумани, Толовул маҳалласи ҳудудига олиб боришиб, пул маблағларини босқинчилик йўли билан қўлга киритиб, уни бўйин қисмидан бўғиб, қасддан ўлдиришган."
    }
]

post_objes=[]

for i in pos:
    pos_obj=posts(i["id"], i["title"], i["subtitle"], i["body"])
    post_objes.append(pos_obj)


app=Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html",lis=post_objes)


@app.route("/pos<int:index>")
def m(index):
    return render_template("manba.html",id=index,lis=post_objes)

if __name__=="__main__":
    app.run(debug=True)