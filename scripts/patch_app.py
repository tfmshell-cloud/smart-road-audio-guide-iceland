# -*- coding: utf-8 -*-
import json
import re

with open("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Enrich Gullfoss and key POIs in the POIS array with full facts and 75-second audioScript
poi_enrichments = {
    "gullfoss": {
        "badge": "Golden Waterfall • 32m Canyon",
        "geology": {
            "uk": "Двоступеневий каскад (верхній уступ 11 м, нижній 21 м, загальна висота 32 м), що обривається під прямим кутом у 70-метровий каньйон річки Гвіта. Живиться таненням льодовика Ланґййокюдль. Середня витрата води влітку — 140 м³/с, під час історичних паводків досягала 2000 м³/с. Каньйон висічений крізь плейстоценові базальтові лави та осадові міжльодовикові породи.",
            "en": "Two-tiered cascade (11m and 21m drops, total 32m height) plunging at right angles into a 70m deep gorge on the Hvítá glacial river, fed by Langjökull. Average summer discharge is 140 m³/s, reaching 2,000 m³/s during floods. Carved through Pleistocene flood basalts."
        },
        "saga": {
            "uk": "Пов'язаний із подвигом Сігрідур Томасдоттір (1871–1957) з садиби Браттагольт — першої екологічної захисниці Ісландії. На початку XX ст. іноземні інвестори намагалися збудувати тут ГЕС. Сігрідур пішки ходила до Рейк'явіка за 120 км і погрожувала кинутися у водоспад. Її інтереси захищав юрист Свейнн Бйорнссон (перший президент Ісландії 1944 р.), що дозволило врятувати Ґулльфосс.",
            "en": "Inextricably tied to Sigríður Tómasdóttir of Brattholt farm, Iceland's first environmental protector. In the early 1900s, foreign syndicates attempted to build a hydroelectric dam. Sigríður walked 120 km barefoot to Reykjavík and threatened to drown herself in the falls. Lawyer Sveinn Björnsson (later Iceland's 1st President) defended her."
        },
        "facts": {
            "uk": [
                "💧 Свою назву «Золотий водоспад» отримав через золотаво-коричневий відтінок води на сонці, зумовлений льодовиковим мулом із Ланґййокюдля.",
                "🛡️ Боротьба Сігрідур Томасдоттір за збереження Ґулльфосса створила перше в історії Ісландії природоохоронне прецедентне право.",
                "🌈 Завдяки гігантській хмарі водяного пилу, у сонячні дні над Ґулльфоссом майже завжди розгортається яскрава подвійна кругова веселка.",
                "⚡ У 1920-х роках тут планували збудувати ГЕС потужністю 100 МВт, яка назавжди знищила б водоспад і каньйон."
            ],
            "en": [
                "💧 Named 'Golden Falls' because glacial sediment from Langjökull gives the churning water a rich golden-amber hue in the sunlight.",
                "🛡️ Sigríður Tómasdóttir's crusade to save Gullfoss established Iceland's foundational environmental conservation case law.",
                "🌈 Dense airborne mist creates vivid, permanent double circular rainbows across the gorge on sunny days.",
                "⚡ British investors attempted to build a 100 MW hydroelectric dam in the 1920s that would have permanently flooded the falls."
            ]
        },
        "practical": {
            "uk": "Верхній та нижній оглядові майданчики з'єднані сходами та доріжками. Паркінг біля візитор-центру платний (Parka.is). ОБОВ'ЯЗКОВО вдягати мембранну непромокальну куртку: водяний пил просочує одяг за 3 хвилини. Взимку нижня стежка до краю уступу закривається SafeTravel через намерзання небезпечного льоду.",
            "en": "Upper and lower observation platforms linked by wooden stairs. Paid parking via Parka.is. Waterproof storm shell mandatory due to dense spray. The lower trail to the rock outcrop closes in winter due to hazardous glaze ice."
        },
        "audioScript": {
            "uk": "Ви наближаєтеся до Ґулльфосса — культового «Золотого водоспаду», що дав назву всьому маршруту Золотого кільця! Потужні льодовикові води річки Гвіта, що живляться таненням льодовика Ланґййокюдль, тут вириваються з вузького каньйону і двома ступенями падають у сімдесятиметрову прірву. У сонячні дні над водоспадом розгортається яскрава веселка, а у повітрі висить постійна водяна хмара. Цей водоспад зберігся завдяки мужності однієї жінки — Сігрідур Томасдоттір, яка відстояла природу Ісландії проти промислової забудови. Відчуйте невимовну силу та гуркіт стихії, що формувала ці базальтові скелі протягом тисячоліть!",
            "en": "You are approaching Gullfoss, the iconic Golden Falls giving the Golden Circle its legendary name! Here, the roaring glacial river Hvítá, fed by the massive Langjökull ice cap, plunges thirty-two meters over two dramatic basalt steps into a rugged canyon. On sunny days, brilliant rainbows span the mist, illuminating the golden-hued glacial sediment. Gullfoss stands preserved today thanks to Sigríður Tómasdóttir, who fought tirelessly in the early 1900s to stop a hydroelectric dam project. Feel the thunderous vibrations of nature's raw power as thousands of tons of glacial meltwater carve through the ancient volcanic bedrock!"
        }
    },
    "thingvellir": {
        "facts": {
            "uk": [
                "🏛️ Альтинг, заснований у Тінгведлірі в 930 році н.е., є найстарішим безперервно діючим парламентом світу.",
                "🌍 Це єдине місце на планеті, де розходження Північноамериканської та Євразійської тектонічних плит (2 см/рік) можна побачити неозброєним оком на суходолі.",
                "✝️ У 1000 році саме на скелі Льоґберґ законоговоритель Торгейр проголосив християнство офіційною релігією Ісландії.",
                "🤿 У тріщині Сільфра (Silfra) вода настільки чиста завдяки фільтрації крізь лаву протягом 100 років, що видимість під водою перевищує 100 метрів!"
            ],
            "en": [
                "🏛️ Alþingi, established at Þingvellir in 930 AD, is recognized as the world's oldest parliamentary assembly.",
                "🌍 The only terrestrial site on Earth where the divergent boundary between the North American and Eurasian plates is visible on dry land (drifting 2 cm/year).",
                "✝️ In 1000 AD, lawspeaker Þorgeir declared Christianity the state religion at the Law Rock (Lögberg).",
                "🤿 In the Silfra fissure, water filtered through lava fields for a century yields underwater visibility exceeding 100 meters!"
            ]
        },
        "audioScript": {
            "uk": "Ласкаво просимо до Національного парку Тінгведлір — колиски ісландської нації та об'єкта Всесвітньої спадщини ЮНЕСКО! Ви стоїте на межі двох континентів: прямо під вашими ногами розходиться Серединно-Атлантичний хребет. Стіна узвозу Альманнаґ'я — це край Північноамериканської тектонічної плити, а на протилежному боці долини лежить Євразія. Саме тут у дев'ятсот тридцятому році вікінги заснували найстаріший парламент світу — Альтинг. Тут ухвалювали закони, вирішували долі королівств та хрестили народ Ісландії. Відчуйте сакральну енергію цього місця, де тектоніка планети поєдналася з величною історією вікінгів!",
            "en": "Welcome to Þingvellir National Park, the cradle of Icelandic nationhood and a UNESCO World Heritage site! You stand at the boundary of two continents: directly beneath your feet diverges the Mid-Atlantic Ridge. The cliff wall of Almannagjá marks the edge of the North American tectonic plate, looking across to Eurasia. Here in 930 AD, Norse chieftains founded the Alþingi, the world's oldest surviving parliament. Step between the tectonic scarps, breathe in the pristine sub-arctic air, and touch the sacred soil where planetary geology and human history merge!"
        }
    },
    "geysir": {
        "facts": {
            "uk": [
                "💨 Саме ісландський Великий Ґейзір (Geysir) дав назву всім гейзерам на планеті Земля (від дієслова geysa — «вириватися, бурхливо вивергатися»).",
                "⏱️ Сусідній гейзер Строккюр (Strokkur) є найнадійнішим у світі: він вистрілює стовп окропу на 20–30 метрів кожні 6–10 хвилин.",
                "🌡️ Температура води в підземному резервуарі гейзера на глибині 20 метрів сягає 125°C і не закипає лише через колосальний гідростатичний тиск.",
                "🔵 За кілька секунд до виверження над жерлом Строккюра утворюється дивовижний бірюзовий водяний купол із натягнутої плівки води."
            ],
            "en": [
                "💨 The Great Geysir at Haukadalur lent its name to all geysers on Earth, derived from the Old Norse verb geysa ('to gush/erupt').",
                "⏱️ Neighboring Strokkur is the world's most reliable geyser, erupting a boiling plume 20–30 meters high every 6–10 minutes.",
                "🌡️ Water in the underground conduit reaches 125°C at 20 meters depth, prevented from boiling by immense hydrostatic pressure.",
                "🔵 Seconds before erupting, surface tension inflates a mesmerizing turquoise water bubble over the vent."
            ]
        },
        "audioScript": {
            "uk": "Перед вами долина Хейкадалур — легендарне геотермальне поле, де земне ядро промовляє до нас мовою пари та киплячої води! Саме тут розташований Великий Ґейзір, який дав своє ім'я всім гейзерам нашої планети. Хоча сам Ґейзір зараз спить, його молодший брат Строккюр демонструє бездоганну точність: кожні шість-вісім хвилин вода в його жерлі закипає, надувається величезним блакитним куполом і з оглушливим ревом вистрілює стовп окропу на висоту до тридцяти метрів! Тримайтеся з навітряного боку, щоб не потрапити під хмару сірчаної пари, і приготуйте камери: секунда появи водяного купола — це один із найзахоплюючих кадрів у житті!",
            "en": "Welcome to Haukadalur, the legendary geothermal sanctuary where the Earth's fiery mantle speaks through plumes of boiling steam! This valley gave birth to the Great Geysir, the namesake of every erupting thermal spring on the globe. While the Great Geysir slumbers, neighboring Strokkur exhibits clockwork precision: every six to ten minutes, a luminous turquoise water dome inflates over the vent before exploding skyward thirty meters into the crisp sub-arctic air. Stand upwind to stay clear of boiling sulfur mist, watch the boiling vents breathe, and witness the untamed geothermal heartbeat of Iceland!"
        }
    },
    "reynisfjara": {
        "facts": {
            "uk": [
                "⚠️ Рейнісф'яра — найнебезпечніший пляж Ісландії через так звані «хвилі-підкрадачі» (sneaker waves), які раптово накочуються на десятки метрів далі лінії прибою.",
                "🏛️ Скеля Ґардар на пляжі утворена ідеальними шестикутними базальтовими колонами, що охолоджувалися повільно всередині лавового потоку.",
                "🧌 За легендою, скелі Рейнісдранґар у морі — це тролі, які намагалися витягти трищогловий корабель і закам'яніли з першими променями сонця.",
                "🎬 Пляж з'являвся у безлічі фільмів: «Зоряні війни: Бунтар Один» (планета Ламу), «Гра престолів» (Східний Дозор біля моря) та кліпах Bon Iver."
            ],
            "en": [
                "⚠️ Reynisfjara is Iceland's most hazardous shore due to sneaker waves that surge unpredictably far up the dark sands with devastating force.",
                "🏛️ The cliff Garðar features pristine hexagonal columnar basalt joints formed by the gradual, symmetric contraction of cooling lava.",
                "🧌 Folklore proclaims the Reynisdrangar sea stacks are petrified trolls caught dragging a ship ashore when daylight struck.",
                "🎬 Filming location for Star Wars: Rogue One (Planet Lah'mu), Game of Thrones (Eastwatch-by-the-Sea), and numerous international music videos."
            ]
        },
        "audioScript": {
            "uk": "Вітаємо на Рейнісф'ярі — одному з найкрасивіших, найзагадковіших і водночас найнебезпечніших пляжів нашої планети! Подивіться на ідеальні шестикутні базальтові колони скелі Ґардар: вони виглядають наче гігантський орган, витесаний невідомим майстром, але це творіння самої природи при охолодженні лави. А у морі височіють гострі шпилі Рейнісдранґар — за давньою легендою, це тролі, які закам'яніли на світанку. Але головне правило Рейнісф'яри — це гранична повага до океану. Тут народжуються підступні хвилі-вбивці, які накочуються значно далі звичайних і миттєво збивають людину з ніг. Запам'ятайте головне правило безпеки: ніколи не повертайтеся спиною до хвиль, не підходьте близько до кромки води і тримайтеся безпечної зони!",
            "en": "Welcome to Reynisfjara, widely celebrated as one of the most stunning, cinematic, and treacherous beaches on Earth! Gaze upon the breathtaking basalt cliffs of Garðar: the perfectly carved hexagonal columns resemble an immense stone pipe organ sculpted by Titans, formed by the slow geometric cooling of ancient lava flows. Out in the churning ocean, the sea stacks of Reynisdrangar jut skyward—legend tells they are petrified trolls caught by the morning sun. Yet the sublime grandeur of Reynisfjara demands utmost vigilance. Obey the automated safety warning lights, stay well back from the breakers, and never turn your back on the Atlantic Ocean!"
        }
    }
}

# Find POIS array in html and patch entries
pois_match = re.search(r'const POIS = (\[.*?\]);', html, re.DOTALL)
if pois_match:
    pois_list = json.loads(pois_match.group(1))
    for p in pois_list:
        pid = p["id"]
        # Apply specific enrichment if available
        if pid in poi_enrichments:
            for k, v in poi_enrichments[pid].items():
                p[k] = v
        # Ensure every single POI has a 'facts' and 'audioScript' field if missing
        if "facts" not in p:
            uk_fact = f"📍 {p['name']['uk']} є офіційною ключовою локацією експедиційного маршруту ({p.get('badge', 'Must-See')}). {p['geology']['uk'][:120]}..."
            en_fact = f"📍 {p['name']['en']} is an essential expedition waypoint ({p.get('badge', 'Must-See')}). {p['geology']['en'][:120]}..."
            p["facts"] = {"uk": [uk_fact], "en": [en_fact]}
        if "audioScript" not in p:
            p["audioScript"] = {
                "uk": f"Вітаємо на локації {p['name']['uk']}! {p['vector']['uk']}. Геологічна структура: {p['geology']['uk']}. Історичне значення та фольклор: {p['saga']['uk']}. Важлива порада для водія та правила безпеки: {p['practical']['uk']}. Насолоджуйтеся дослідженням цього унікального куточка природи Ісландії!",
                "en": f"Welcome to {p['name']['en']}! Location vector: {p['vector']['en']}. Geological overview: {p['geology']['en']}. Historical chronicles and sagas: {p['saga']['en']}. Crucial driving safety and logistics: {p['practical']['en']}. Enjoy your visit to this remarkable Icelandic expedition landmark!"
            }
    
    new_pois_json = json.dumps(pois_list, ensure_ascii=False)
    html = html[:pois_match.start()] + f"const POIS = {new_pois_json};" + html[pois_match.end():]
    print(f"Patched {len(pois_list)} POIs with facts and audioScripts.")

# 2. Add 'Цікаві факти' button to header navigation
facts_btn_desktop = '''
      <button onclick="openFactsModal()" class="px-3 py-1.5 rounded-lg bg-gradient-to-r from-amber-500/20 to-orange-500/20 hover:from-amber-500/30 hover:to-orange-500/30 text-amber-300 border border-amber-500/40 font-semibold flex items-center gap-1.5 shadow-md shadow-amber-500/10 transition">
        <span>💡</span> <span>Цікаві факти про Ісландію</span>
        <span class="text-[9px] px-1 py-0.2 rounded bg-amber-500/30 font-mono text-amber-200">ТОП</span>
      </button>
'''
if 'openFactsModal()' not in html:
    # Insert before openCopilotModal button in header nav
    target_nav = '<button onclick="openCopilotModal()"'
    html = html.replace(target_nav, facts_btn_desktop + '\n      ' + target_nav, 1)
    print("Added Facts button to header navigation.")

# 3. Add 'Цікаві факти' button to mobile subheader / tools bar
mobile_facts_btn = '''
        <button onclick="openFactsModal()" class="px-2.5 py-1 rounded-lg bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/30 text-[11px] font-semibold flex items-center gap-1 shrink-0">
          <span>💡</span> <span>Цікаві факти</span>
        </button>
'''
if 'mobile-facts-btn' not in html:
    target_mobile = '<div class="flex items-center space-x-1.5 overflow-x-auto'
    # We can inject right after opening of category / quick filter bar
    html = html.replace('<div class="flex items-center space-x-2 shrink-0">', '<div class="flex items-center space-x-2 shrink-0">\n' + mobile_facts_btn, 1)

with open("/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Saved updated index.html with POI enrichments and buttons.")
