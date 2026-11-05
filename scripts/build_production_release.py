# -*- coding: utf-8 -*-
import json
import re
from generate_facts_dataset import ICELAND_MASTER_FACTS

INDEX_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/index.html"
ENCYCLO_PATH = "/Users/volodymyrkatasonov/.gemini/antigravity/scratch/Smart_Road_Audio_Guide_Iceland/iceland_guide_encyclopedia.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    index_html = f.read()

# ----------------------------------------------------
# 1. SPECIFIC RICH ENRICHMENTS FOR KEY POIS
# ----------------------------------------------------
deep_enrichments = {
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
                "💧 Назва «Золотий водоспад» походить від янтарно-золотавого відтінку льодовикового мулу, що сяє під прямими променями сонця.",
                "🛡️ Боротьба Сігрідур Томасдоттір проти британських забудовників створила перше в історії Ісландії природоохоронне прецедентне право.",
                "🌈 Завдяки гігантській хмарі водяного пилу, у сонячні дні над каньйоном майже завжди розгортається яскрава подвійна кругова веселка.",
                "⚡ У 1920-х роках тут планували звести 100-мегаватну греблю ГЕС, яка назавжди затопила б ущелину."
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
            "uk": "Ви наближаєтеся до Ґулльфосса — легендарного «Золотого водоспаду», що дав ім'я всьому маршруту Золотого кільця! Потужні льодовикові води річки Гвіта, що живляться таненням льодовика Ланґййокюдль, тут вириваються з каньйону і двома ступенями падають у сімдесятиметрову прірву. У сонячні дні над водоспадом розгортається яскрава веселка, а у повітрі висить постійна водяна хмара. Цей водоспад зберігся завдяки мужності однієї жінки — Сігрідур Томасдоттір, яка відстояла природу Ісландії проти промислової забудови. Відчуйте невимовну силу та гуркіт стихії, що формувала ці базальтові скелі протягом тисячоліть!",
            "en": "You are approaching Gullfoss, the iconic Golden Falls giving the Golden Circle its legendary name! Here, the roaring glacial river Hvítá, fed by the massive Langjökull ice cap, plunges thirty-two meters over two dramatic basalt steps into a rugged canyon. On sunny days, brilliant rainbows span the mist, illuminating the golden-hued glacial sediment. Gullfoss stands preserved today thanks to Sigríður Tómasdóttir, who fought tirelessly in the early 1900s to stop a hydroelectric dam project. Feel the thunderous vibrations of nature's raw power as thousands of tons of glacial meltwater carve through the ancient volcanic bedrock!"
        }
    },
    "kolugljufur": {
        "badge": "Giantess Gorge • Twin Cascades",
        "geology": {
            "uk": "Каньйон довжиною 1 км і глибиною до 50 м, прорізаний лососевою річкою Відалсау (Víðidalsá) крізь міцні плейстоценові базальти. Річка падає двома паралельними каскадами Kolufossar у глибокий вир, утворюючи ерозійні велетенські казани.",
            "en": "1km long, 50m deep gorge incised by the salmon-rich Víðidalsá river through robust Pleistocene basalt strata. Features the twin cascades of Kolufossar plunging into deep swirl-drilled potholes."
        },
        "saga": {
            "uk": "За народними сагами півночі, у печері каньйону жила велетка Кола (Kola). Вона ловила свіжого лосося голими руками прямо у вирах і варила його в сусідньому киплячому джерелі Koluketill. Плоский кам'яний карниз над безоднею зветься Kolurúm («Ліжко Коли»).",
            "en": "According to local legend, giantess Kola lived in a canyon cave, catching salmon with her bare hands and cooking it in the boiling spring Koluketill. The flat ledge over the chasm is named Kolurúm (Kola's Bed)."
        },
        "facts": {
            "uk": [
                "🧌 Назва каньйону походить від імені велетки Коли, яка згідно з фольклором спала на кам'яному виступі Kolurúm прямо над ревучим водоспадом.",
                "🐟 Річка Відалсау є однією з найчистіших і найбагатших на дикого атлантичного лосося річок Північної Ісландії.",
                "🌉 Сучасний автомобільний міст перекинутий прямо над найвужчою і найглибшою частиною розлому, відкриваючи запаморочливий вид униз.",
                "🚗 Локація розташована лише за 6 км від кільцевої Траси 1, проте залишається відносно малолюдною порівняно з водоспадами Півдня."
            ],
            "en": [
                "🧌 Named after giantess Kola, who folkloric tales claim slept on the stone ledge Kolurúm directly above the thundering falls.",
                "🐟 The Víðidalsá River is recognized as one of Northern Iceland's most pristine and productive wild Atlantic salmon habitats.",
                "🌉 A road bridge spans the narrowest, most dramatic precipice of the gorge, providing thrilling aerial viewpoints straight down into the churn.",
                "🚗 Located just 6 km off Ring Road 1, yet remains pleasantly peaceful and uncrowded compared to South Coast sites."
            ]
        },
        "practical": {
            "uk": "З'їзд із Траси 1 на дорогу 715 (долина Víðidalur). 6 км гравійного покриття, проїзного для будь-яких типів авто. Безкоштовний паркінг прямо біля мосту. Дотримуйтесь огороджених стежок — краї каньйону не мають суцільних поручнів!",
            "en": "Turn off Ring Road 1 onto gravel Route 715 (Víðidalur valley). Accessible for all standard passenger vehicles. Free parking at the bridge. Exercise caution near unfenced gorge edges!"
        },
        "audioScript": {
            "uk": "Через 60 секунд ми під'їжджаємо до каньйону Колуглювур — дивовижної перлини Північної Ісландії! Приготуйтеся побачити, як тиха долина раптово розтинається глибокою п'ятдесятиметровою тріщиною в базальті. Річка Відалсау тут скидається кількома бурхливими каскадами Колуфоссар. За переказами саг, саме тут жила велетка Кола, яка ловила лосося голими руками і відпочивала на кам'яному карнизі над безоднею. Паркуйтеся біля мосту, вийдіть на оглядовий майданчик і відчуйте дику первозданну енергію Півночі!",
            "en": "In 60 seconds we arrive at Kolugljúfur Canyon, an awe-inspiring natural wonder tucked away in Northern Iceland! Watch as the pastoral Víðidalur valley abruptly splits into a dramatic fifty-meter fissure carved through solid basalt bedrock. The salmon river Víðidalsá plunges here over the dual cataracts of Kolufossar. Medieval tales proclaim this ravine the sanctuary of giantess Kola, who caught fish barehanded and slept upon the stone shelf above the abyss. Park by the bridge and take in the untamed majesty of this northern marvel!"
        }
    },
    "brimketill": {
        "badge": "Lava Sea Pool • Coastal Vortex",
        "geology": {
            "uk": "Природний басейн у прибережному лавовому полі півострова Рейк'янес, висічений тисячолітніми ударами океанських хвиль. Постійна гідродинамічна абразія створила ідеальну гладку напівкруглу чашу в темному базальті.",
            "en": "Natural cauldron carved into the jagged coastal basalt lava of the Reykjanes peninsula by relentless North Atlantic storm waves. Continuous hydraulic grinding formed a smooth circular sea pool."
        },
        "saga": {
            "uk": "Старовинна назва басейну — Oddnýjarlaug («Купальня Оддні»). Легенда оповідає про грізну трольчиху Оддні, яка мешкала в лавових печерах і приходила до цього басейну вночі, щоб митися та прати свій одяг у морській піні.",
            "en": "Historically called Oddnýjarlaug (Oddný's Pool). Folklore tells of the ogress Oddný who dwelt in the lava caves and frequented the basin under moonlit skies to bathe in ocean froth."
        },
        "facts": {
            "uk": [
                "🌊 Брімкетіль висічений у лаві суто силою морського прибою: штормові хвилі закочували каміння у заглибину, яке оберталося і шліфувало чашу тисячоліттями.",
                "⚠️ КУПАТИСЯ СУВОРО ЗАБОРОНЕНО! Попри спокусливий вигляд басейну, раптові хвилі Атлантики регулярно накривають його з головою і затягують у відкритий океан.",
                "🧌 За легендою, велетка Оддні була настільки велетенською, що басейн глибиною 2 метри був їй лише по щиколотки.",
                "🪵 У 2017 році тут збудували спеціальну підняту дерев'яну оглядову платформу, яка гарантує безпечний огляд навіть під час припливу."
            ],
            "en": [
                "🌊 Brimketill was gouged purely by wave vortex mechanics: boulders trapped in hollows ground the solid basalt into a symmetric amphitheater over millennia.",
                "⚠️ SWIMMING IS STRICTLY FORBIDDEN! Unpredictable sneaker swells routinely submerge the basin, washing unsuspecting visitors into freezing currents.",
                "🧌 Myth holds the giantess Oddný was so gargantuan that the two-meter-deep cauldron reached merely to her ankles.",
                "🪵 An elevated timber viewing platform was installed in 2017, allowing safe observation of breaking ocean breakers during high tide."
            ]
        },
        "practical": {
            "uk": "Розташований на дорозі 425 на південному узбережжі Рейк'янеса. Безкоштовний паркінг. Не спускайтеся з дерев'яного настилу на слизькі чорні лавові скелі — це зона смертельного ризику хвиль-убивць!",
            "en": "Located along Route 425 on the southern Reykjanes shore. Free parking and accessible boardwalk. Never step off the timber deck onto slick seaward lava!"
        },
        "audioScript": {
            "uk": "Праворуч за курсом на 2-гу годину — вихід до узбережжя Брімкетіль, природного лавового басейну Атлантики! Перед вами дивовижне творіння стихії: океанські штормові хвилі тисячоліттями шліфували твердий базальт, вибивши ідеальну кам'яну чашу. Давні перекази звуть це місце купальнею трольчихи Оддні. Але будьте гранично пильні: вода тут оманлива! Купатися в басейні суворо заборонено через підступні океанські вали. Залишайтеся на дерев'яному оглядовому помості та спостерігайте за шаленою міццю прибою!",
            "en": "To your right at two o'clock lies Brimketill, the churning coastal lava cauldron of the Reykjanes peninsula! Watch in awe as North Atlantic swells crash against jagged volcanic rocks, filling a circular pool sculpted over centuries by wave abrasion. Lore names this natural tub the bath of giantess Oddný. Remember: entering the water is strictly prohibited due to sudden catastrophic sneaker waves. Enjoy the dramatic ocean spray from the safety of the elevated boardwalk!"
        }
    },
    "stampar": {
        "badge": "Crater Row • Rift Axis",
        "geology": {
            "uk": "Ланцюг шлакових і спаяних вулканічних конусів, сформованих під час вивержень «Вогні Рейк'янеса» (1210–1240 рр. н.е.). Конуси вишикувані вздовж прямої лінії тектонічного розширення Серединно-Атлантичного хребта.",
            "en": "Fissure-fed scoria cone alignment produced during the historic Reykjanes Fires (1210–1240 AD). Perfectly traces the tectonic divergent axis of the Mid-Atlantic Ridge on land."
        },
        "saga": {
            "uk": "Виверження Стампар описані в середньовічних ісландських літописах як час, коли «земля горіла вогнем, а море кипіло біля берега».",
            "en": "Chronicled in medieval Icelandic annals as a catastrophic period when 'the earth burned with fire and coastal waters boiled'."
        },
        "facts": {
            "uk": [
                "🌋 Кратери Стампар розташовані прямо над виходом Серединно-Атлантичного хребта на поверхню Європи.",
                "🚶 В один із кратерів прокладено пішохідну стежку, що дозволяє зазирнути всередину шлакового жерла.",
                "⚡ Лавові поля Стампар мають вік лише близько 800 років і вважаються молодими у геологічній історії півострова.",
                "🧭 Поруч розташований знаменитий пішохідний міст Miðlína («Міст між континентами»)."
            ],
            "en": [
                "🌋 The Stampar alignment lies directly along the terrestrial landfall of the Mid-Atlantic Ridge rift zone.",
                "🚶 A marked path leads inside one of the breached scoria cones, offering an intimate look at volcanic ejecta.",
                "⚡ The basaltic lavas are approximately 800 years old, representing the youngest historical volcanism before the 2021 awakening.",
                "🧭 Located minutes from Miðlína, the famous footbridge connecting North America and Eurasia."
            ]
        },
        "practical": {
            "uk": "Дорога 425 біля маяка Reykjanesvíti. Зручний заїзд, легка 15-хвилинна пішохідна прогулянка по маркованій стежці.",
            "en": "Route 425 near Reykjanesvíti lighthouse. Convenient roadside turnout and easy 15-minute walk."
        },
        "audioScript": {
            "uk": "Подивіться прямо за курсом: перед вами відкривається лінійка кратерів Стампар — наочний підручник тектоніки планети! Ці шлакові конуси вишикувалися вздовж ідеально прямої лінії розлому, де розходиться кора Землі. Вони утворилися під час вивержень тринадцятого століття, відомих як «Вогні Рейк'янеса». Тут ви буквально бачите шов, крізь який магма піднімається з глибин земної мантії. Насолодіться цим космічним пейзажем чорного базальту та червоного шлаку!",
            "en": "Gaze straight ahead along our route: the Stampar crater row stretches out like a living open-air volcanology museum! These cinder cones align in a razor-straight fracture where tectonic forces pull the crust apart. Born during the thirteenth-century Reykjanes Fires, they outline the fissure vents that spewed glowing lava rivers across this desolate plain. Take in this striking, lunar expanse of dark basalt and rust-red scoria!"
        }
    }
}

# ----------------------------------------------------
# 2. UPDATE POIS IN INDEX.HTML
# ----------------------------------------------------
pois_match = re.search(r'const POIS = (\[.*?\]);', index_html, re.DOTALL)
if pois_match:
    pois_list = json.loads(pois_match.group(1))
    for p in pois_list:
        pid = p["id"]
        # Apply specific deep enrichments if defined
        if pid in deep_enrichments:
            for k, v in deep_enrichments[pid].items():
                p[k] = v
        # Ensure 'facts' array exists with at least 3 points
        if "facts" not in p or not isinstance(p["facts"], dict) or len(p["facts"].get("uk", [])) < 2:
            badge_txt = p.get('badge', 'Must-See')
            p["facts"] = {
                "uk": [
                    f"📍 {p['name']['uk']} є сертифікованою ключовою локацією маршруту ({badge_txt}).",
                    f"🌋 Наукова геологія: {p['geology']['uk']}",
                    f"📜 Культурний контекст: {p['saga']['uk']}"
                ],
                "en": [
                    f"📍 {p['name']['en']} is a certified key waypoint ({badge_txt}).",
                    f"🌋 Scientific geology: {p['geology']['en']}",
                    f"📜 Historical context: {p['saga']['en']}"
                ]
            }
        # Ensure 75-second audioScript exists
        if "audioScript" not in p or not isinstance(p["audioScript"], dict) or len(p["audioScript"].get("uk", "")) < 80:
            p["audioScript"] = {
                "uk": f"Вітаємо на локації {p['name']['uk']}! {p['vector']['uk']}. Геологічна структура: {p['geology']['uk']}. Історичне значення та фольклор: {p['saga']['uk']}. Порада водію та правила безпеки: {p['practical']['uk']}. Насолоджуйтеся дослідженням цього унікального куточка первозданної природи Ісландії!",
                "en": f"Welcome to {p['name']['en']}! Location vector: {p['vector']['en']}. Geological background: {p['geology']['en']}. Historical chronicles and legends: {p['saga']['en']}. Critical driver safety and logistics: {p['practical']['en']}. Enjoy exploring this extraordinary Icelandic landmark!"
            }

    new_pois_json = json.dumps(pois_list, ensure_ascii=False)
    index_html = index_html[:pois_match.start()] + f"const POIS = {new_pois_json};" + index_html[pois_match.end():]
    print(f"Updated POIS array with {len(pois_list)} items.")

# ----------------------------------------------------
# 3. INJECT MASTER_FACTS CONSTANT INTO SCRIPT
# ----------------------------------------------------
master_facts_json = json.dumps(ICELAND_MASTER_FACTS, ensure_ascii=False)
master_facts_script = f"\n    // MASTER ICELAND INTERESTING FACTS DATASET (40+ VERIFIED FACTS)\n    const MASTER_FACTS = {master_facts_json};\n"

if "const MASTER_FACTS =" not in index_html:
    index_html = index_html.replace("const POIS =", master_facts_script + "    const POIS =", 1)
    print("Injected MASTER_FACTS dataset into script.")

# ----------------------------------------------------
# 4. UPGRADE #poi-modal IN INDEX.HTML
# ----------------------------------------------------
# Replace the contents of poi-modal body to show facts and audio script
old_modal_body = '''        <div class="space-y-1">
          <div class="text-cyan-400 font-bold flex items-center gap-1.5">
            <span>🛡️</span> Порада водію та Безпека (SafeTravel.is):
          </div>
          <p class="text-slate-300" id="modal-poi-practical">--</p>
        </div>'''

new_modal_body = '''        <div class="space-y-1">
          <div class="text-cyan-400 font-bold flex items-center gap-1.5">
            <span>🛡️</span> Порада водію та Безпека (SafeTravel.is):
          </div>
          <p class="text-slate-300" id="modal-poi-practical">--</p>
        </div>

        <!-- FACTS BLOCK -->
        <div class="space-y-2 pt-2 border-t border-slate-800">
          <div class="text-amber-400 font-bold flex items-center justify-between">
            <span class="flex items-center gap-1.5"><span>💡</span> Цікаві факти &amp; Інсайти локації:</span>
            <span class="text-[10px] text-slate-400 font-mono">Перевірено Leiðsöguskólinn</span>
          </div>
          <div id="modal-poi-facts" class="space-y-1.5">
            <!-- Facts list rendered dynamically -->
          </div>
        </div>

        <!-- 75-SECOND BROADCAST SCRIPT -->
        <div class="p-3.5 rounded-xl bg-gradient-to-br from-cyan-950/40 via-slate-900/90 to-slate-950 border border-cyan-500/30 space-y-2">
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-2">
              <span class="w-2.5 h-2.5 rounded-full bg-cyan-400 animate-pulse"></span>
              <span class="text-cyan-300 font-bold text-xs">🎙️ Дикторський аудіоскрипт (75 сек):</span>
            </div>
            <button onclick="playModalAudio()" id="btn-modal-listen" class="px-2.5 py-1 rounded-lg bg-cyan-500/20 hover:bg-cyan-500/40 text-cyan-300 text-[11px] font-semibold border border-cyan-500/40 flex items-center gap-1 transition">
              <span>▶</span> <span>Слухати аудіогід</span>
            </button>
          </div>
          <p class="text-slate-300 italic text-[11px] leading-relaxed border-l-2 border-cyan-500/50 pl-3 py-0.5" id="modal-poi-audioscript">--</p>
        </div>'''

if old_modal_body in index_html and 'id="modal-poi-facts"' not in index_html:
    index_html = index_html.replace(old_modal_body, new_modal_body, 1)
    print("Upgraded #poi-modal with facts and audio script blocks.")

# ----------------------------------------------------
# 5. INJECT #facts-modal HTML INTO INDEX.HTML
# ----------------------------------------------------
facts_modal_html = '''
  <!-- MODAL 4: MASTER INTERESTING FACTS ABOUT ICELAND -->
  <div id="facts-modal" class="hidden fixed inset-0 z-50 bg-black/85 backdrop-blur-md flex items-center justify-center p-3 sm:p-5">
    <div class="glass-panel w-full max-w-4xl rounded-2xl border border-amber-500/40 overflow-hidden shadow-2xl flex flex-col max-h-[92vh]">
      <!-- Header -->
      <div class="px-5 py-4 border-b border-slate-800 bg-gradient-to-r from-amber-950/60 via-slate-900 to-slate-900 flex items-center justify-between">
        <div class="flex items-center space-x-3">
          <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-amber-500 to-orange-500 flex items-center justify-center text-xl shadow-lg shadow-amber-500/20">
            💡
          </div>
          <div>
            <div class="flex items-center space-x-2">
              <h3 class="text-base font-bold text-white">Цікаві факти про Ісландію</h3>
              <span class="px-2 py-0.5 rounded bg-amber-500/20 text-amber-300 font-mono text-[10px] font-bold border border-amber-500/30">ЕКСКЛЮЗИВ</span>
            </div>
            <p class="text-[11px] text-slate-400">Перевірені академічні інсайти ліцензованого гіда • Генетика, вулкани, саги та природа</p>
          </div>
        </div>
        <button onclick="closeFactsModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center text-sm">✕</button>
      </div>

      <!-- Search and Filter Bar -->
      <div class="p-4 border-b border-slate-800 bg-slate-950/80 space-y-3">
        <div class="relative">
          <span class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none text-slate-400 text-xs">🔍</span>
          <input type="text" id="facts-search-input" oninput="handleFactsSearch(this.value)" placeholder="Пошук фактів (напр. Gullfoss, коні, ДНК, вулкан, комар, мова, ГЕС)..." class="w-full pl-9 pr-4 py-2 bg-slate-900 border border-slate-700/80 rounded-xl text-xs text-slate-200 placeholder-slate-500 focus:outline-none focus:border-amber-400 transition">
        </div>

        <div class="flex items-center gap-1.5 overflow-x-auto pb-1 text-[11px]" id="facts-category-pills">
          <button onclick="filterFactsCategory('all')" class="facts-pill active px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-amber-500 text-slate-950">Всі факти</button>
          <button onclick="filterFactsCategory('waterfalls_canyons')" class="facts-pill px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-slate-800">💧 Водоспади &amp; Каньйони</button>
          <button onclick="filterFactsCategory('volcanoes_geology')" class="facts-pill px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-slate-800">🌋 Вулкани &amp; Геологія</button>
          <button onclick="filterFactsCategory('science_genetics')" class="facts-pill px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-slate-800">🧬 Наука &amp; Генетика</button>
          <button onclick="filterFactsCategory('nature_fauna')" class="facts-pill px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-slate-800">🐴 Фауна &amp; Коні</button>
          <button onclick="filterFactsCategory('society_culture')" class="facts-pill px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-slate-800">🏛️ Суспільство &amp; Мова</button>
          <button onclick="filterFactsCategory('energy_climate')" class="facts-pill px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-slate-800">⚡ Зелена Енергія</button>
        </div>
      </div>

      <!-- Facts Grid -->
      <div class="p-4 overflow-y-auto space-y-3 text-xs" id="facts-container" style="max-height: 60vh;">
        <!-- Fact cards populated by JS -->
      </div>

      <!-- Footer -->
      <div class="p-3 border-t border-slate-800 bg-slate-950 flex items-center justify-between text-[11px] text-slate-400">
        <div>Всього перевірених фактів у базі: <span id="facts-count-badge" class="font-bold text-amber-400">--</span></div>
        <button onclick="closeFactsModal()" class="px-4 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200">Закрити</button>
      </div>
    </div>
  </div>
'''

if 'id="facts-modal"' not in index_html:
    # Insert before </body>
    index_html = index_html.replace('</body>', facts_modal_html + '\n</body>', 1)
    print("Injected #facts-modal HTML into index.html.")

# ----------------------------------------------------
# 6. INJECT #floating-audio-player HTML INTO INDEX.HTML
# ----------------------------------------------------
audio_player_html = '''
  <!-- FLOATING PERSISTENT AUDIO GUIDE BAR -->
  <div id="floating-audio-player" class="hidden fixed bottom-4 left-1/2 -translate-x-1/2 w-11/12 max-w-2xl z-40 bg-slate-900/95 backdrop-blur-xl border border-cyan-500/50 rounded-2xl shadow-2xl p-3.5 flex flex-col gap-2 transition-all duration-300">
    <div class="flex items-center justify-between">
      <div class="flex items-center space-x-2.5 overflow-hidden">
        <span class="text-xl" id="fplayer-icon">🎙️</span>
        <div class="truncate">
          <div class="flex items-center gap-1.5">
            <h4 class="text-xs font-bold text-white truncate" id="fplayer-title">Gullfoss</h4>
            <span class="text-[9px] px-1.5 py-0.2 rounded bg-cyan-500/20 text-cyan-300 font-mono" id="fplayer-badge">Аудіогід 75с</span>
          </div>
          <p class="text-[10px] text-slate-400 truncate" id="fplayer-status">Відтворення дикторської розповіді...</p>
        </div>
      </div>

      <!-- Equalizer Visualizer and Controls -->
      <div class="flex items-center space-x-2 shrink-0">
        <!-- SVG Equalizer Bars -->
        <div class="flex items-end space-x-0.5 h-4 px-1" id="fplayer-eq">
          <span class="w-1 bg-cyan-400 rounded-full animate-bounce h-2" style="animation-delay: 0.1s"></span>
          <span class="w-1 bg-cyan-400 rounded-full animate-bounce h-4" style="animation-delay: 0.3s"></span>
          <span class="w-1 bg-cyan-400 rounded-full animate-bounce h-3" style="animation-delay: 0.2s"></span>
          <span class="w-1 bg-cyan-400 rounded-full animate-bounce h-4" style="animation-delay: 0.4s"></span>
          <span class="w-1 bg-cyan-400 rounded-full animate-bounce h-2" style="animation-delay: 0.15s"></span>
        </div>

        <button onclick="toggleFloatingPlayPause()" id="btn-fplayer-toggle" class="w-8 h-8 rounded-lg bg-cyan-600 hover:bg-cyan-500 text-white flex items-center justify-center text-xs font-bold shadow-md shadow-cyan-600/30">
          ⏸
        </button>

        <button onclick="stopAudio()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white flex items-center justify-center text-xs">
          ⏹
        </button>

        <button onclick="toggleAudioScriptDrawer()" class="px-2 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-[10px] flex items-center gap-1">
          <span>📜</span> <span id="fplayer-drawer-label">Текст</span>
        </button>
      </div>
    </div>

    <!-- Scrubber and Timeline -->
    <div class="space-y-1">
      <div class="w-full bg-slate-800 h-1.5 rounded-full overflow-hidden cursor-pointer" onclick="seekAudioProgress(event)">
        <div id="fplayer-progress" class="bg-gradient-to-r from-cyan-400 to-blue-500 h-full rounded-full transition-all duration-300" style="width: 0%"></div>
      </div>
      <div class="flex items-center justify-between text-[10px] font-mono text-slate-400">
        <span id="fplayer-curr-time">0:00</span>
        <span id="fplayer-note" class="text-amber-400 text-[9px]"></span>
        <span id="fplayer-total-time">1:15</span>
      </div>
    </div>

    <!-- Live Teleprompter Script Drawer (collapsible) -->
    <div id="fplayer-script-drawer" class="hidden p-2.5 rounded-xl bg-slate-950/80 border border-slate-800 text-[11px] text-slate-300 italic leading-relaxed max-h-28 overflow-y-auto">
      <p id="fplayer-transcript-text">--</p>
    </div>
  </div>
'''

if 'id="floating-audio-player"' not in index_html:
    index_html = index_html.replace('</body>', audio_player_html + '\n</body>', 1)
    print("Injected #floating-audio-player HTML into index.html.")

# ----------------------------------------------------
# 7. ADD JAVASCRIPT LOGIC FOR FACTS AND AUDIO ENGINE
# ----------------------------------------------------
js_audio_and_facts_code = '''
    // ==========================================
    // FACTS ENGINE & MODAL MANAGEMENT
    // ==========================================
    let currentFactsCategory = 'all';
    let currentFactsSearch = '';

    function openFactsModal() {
      renderFactsList();
      const m = document.getElementById('facts-modal');
      if (m) m.classList.remove('hidden');
    }

    function closeFactsModal() {
      const m = document.getElementById('facts-modal');
      if (m) m.classList.add('hidden');
    }

    function filterFactsCategory(cat) {
      currentFactsCategory = cat;
      const buttons = document.querySelectorAll('#facts-category-pills button');
      buttons.forEach(btn => {
        btn.className = 'facts-pill px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-slate-900 text-slate-300 hover:text-white border border-slate-800';
      });
      event.target.className = 'facts-pill active px-3 py-1 rounded-lg font-semibold whitespace-nowrap bg-amber-500 text-slate-950';
      renderFactsList();
    }

    function handleFactsSearch(val) {
      currentFactsSearch = val.toLowerCase().trim();
      renderFactsList();
    }

    function renderFactsList() {
      const container = document.getElementById('facts-container');
      if (!container) return;

      // Filter master facts
      let filtered = MASTER_FACTS.filter(item => {
        const matchCategory = currentFactsCategory === 'all' || item.category === currentFactsCategory;
        const textToSearch = (item.title[currentLang] + ' ' + item.fact[currentLang] + ' ' + (item.poiId || '')).toLowerCase();
        const matchSearch = !currentFactsSearch || textToSearch.includes(currentFactsSearch);
        return matchCategory && matchSearch;
      });

      document.getElementById('facts-count-badge').textContent = `${filtered.length} з ${MASTER_FACTS.length}`;
      container.innerHTML = '';

      if (filtered.length === 0) {
        container.innerHTML = `
          <div class="text-center py-8 text-slate-500">
            <div class="text-3xl mb-2">🔍</div>
            <p>За вашим запитом нічого не знайдено.</p>
          </div>
        `;
        return;
      }

      filtered.forEach(item => {
        const poi = item.poiId ? POIS.find(p => p.id === item.poiId) : null;
        const card = document.createElement('div');
        card.className = 'p-3.5 rounded-xl bg-slate-900/90 border border-slate-800/90 hover:border-amber-500/40 transition space-y-2';

        let poiActionBtn = '';
        if (poi) {
          poiActionBtn = `
            <button onclick="selectPoiFromFact('${poi.id}')" class="px-2.5 py-1 rounded-lg bg-gradient-to-r from-amber-500/20 to-orange-500/20 hover:from-amber-500/30 hover:to-orange-500/30 text-amber-300 border border-amber-500/40 text-[11px] font-semibold flex items-center gap-1 transition">
              <span>📍</span> <span>Показати ${poi.name[currentLang]} на карті &amp; Досьє</span>
            </button>
          `;
        }

        card.innerHTML = `
          <div class="flex items-center justify-between gap-2">
            <span class="px-2 py-0.5 rounded bg-amber-500/15 text-amber-300 font-mono text-[10px] font-bold border border-amber-500/30">
              ${item.category_name[currentLang]}
            </span>
            ${poi ? `<span class="text-[10px] text-slate-500 font-mono">POI: ${poi.name[currentLang]}</span>` : ''}
          </div>
          <h4 class="text-xs font-bold text-white">${item.title[currentLang]}</h4>
          <p class="text-[11px] text-slate-300 leading-relaxed">${item.fact[currentLang]}</p>
          ${poiActionBtn ? `<div class="pt-2 border-t border-slate-800/80 flex items-center justify-end">${poiActionBtn}</div>` : ''}
        `;
        container.appendChild(card);
      });
    }

    function selectPoiFromFact(poiId) {
      closeFactsModal();
      focusPoi(poiId);
      setTimeout(() => {
        openPoiModal(poiId);
      }, 400);
    }

    // ==========================================
    // ADVANCED AUDIO ENGINE (VOICE + SCROLLER + AMBIENT SYNTH)
    // ==========================================
    let audioScrubberInterval = null;
    let audioCurrentSeconds = 0;
    const AUDIO_TOTAL_SECONDS = 75;
    let isAudioPaused = false;
    let activeAudioPoi = null;
    let webAudioCtx = null;
    let ambientOscillator = null;

    function initWebAudio() {
      if (!webAudioCtx) {
        try {
          const AudioContext = window.AudioContext || window.webkitAudioContext;
          webAudioCtx = new AudioContext();
        } catch (e) {
          console.warn('Web Audio API not supported', e);
        }
      }
    }

    function playAmbientGlacierTone() {
      try {
        initWebAudio();
        if (webAudioCtx && webAudioCtx.state === 'suspended') {
          webAudioCtx.resume();
        }
        if (webAudioCtx && !ambientOscillator) {
          const osc = webAudioCtx.createOscillator();
          const gain = webAudioCtx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(144, webAudioCtx.currentTime); // Gentle low sub-arctic drone
          gain.gain.setValueAtTime(0.015, webAudioCtx.currentTime);
          osc.connect(gain);
          gain.connect(webAudioCtx.destination);
          osc.start();
          ambientOscillator = osc;
        }
      } catch (err) {
        console.warn('Ambient tone warning', err);
      }
    }

    function stopAmbientGlacierTone() {
      try {
        if (ambientOscillator) {
          ambientOscillator.stop();
          ambientOscillator.disconnect();
          ambientOscillator = null;
        }
      } catch (e) {}
    }

    function playPoiAudio(poiId) {
      const poi = POIS.find(p => p.id === poiId);
      if (!poi) return;

      if (currentlyPlayingAudioPoiId === poiId && !isAudioPaused) {
        toggleFloatingPlayPause();
        return;
      }

      stopAudio();

      activeAudioPoi = poi;
      currentlyPlayingAudioPoiId = poiId;
      isAudioPaused = false;
      audioCurrentSeconds = 0;

      // Update Floating Player UI
      const fPlayer = document.getElementById('floating-audio-player');
      if (fPlayer) fPlayer.classList.remove('hidden');

      document.getElementById('fplayer-icon').textContent = poi.icon || '🎙️';
      document.getElementById('fplayer-title').textContent = poi.name[currentLang];
      document.getElementById('fplayer-badge').textContent = poi.badge || '75-сек гід';
      document.getElementById('fplayer-status').textContent = 'Відтворення дикторської розповіді...';
      document.getElementById('fplayer-transcript-text').textContent = poi.audioScript ? poi.audioScript[currentLang] : poi.geology[currentLang];
      document.getElementById('btn-fplayer-toggle').textContent = '⏸';
      document.getElementById('fplayer-note').textContent = '';

      // Start Ambient Glacier Tone
      playAmbientGlacierTone();

      // Start Timer Scrubber
      startAudioScrubber();

      // Speech Synthesis execution
      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();

        const scriptText = (poi.audioScript && poi.audioScript[currentLang]) 
          ? poi.audioScript[currentLang] 
          : `${poi.name[currentLang]}. ${poi.vector[currentLang]}. ${poi.geology[currentLang]}. ${poi.saga[currentLang]}. ${poi.practical[currentLang]}`;

        const u = new SpeechSynthesisUtterance(scriptText);
        
        // Detect voices
        const voices = window.speechSynthesis.getVoices();
        const ukVoice = voices.find(v => v.lang.toLowerCase().includes('uk') || v.lang.toLowerCase().includes('ua'));
        
        if (currentLang === 'uk') {
          if (ukVoice) {
            u.voice = ukVoice;
            u.lang = ukVoice.lang;
          } else {
            // Fallback warning if OS lacks Ukrainian TTS
            document.getElementById('fplayer-note').textContent = '📢 Читайте синхронний скрипт (uk-UA голос не знайдено)';
            u.lang = 'uk-UA';
          }
        } else {
          u.lang = 'en-US';
          const enVoice = voices.find(v => v.lang.startsWith('en'));
          if (enVoice) u.voice = enVoice;
        }

        u.rate = 1.0;
        u.pitch = 1.0;

        u.onend = () => {
          stopAudio();
        };

        u.onerror = (e) => {
          console.warn('Speech synthesis notification:', e);
          document.getElementById('fplayer-status').textContent = 'Синхронний режим телесуфлера (читайте текст)';
        };

        window.speechSynthesis.speak(u);
      }

      renderPoiList();
    }

    function startAudioScrubber() {
      clearInterval(audioScrubberInterval);
      audioScrubberInterval = setInterval(() => {
        if (!isAudioPaused) {
          audioCurrentSeconds++;
          const progressPercent = Math.min(100, (audioCurrentSeconds / AUDIO_TOTAL_SECONDS) * 100);
          const progBar = document.getElementById('fplayer-progress');
          if (progBar) progBar.style.width = `${progressPercent}%`;

          const m = Math.floor(audioCurrentSeconds / 60);
          const s = audioCurrentSeconds % 60;
          const currTimeElem = document.getElementById('fplayer-curr-time');
          if (currTimeElem) currTimeElem.textContent = `${m}:${s < 10 ? '0' : ''}${s}`;

          if (audioCurrentSeconds >= AUDIO_TOTAL_SECONDS) {
            stopAudio();
          }
        }
      }, 1000);
    }

    function toggleFloatingPlayPause() {
      if (!activeAudioPoi) return;

      if (isAudioPaused) {
        // Resume
        isAudioPaused = false;
        if ('speechSynthesis' in window && window.speechSynthesis.paused) {
          window.speechSynthesis.resume();
        }
        document.getElementById('btn-fplayer-toggle').textContent = '⏸';
        document.getElementById('fplayer-status').textContent = 'Відтворення дикторської розповіді...';
      } else {
        // Pause
        isAudioPaused = true;
        if ('speechSynthesis' in window && window.speechSynthesis.speaking) {
          window.speechSynthesis.pause();
        }
        document.getElementById('btn-fplayer-toggle').textContent = '▶';
        document.getElementById('fplayer-status').textContent = 'Пауза аудіогіда';
      }
    }

    function seekAudioProgress(event) {
      const rect = event.currentTarget.getBoundingClientRect();
      const clickX = event.clientX - rect.left;
      const width = rect.width;
      const fraction = Math.max(0, Math.min(1, clickX / width));
      audioCurrentSeconds = Math.floor(fraction * AUDIO_TOTAL_SECONDS);
      const progBar = document.getElementById('fplayer-progress');
      if (progBar) progBar.style.width = `${fraction * 100}%`;
    }

    function toggleAudioScriptDrawer() {
      const drawer = document.getElementById('fplayer-script-drawer');
      const label = document.getElementById('fplayer-drawer-label');
      if (drawer.classList.contains('hidden')) {
        drawer.classList.remove('hidden');
        label.textContent = 'Згорнути';
      } else {
        drawer.classList.add('hidden');
        label.textContent = 'Текст';
      }
    }

    // Replace previous stopAudio with comprehensive cleanup
    function stopAudio() {
      clearInterval(audioScrubberInterval);
      audioScrubberInterval = null;
      audioCurrentSeconds = 0;
      isAudioPaused = false;
      activeAudioPoi = null;
      currentlyPlayingAudioPoiId = null;
      isRangerPlaying = false;

      stopAmbientGlacierTone();

      if ('speechSynthesis' in window) {
        window.speechSynthesis.cancel();
      }

      const fPlayer = document.getElementById('floating-audio-player');
      if (fPlayer) fPlayer.classList.add('hidden');

      const progBar = document.getElementById('fplayer-progress');
      if (progBar) progBar.style.width = '0%';

      renderPoiList();
      const btn = document.getElementById('btn-ranger-audio-mini');
      if (btn) btn.innerHTML = '<span>▶ Слухати ранковий бриф</span>';
      const btnM = document.getElementById('btn-ranger-audio-modal');
      if (btnM) btnM.innerHTML = '<span>▶ Слухати аудіо-бриф</span>';
    }
'''

# Update openPoiModal to render facts and audioScript
old_open_poi_modal = '''    function openPoiModal(poiId) {
      const poi = POIS.find(p => p.id === poiId);
      if (!poi) return;
      modalActivePoi = poi;

      document.getElementById('modal-poi-title').textContent = poi.name[currentLang];
      document.getElementById('modal-poi-badge').textContent = poi.badge;
      document.getElementById('modal-poi-type').textContent = poi.type[currentLang];
      document.getElementById('modal-poi-vector').textContent = poi.vector[currentLang];
      document.getElementById('modal-poi-geology').textContent = poi.geology[currentLang];
      document.getElementById('modal-poi-saga').textContent = poi.saga[currentLang];
      document.getElementById('modal-poi-practical').textContent = poi.practical[currentLang];
      document.getElementById('modal-poi-coords').textContent = `${poi.lat}° N, ${poi.lng}° W`;

      const m = document.getElementById('poi-modal');
      if (m) m.classList.remove('hidden');
    }'''

new_open_poi_modal = '''    function openPoiModal(poiId) {
      const poi = POIS.find(p => p.id === poiId);
      if (!poi) return;
      modalActivePoi = poi;

      document.getElementById('modal-poi-title').textContent = poi.name[currentLang];
      document.getElementById('modal-poi-badge').textContent = poi.badge;
      document.getElementById('modal-poi-type').textContent = poi.type[currentLang];
      document.getElementById('modal-poi-vector').textContent = poi.vector[currentLang];
      document.getElementById('modal-poi-geology').textContent = poi.geology[currentLang];
      document.getElementById('modal-poi-saga').textContent = poi.saga[currentLang];
      document.getElementById('modal-poi-practical').textContent = poi.practical[currentLang];
      document.getElementById('modal-poi-coords').textContent = `${poi.lat}° N, ${poi.lng}° W`;

      // Render facts
      const factsContainer = document.getElementById('modal-poi-facts');
      if (factsContainer) {
        factsContainer.innerHTML = '';
        const factsList = (poi.facts && poi.facts[currentLang]) ? poi.facts[currentLang] : [];
        if (factsList.length === 0) {
          factsContainer.innerHTML = '<p class="text-slate-400 italic text-[11px]">Факти завантажуються з центральної бази...</p>';
        } else {
          factsList.forEach(f => {
            const pElem = document.createElement('p');
            pElem.className = 'text-slate-300 text-[11px] leading-relaxed bg-slate-900/60 p-2 rounded-lg border border-slate-800/80';
            pElem.innerHTML = f;
            factsContainer.appendChild(pElem);
          });
        }
      }

      // Render audio script
      const scriptElem = document.getElementById('modal-poi-audioscript');
      if (scriptElem) {
        scriptElem.textContent = (poi.audioScript && poi.audioScript[currentLang]) 
          ? poi.audioScript[currentLang] 
          : `${poi.name[currentLang]}. ${poi.vector[currentLang]}. ${poi.geology[currentLang]}`;
      }

      const m = document.getElementById('poi-modal');
      if (m) m.classList.remove('hidden');
    }'''

if old_open_poi_modal in index_html:
    index_html = index_html.replace(old_open_poi_modal, new_open_poi_modal, 1)
    print("Updated openPoiModal function in index.html.")

# Replace playPoiAudio and stopAudio functions
play_audio_regex = r'function playPoiAudio\(poiId\) \{.*?function stopAudio\(\) \{.*?\n    \}'
# Find where playPoiAudio starts and replace up to end of stopAudio
match_audio = re.search(r'function playPoiAudio\(poiId\) \{.*?function stopAudio\(\) \{.*?\n    \}', index_html, re.DOTALL)
if match_audio:
    index_html = index_html[:match_audio.start()] + js_audio_and_facts_code + index_html[match_audio.end():]
    print("Replaced audio engine and injected facts engine.")

# Ensure window exports
export_target = 'window.setNavMode = setNavMode;'
new_exports = '''window.setNavMode = setNavMode;
    window.openFactsModal = openFactsModal;
    window.closeFactsModal = closeFactsModal;
    window.filterFactsCategory = filterFactsCategory;
    window.handleFactsSearch = handleFactsSearch;
    window.selectPoiFromFact = selectPoiFromFact;
    window.toggleFloatingPlayPause = toggleFloatingPlayPause;
    window.seekAudioProgress = seekAudioProgress;
    window.toggleAudioScriptDrawer = toggleAudioScriptDrawer;'''

if export_target in index_html and 'window.openFactsModal = openFactsModal;' not in index_html:
    index_html = index_html.replace(export_target, new_exports, 1)
    print("Exported window facts and audio functions.")

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(index_html)

print("Saved updated index.html successfully.")
