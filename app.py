from flask import Flask, render_template

app = Flask(__name__)

# ============================================================
# Данные о проекте (Intro data)
# ============================================================

INTRO = {
    'compilers': [
        'Ավանեսյան Անի',
        'Գրիգորյան Նարինե',
        'Կոստանյան Վիկա',
        'Մուրադյան Էլեն',
        'Նիկողոսյան Գայանե',
        'Շահնազարյան Վահե',
        'Սարյան Լուսինե',
    ],
    'assignments': [
        ('Հայոց լեզու', 'Ավանեսյան Անի'),
        ('Հայ գրականություն', 'Սարյան Լուսինե'),
        ('Հայոց պատմություն', 'Մուրադյան Էլեն'),
        ('Համաշխարհային պատմություն', 'Կոստանյան Վիկա, Նիկողոսյան Գայանե'),
        ('Ռուսաց լեզու (քերականություն)', 'Գրիգորյան Նարինե'),
        ('Ռուսաց լեզու (գրականություն)', 'Շահնազարյան Վահե'),
        ('Անգլերեն', 'Գրիգորյան Նարինե, Շահնազարյան Վահե'),
    ],
    'editor': 'Վահե Շահնազարյան',
    'supervisor': 'Ալիսա Ղալթախսազյան',
    'letter': (
        'Սիրելի ընթերցող, Ձեր ձեռքում է մեր ստեղծած բառարանը, '
        'որը ծնվել է «Հայոց լեզու» առարկայի նախագծային աշխատանքի ընթացքում: '
        'Այս գրքի ստեղծման ընթացքում մենք միասին անցանք երկար ճանապարհ — '
        'սովորելով, քննարկելով, որոնելով և ձևավորելով այս գիրքը: '
        'Մենք — նախագծային աշխատանքի անդամներս — քրտնաջան աշխատել ենք մեր սիրելի ուսուցչի՝ '
        'Ալիսա Ղալթախսազյանի հետ: Նա մշտապես եղել է մեր կողքին — խորհուրդներով, '
        'օգնությամբ և անսահման համբերատարությամբ ու անձնվիրությամբ, ինչի համար մենք '
        'առանձնահատուկ շնորհակալություն ենք ուզում հայտնել իրեն:'
    ),
}

# ============================================================
# Разделы словаря с выверенным армянским контентом
# ============================================================

SECTIONS = {
    'hayoc_lezou': {
        'title': 'Հայոց լեզու',
        'emoji': '🇦🇲',
        'color': '#e74c3c',
        'pages': '3–12',
        'content': """
<h3>Հարադրավոր բաղադրյալ հատուկ անվան բոլոր բաղադրիչները (բացի շաղկապներից) գրվում են մեծատարով</h3>

<h4>Անձնանուններ</h4>

<div class="letter-section">
<div class="letter">Ա</div>
<ul>
<li>Ակսել Բակունց</li><li>Ալիսիա Կիրակոսյան</li><li>Անտոն Հիժնյակ</li>
<li>Անտուան Մեյ</li><li>Արամ Խաչատրյան</li><li>Առնո Բաբաջանյան</li>
<li>Արշալույս Մարգարյան</li><li>Ազատ Վշտունի</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Բ</div>
<p class="empty-note">(—)</p>
</div>

<div class="letter-section">
<div class="letter">Գ</div>
<ul>
<li>Գեղամ Սարյան</li><li>Գևորգ Էմին</li><li>Գրիգոր Լուսավորիչ</li><li>Գրիգոր Նարեկացի</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Դ</div>
<ul><li>Դավիթ Զաքարյան</li></ul>
</div>

<div class="letter-section">
<div class="letter">Է</div>
<ul><li>Էդուարդ Մեժելայտիս</li></ul>
</div>

<div class="letter-section">
<div class="letter">Թ</div>
<ul><li>Թոմ Քրոնին</li></ul>
</div>

<div class="letter-section">
<div class="letter">Ժ</div>
<ul><li>Պերճ Ժամկոչյան</li></ul>
</div>

<div class="letter-section">
<div class="letter">Խ</div>
<ul>
<li>Խորեն Պալյան</li><li>Հենրիխ Հյուբշման</li><li>Անտոն Հիժնյակ</li>
<li>Արամ Խաչատրյան</li><li>Մովսես Խորենացի</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Լ</div>
<ul><li>Լուսինե Զաքարյան</li></ul>
</div>

<div class="letter-section">
<div class="letter">Մ</div>
<ul>
<li>Մարտիրոս Սարյան</li><li>Մեսրոպ Մաշտոց</li><li>Մխիթար Գոշ</li>
<li>Միխայիլ Մատուսովսկի</li><li>Մովսես Խորենացի</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Ն</div>
<ul><li>Նաիրի Զարյան</li></ul>
</div>

<div class="letter-section">
<div class="letter">Պ</div>
<ul>
<li>Պարույր Սևակ</li><li>Պետրոս Դուրյան</li><li>Պերճ Ժամկոչյան</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Ս</div>
<ul>
<li>Սիլվա Կապուտիկյան</li><li>Ստեփան Զորյան</li><li>Ստեփան Շիրազ</li>
<li>Սվետլանա Նավասարդյան</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Տ</div>
<ul>
<li>Տիգրան Մանսուրյան</li><li>Իոսիֆ Տեմաշևիչ</li>
<li>Ելենա Տոմաշևսկայա</li><li>Վերոնիկա Տոմաշևսկայա</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Վ</div>
<ul>
<li>Վարդան Այգեկցի</li><li>Վահագն Դավթյան</li><li>Վերոնիկա Տոմաշևսկայա</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Հ</div>
<ul>
<li>Հովհաննես Թումանյան</li><li>Հովհաննես Իսակով</li><li>Հենրիխ Հյուբշման</li>
<li>Հրաչյա Աճառյան</li><li>Հակոբ Կոջոյան</li><li>Հաբեթ Զաքարյան</li>
</ul>
</div>

<div class="letter-section">
<div class="letter">Ջ</div>
<ul><li>Ջոնաթան Сվիֆթ</li></ul>
</div>

<div class="letter-section">
<div class="letter">Ռ</div>
<ul><li>Ռոմանոս Մելիքյան</li></ul>
</div>

<div class="letter-section">
<div class="letter">Մ</div>
<ul><li>Մարգար Մարգարյան</li></ul>
</div>

<hr class="section-divider">
<h4>Աշխարհագրական տեղանուններ — Պետությունների անուններում</h4>

<div class="letter-section">
<div class="letter">Ա</div>
<ul><li>Ամերիկայի Միացյալ Նահանգներ</li></ul>
</div>

<div class="letter-section">
<div class="letter">Ի</div>
<ul><li>Իրանի Իսլամական Հանրապետություն</li></ul>
</div>

<div class="letter-section">
<div class="letter">Լ</div>
<ul><li>Լեռնային Ղարաբաղի Հանրապետություն</li></ul>
</div>

<div class="letter-section">
<div class="letter">Ն</div>
<ul><li>Նախիջևանի Ինքնավար Հանրապետություն</li></ul>
</div>

<div class="letter-section">
<div class="letter">Հ</div>
<ul><li>Հայաստանի Հանրապետություն</li></ul>
</div>

<div class="letter-section">
<div class="letter">Ս</div>
<ul><li>Սանկտ Պետերբուրգ</li></ul>
</div>

<hr class="section-divider">
<h4>Լրացումից և լրացյալից կազմված անվանումներ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Ախթալայի ամրոց</li><li>Ակոռիի լեռնային սարավանդ</li>
<li>Արամ նահապետ</li><li>Արայի լեռներ</li>
<li>Արարատյան դաշտ</li><li>Արեգունի լեռնաշղթա</li><li>Արտանիշ թերակղզի</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Բ</div>
<ul><li>Բարաբեր գետ</li></ul>
</div>

<div class="letter-section"><div class="letter">Գ</div>
<ul>
<li>Գայանեի տաճար</li><li>Գեղամա սարեր</li>
<li>Գետիկի ավազան</li><li>Գետիկի հովիտ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Դ</div>
<ul>
<li>Դեբեդի ձոր</li><li>Դիլիջան ազգային այգի</li>
<li>Դրախտիկ գետ</li><li>Դսեղի լեռնային սարավանդ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Զ</div>
<ul><li>Զաքարե զորավար</li></ul>
</div>

<div class="letter-section"><div class="letter">Թ</div>
<ul>
<li>Թիֆլիսի ռեալական համալսարան</li><li>Թումանյան կայարան</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ժ</div>
<ul><li>Ժանգոտ լիճ</li></ul>
</div>

<div class="letter-section"><div class="letter">Լ</div>
<ul><li>Լոռվա դաշտ</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մշո Սուրբ Կարապետ վանք</li><li>Միափորի լեռնանցք</li></ul>
</div>

<div class="letter-section"><div class="letter">Պ</div>
<ul>
<li>Պարզ լիճ</li><li>Պետերբուրգի կայսերական թատրոն</li>
<li>Պրյուսովի անվան արվեստանոց</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Փ</div>
<ul>
<li>Փամբակի գոգահովիտ</li><li>Փամբակի լեռներ</li><li>Փամբակի լեռնաշղթա</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul>
<li>Սանահինի կամուրջ</li><li>Սարդարապատի հուշահամալիր</li>
<li>Սևանի ավազան</li><li>Սևանի լեռնանցք</li><li>Սոսյաց անտառ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Տ</div>
<ul><li>Տաթևի վանք</li><li>Տիրի տաճար</li></ul>
</div>

<div class="letter-section"><div class="letter">Խ</div>
<ul><li>Խալդիի դարպաս</li><li>Խաղաղ օվկիանոս</li></ul>
</div>

<div class="letter-section"><div class="letter">Ք</div>
<ul><li>Քաշաթաղի լեռնագագաթ-լեռնահանգույց</li><li>Քառասնից մանկանց վանք</li></ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul>
<li>Կայան բերդ</li><li>Կասպից ծով</li><li>Կովկասյան ծովափ</li><li>Կուրի ավազան</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հաղպատի վանք</li><li>Հյուսիսկովկասյան ռազմաճակատ</li></ul>
</div>

<div class="letter-section"><div class="letter">Ճ</div>
<ul><li>Ճամբարակի գոգահովիտ</li><li>Ճամբարակի լեռնանցք</li></ul>
</div>

<hr class="section-divider">
<h4>Ստեղծագործությունների անուններ</h4>
<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Ա. Խաչատրյան «Գայանե» բալետ</li>
<li>Ա. Խաչատրյան «Սուսերով պար»</li>
</ul>
</div>

<hr class="section-divider">
<h4>Պետության կողմից շնորհվող շքանշանների անուններ</h4>
<div class="letter-section"><div class="letter">Խ</div>
<ul>
<li>ԽՍՀՄ պետական մրցանակ</li><li>Խորհրդային Միության հերոս</li>
</ul>
</div>

<hr class="section-divider">
<h4>Այլ կանոններ</h4>
<div class="rule-box">
<p><strong>Կանոն.</strong> Հայկական բառը երբեմն հատուկ անվան առաջին բաղադրիչն է:</p>
</div>
<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հայկական պար լեռնաշղթա</li><li>Հայկական Տավրոս</li></ul>
</div>

<div class="rule-box">
<p><strong>Կանոն.</strong> Տեղանուններում հաճախ հատուկ անվան առաջին բաղադրիչն են լինում Արևելյան, Մեծ, Մերձավոր, Նոր, Փոքր և այլ բառեր:</p>
</div>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Արևելյան Հայաստան</li></ul>
</div>
<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մեծ Մասիս</li><li>Մերձավոր Արևելք</li></ul>
</div>
<div class="letter-section"><div class="letter">Ն</div>
<ul><li>Նոր Ջուղա</li></ul>
</div>
<div class="letter-section"><div class="letter">Փ</div>
<ul><li>Փոքր Կովկաս</li><li>Փոքր Մասիս</li><li>Փոքր Մհեր</li><li>Փոքր Սևան</li></ul>
</div>

<div class="rule-box">
<p><strong>Կանոն.</strong> Համաստեղությունների և այլ հատուկ անվանումներում միայն առաջին բաղադրիչն է մեծատարով գրվում:</p>
</div>
<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Արեգակնային համակարգ</li></ul>
</div>
<div class="letter-section"><div class="letter">Լ</div>
<ul><li>Լուսնի խավարում</li></ul>
</div>

<div class="rule-box">
<p><strong>Կանոն.</strong> «Մայր» բառը «Մայր աթոռ Սուրբ Էջմիածին» կապակցության դեպքում է մեծատարով գրվում:</p>
</div>
<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մայր աթոռ</li></ul>
</div>

<div class="rule-box">
<p><strong>Կանոն.</strong> Եկեղեցիների, վանքերի անվանումներում, երբ «Սուրբ» բառն առաջին բաղադրիչն է, ապա գրվում է մեծատարով:</p>
</div>
<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Աղջոց Սուրբ Ստեփանոս վանք</li></ul>
</div>

<div class="rule-box">
<p><strong>Կանոն.</strong> «Աստված» բառը կարելի է մեծատարով գրել, երբ վերաբերում է քրիստոնյաների պաշտած Աստծուն, բայց փոքրատարով պետք է գրել մյուս դեպքերում:</p>
</div>
<div class="letter-section"><div class="letter">Տ</div>
<ul><li>Տիր աստված</li></ul>
</div>

<div class="rule-box"><p><strong>Կանոն.</strong> Ավանդական գրությամբ, գծիկով գրվող և առանձին բաղադրիչներով հատուկ անուններ:</p></div>
<div class="letter-section"><div class="letter">Ն</div><ul><li>Նար-Դոս</li></ul></div>
<div class="letter-section"><div class="letter">Ս</div><ul><li>Սայաթ-Նովա</li></ul></div>
"""
    },

    'hay_grakanutyan': {
        'title': 'Հայ գրականություն',
        'emoji': '📚',
        'color': '#8e44ad',
        'pages': '13–21',
        'content': """
<h3>Հարադրավոր բաղադրյալ հատուկ անվան բոլոր բաղադրիչները (բացի շաղկապներից) սկսվում են մեծատարով</h3>

<h4>Անձնանուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Ավետիք Իսահակյան</li><li>Արամ Խաչատրյան</li><li>Աքսել Բակունց</li>
<li>Ալեքսանդր Պուշկին</li><li>Ալեքսանդր Բլոկ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Գ</div>
<ul><li>Գաբրիել Սունդուկյան</li></ul>
</div>

<div class="letter-section"><div class="letter">Դ</div>
<ul><li>Դանիել Վարուժան</li><li>Դերենիկ Դեմիրճյան</li></ul>
</div>

<div class="letter-section"><div class="letter">Լ</div>
<ul><li>Լևոն Շանթ</li></ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հովհաննես Թումանյան</li><li>Հովհաննես Հովհաննիսյան</li></ul>
</div>

<div class="letter-section"><div class="letter">Ղ</div>
<ul><li>Ղևոնդ Ալիշան</li><li>Ղազարոս Աղայան</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մեսրոպ Մաշտոց</li><li>Մուրադ Ռաֆայելյան</li></ul>
</div>

<div class="letter-section"><div class="letter">Ն</div>
<ul><li>Նար-Դոս</li><li>Նաիրի Զարյան</li></ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul><li>Սուրբ Գրիգոր Լուսավորիչ</li><li>Ստեֆան Ցվայգ</li></ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul>
<li>Վահան Թեքեյան</li><li>Վասիլի Շուկշին</li><li>Վիկտոր Հյուգո</li><li>Վահան Տերյան</li>
</ul>
</div>

<hr class="section-divider">
<h4>Պատմական երկրանունների միայն առաջին բաղադրիչն է մեծատարով</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Արտաշեսյան թագավորություն</li><li>Արշակունյաց թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Բ</div>
<ul><li>Բագրատունիների թագավորություն</li><li>Բյուզանդական թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Ե</div>
<ul><li>Երվանդունիների թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul><li>Կիլիկիայի թագավորություն</li><li>Կարսի թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մեծ Հայքի թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul><li>Սյունիքի թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul><li>Վասպուրականի թագավորություն</li><li>Վանի թագավորություն</li></ul>
</div>

<hr class="section-divider">
<h4>Տեղանուններում առաջին բաղադրիչը</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Արևելյան Հայաստան</li><li>Արևմտյան Հայաստան</li></ul>
</div>

<div class="letter-section"><div class="letter">Ի</div>
<ul><li>Իսպանիայի թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Խ</div>
<ul><li>Խաղաղ օվկիանոս</li></ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul><li>Կարմիր ծով</li></ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հին աշխարհ</li><li>Հյուսիսային սառուցյալ օվկիանոս</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մեծ Բրիտանիա</li><li>Մեծ Մասիս</li></ul>
</div>

<div class="letter-section"><div class="letter">Ն</div>
<ul><li>Նոր աշխարհ</li></ul>
</div>

<hr class="section-divider">
<h4>Միջնաբերդ, դյուցազն, սպարապետ և այլն</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Անիի միջնաբերդ</li><li>Աթենքի միջնաբերդ</li><li>Անդրեաս Գունդստաբլ</li></ul>
</div>

<div class="letter-section"><div class="letter">Դ</div>
<ul><li>Դյուցազն Վարդան</li></ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հայկ նահապետ</li><li>Մեծն Նահապետ</li></ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul><li>Վազգեն սպարապետ</li></ul>
</div>

<hr class="section-divider">
<h4>Սուրբ — եկեղեցիների անվանումներում</h4>

<div class="letter-section"><div class="letter">Ս</div>
<ul>
<li>Սուրբ Գրիգոր Լուսավորիչ եկեղեցի</li>
<li>Սուրբ Թադեոս վանք</li>
<li>Սուրբ Աննա եկեղեցի</li>
<li>Սուրբ Մարիամ Մայր տաճար</li>
</ul>
</div>

<hr class="section-divider">
<h4>Մականունավոր անուններ (լրացում + մականուն)</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Արա Գեղեցիկ</li><li>Աշոտ Երկաթ</li></ul>
</div>
<div class="letter-section"><div class="letter">Գ</div>
<ul><li>Գայլ Վահան</li></ul>
</div>
<div class="letter-section"><div class="letter">Դ</div>
<ul><li>Դավիթ Անհաղթ</li></ul>
</div>
<div class="letter-section"><div class="letter">Խ</div>
<ul><li>Խոսրով Կոտակ</li></ul>
</div>
<div class="letter-section"><div class="letter">Ձ</div>
<ul><li>Ձախորդ Փանոս</li></ul>
</div>
<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մեծ Մհեր</li></ul>
</div>
<div class="letter-section"><div class="letter">Ս</div>
<ul><li>Սահակ Պարթև</li></ul>
</div>
<div class="letter-section"><div class="letter">Տ</div>
<ul><li>Տիգրան Մեծ</li></ul>
</div>

<hr class="section-divider">
<h4>Երկրների կենտրոնական ղեկավար մարմինների անուններ</h4>

<div class="letter-section"><div class="letter">Գ</div>
<ul><li>Գործադիր մարմին</li></ul>
</div>
<div class="letter-section"><div class="letter">Դ</div>
<ul><li>Դատական մարմին</li></ul>
</div>
<div class="letter-section"><div class="letter">Օ</div>
<ul><li>Օրենսդիր մարմին</li></ul>
</div>

<hr class="section-divider">
<h4>Պատմական իրադարձությունների անուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Ավարայրի ճակատամարտ</li></ul>
</div>
<div class="letter-section"><div class="letter">Թ</div>
<ul><li>Թարգմանչաց տոն</li></ul>
</div>
<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հայաստանի առաջին հանրապետության հռչակում</li><li>Հայոց ցեղասպանություն</li></ul>
</div>
<div class="letter-section"><div class="letter">Ս</div>
<ul><li>Սարդարապատի ճակատամարտ</li></ul>
</div>
<div class="letter-section"><div class="letter">Վ</div>
<ul><li>Վարդանանց պատերազմ</li><li>Վարդանանց տոն</li></ul>
</div>
<div class="letter-section"><div class="letter">Ց</div>
<ul><li>Ցեղասպանության զոհերի հիշատակի օր</li></ul>
</div>

<hr class="section-divider">
<h4>«Տեր» բառը հայկական ազգանվան կազմում մեծատարով է գրվում</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Արտաշես Տեր-Ղազարյան</li></ul>
</div>
<div class="letter-section"><div class="letter">Գ</div>
<ul><li>Գարեգին Տեր-Գրիգորյան</li></ul>
</div>
<div class="letter-section"><div class="letter">Ե</div>
<ul><li>Երվանդ Տեր-Մինասյան</li></ul>
</div>
<div class="letter-section"><div class="letter">Լ</div>
<ul><li>Լևոն Տեր-Զաքարյան</li></ul>
</div>
<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Միքայել Տեր-Մկրտչյան</li></ul>
</div>
<div class="letter-section"><div class="letter">Ռ</div>
<ul><li>Ռուբեն Տեր-Աբրահամյան</li></ul>
</div>
"""
    },

    'hayoc_patmutyun': {
        'title': 'Հայոց պատմություն',
        'emoji': '🏛️',
        'color': '#e67e22',
        'pages': '22–28',
        'content': """
<h3>«Հայկական քաղաքակրթությունը նոր շրջանում» — Հարադրավոր հատուկ անուններ</h3>

<h4>Անձնանուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Անդրանիկ Օզանյան</li><li>Արամ Մանուկյան</li><li>Արմեն Գարո</li>
<li>Ալեքսանդր Պետրոսյան</li><li>Ավետիք Իսահակյան</li><li>Առնոլդ Թոյնբի</li>
<li>Աղբյուր Սերոբ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Բ</div>
<ul>
<li>Բարսեղ Մանուկյան</li><li>Բուզանդ Կեֆտե</li><li>Բեկ-Փիրումյան</li>
<li>Բեհաեդդին Շաքիր</li><li>Բուլղարացի Գրիգոր</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Գ</div>
<ul>
<li>Գրիգոր Նարեկացի</li><li>Գրում Գուպի</li><li>Գևորգ Չավուշ</li>
<li>Գրիգոր Մոսեյան</li><li>Գարուն Աղասի</li><li>Գրիգոր Զոհրապ</li><li>Գարեգին Նժդեհ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Դ</div>
<ul>
<li>Դանիել Բեկ-Փիրումյան</li><li>Դանիել Վարուժան</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ի</div>
<ul>
<li>Իվան Կարապետ</li><li>Իսրայել Օրի</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul>
<li>Յոհաննես Լեփսիուս</li><li>Հովհաննես Թութունջի</li><li>Հակոբ Ջուղայեցի</li>
<li>Հասան-Ջալալյան</li><li>Հովհաննես Էմին</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul>
<li>Մելիք Շահնազարյան</li><li>Մովսես Սատաֆյան</li><li>Մկրտիչ Խրիմյան</li>
<li>Միհրան Տամատյան</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Յ</div>
<ul>
<li>Յան Սոբեսկի</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul>
<li>Սմբատ Բագրատունի</li><li>Սասունցի Դավիթ</li><li>Սահակ Պարթև</li>
<li>Ստեփանոս Շահումյան</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul>
<li>Վահան Մամիկոնյան</li><li>Վրթանես Սրբազան</li><li>Վարդան Մամիկոնյան</li>
<li>Վահան Վիլեմի</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Պ</div>
<ul>
<li>Պարույր Սևակ</li><li>Պապ Գասպարական</li><li>Պողոս Քեչիբեկյան</li>
<li>Պողոս Նուբար Փաշա</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ռ</div>
<ul>
<li>Ռաֆայել Մեծ</li><li>Ռոբերտ Գալստյան</li><li>Ռաֆայել Լեմկին</li>
</ul>
</div>

<hr class="section-divider">
<h4>Տեղանուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Արցախ</li><li>Անդրկովկաս</li><li>Ալավերդի</li><li>Արարատ</li>
<li>Ալեքսանդրապոլ</li><li>Ադրիանապոլիս</li><li>Ախալքալաք</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Բ</div>
<ul><li>Բաթումի</li><li>Բիթլիս</li><li>Բալկանյան</li></ul>
</div>

<div class="letter-section"><div class="letter">Գ</div>
<ul><li>Գետաշեն</li><li>Գանձակ</li></ul>
</div>

<div class="letter-section"><div class="letter">Դ</div>
<ul><li>Դահարան</li><li>Դիլիջան</li><li>Դիարբեքիր</li></ul>
</div>

<div class="letter-section"><div class="letter">Ե</div>
<ul><li>Եվրոպա</li><li>Ելիզավետպոլ</li></ul>
</div>

<div class="letter-section"><div class="letter">Է</div>
<ul><li>Էջմիածին</li><li>Էրզրում</li></ul>
</div>

<div class="letter-section"><div class="letter">Ի</div>
<ul><li>Իսրայել</li><li>Իշխան</li></ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հայաստան</li><li>Հալիձոր</li><li>Հռոմ</li></ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul><li>Վան</li><li>Վաղարշապատ</li><li>Վրաստան</li></ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul><li>Սյունիք</li><li>Սարիղամիշ</li></ul>
</div>

<div class="letter-section"><div class="letter">Տ</div>
<ul><li>Տրապիզոն</li><li>Տարոն</li></ul>
</div>

<hr class="section-divider">
<h4>Պատմական երկրանուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Անգեղակոթ գյուղ</li><li>Ադանայի նահանգ</li></ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul>
<li>Սարդարապատի ջոկատ</li><li>Սուլուխ գյուղ</li>
<li>Սուլթանական կառավարություն</li><li>Սասուն լեռնագավառ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul><li>Վենետիկի հանրապետություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul><li>Կարսի մարզ</li><li>Կովկասի փոխարքայություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Օ</div>
<ul><li>Օսմանյան կայսրություն</li><li>Օսմանյան տերություն</li></ul>
</div>

<hr class="section-divider">
<h4>Մականուններ — մեծատարով</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Արտաշես Արդար</li><li>Աբգար Մեծ</li><li>Աշոտ Երկաթ</li></ul>
</div>
<div class="letter-section"><div class="letter">Բ</div>
<ul><li>Բաբ Բարի</li><li>Բարսեղ Իմաստուն</li></ul>
</div>
<div class="letter-section"><div class="letter">Դ</div>
<ul><li>Դավիթ Բեկ</li><li>Տիրանի Քաջ</li></ul>
</div>
"""
    },

    'hamashkharhayin': {
        'title': 'Համաշխարհային պատմություն',
        'emoji': '🌍',
        'color': '#27ae60',
        'pages': '29–42',
        'content': """
<h3>Հարադրավոր հատուկ անունների բոլոր բաղադրյալները գրվում են մեծատարով</h3>
<h4>Տեղանուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Արևմտյան Փոքր Ասիա</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul><li>Կենտրոնական Ասիա</li></ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հյուսիսային Հնդկաստան</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մեծ Բրիտանիա</li><li>Սանկտ Պետերբուրգ</li></ul>
</div>

<hr class="section-divider">
<h4>Անձնանուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Աբդուլ Համիդ II</li><li>Ալեքսանդր Երկրորդ</li>
<li>Ալեքսանդր Մակեդոնացի</li><li>Ալ-Մուսթասիմ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul><li>Կյուրոս Մեծ</li><li>Կառլոս Հինգերորդ</li></ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հռոմի Պապ</li></ul>
</div>

<div class="letter-section"><div class="letter">Չ</div>
<ul><li>Չինգիզ Խան</li></ul>
</div>

<div class="letter-section"><div class="letter">Պ</div>
<ul><li>Պիպին Կարճահասակ</li></ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul><li>Սուլեյման Կանոնի</li></ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul><li>Վուդրո Վիլսոն</li></ul>
</div>

<hr class="section-divider">
<h4>Առաջին բառը մեծատարով — հարադրավոր անուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Աքեմենյան տերություն</li><li>Արաբական խալիֆայություն</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Բ</div>
<ul><li>Բալկանյան թերակղզի</li></ul>
</div>

<div class="letter-section"><div class="letter">Է</div>
<ul><li>Էգեյան ծով</li></ul>
</div>

<div class="letter-section"><div class="letter">Լ</div>
<ul><li>Լանգոբարդների թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Խ</div>
<ul><li>Խեթական տերություն</li><li>Խորեզմշահերի տերություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul><li>Կորդովայի խալիֆայություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հնդկական օվկիանոս</li><li>Հռոմեական կայսրություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Միջերկրական ծով</li></ul>
</div>

<div class="letter-section"><div class="letter">Ռ</div>
<ul><li>Ռուսական կայսրություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul><li>Սև ծով</li><li>Սելևկյան թագավորություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Օ</div>
<ul><li>Օմայյան խալիֆայություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Ֆ</div>
<ul><li>Ֆաթիմյան խալիֆայություն</li></ul>
</div>

<hr class="section-divider">
<h4>Պարզ հատուկ անուններ — Տեղանուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Ասորեստան</li><li>Անի</li><li>Աղվանք</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Բ</div>
<ul><li>Բաբելոն</li><li>Բաղդադ</li><li>Բենգալիա</li><li>Բիբլոս</li><li>Բրիտանիա</li></ul>
</div>

<div class="letter-section"><div class="letter">Դ</div>
<ul><li>Դերբենդ</li></ul>
</div>

<div class="letter-section"><div class="letter">Ե</div>
<ul><li>Եգիպտոս</li><li>Երուսաղեմ</li></ul>
</div>

<div class="letter-section"><div class="letter">Ի</div>
<ul><li>Իրան</li></ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul><li>Կապադովկիա</li></ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>Հոնկոնգ</li><li>Հունաստան</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մակեդոնիա</li><li>Մեդինա</li><li>Միջագետք</li><li>Մեքքա</li></ul>
</div>

<div class="letter-section"><div class="letter">Ն</div>
<ul><li>Նեպալ</li></ul>
</div>

<div class="letter-section"><div class="letter">Շ</div>
<ul><li>Շվեյցարիա</li></ul>
</div>

<div class="letter-section"><div class="letter">Պ</div>
<ul><li>Պերսեպոլիս</li><li>Պորտուգալիա</li></ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul><li>Սիդոն</li><li>Սիրիա</li></ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul><li>Վիրք</li><li>Վիետնամ</li></ul>
</div>

<div class="letter-section"><div class="letter">Փ</div>
<ul><li>Փարիզ</li></ul>
</div>

<hr class="section-divider">
<h4>Պարզ հատուկ անուններ — Անձնանուններ</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul><li>Ամոն</li></ul>
</div>

<div class="letter-section"><div class="letter">Դ</div>
<ul><li>Դարեհ I</li><li>Դարեհ III</li></ul>
</div>

<div class="letter-section"><div class="letter">Ե</div>
<ul><li>Եկատերինա II</li></ul>
</div>

<div class="letter-section"><div class="letter">Թ</div>
<ul><li>Տեմուչին</li></ul>
</div>

<div class="letter-section"><div class="letter">Լ</div>
<ul><li>Լևոն III</li><li>Լյուդովիկոս</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>Մելիքշահ</li></ul>
</div>

<div class="letter-section"><div class="letter">Ն</div>
<ul><li>Նիկոլայ II</li></ul>
</div>

<div class="letter-section"><div class="letter">Պ</div>
<ul><li>Պետրոս I</li></ul>
</div>

<div class="letter-section"><div class="letter">Ռ</div>
<ul><li>Ռոմանոս III</li></ul>
</div>

<hr class="section-divider">
<h4>Ստեղծագործությունների անուններ (չակերտներով)</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>«Աստղային գիշեր»</li><li>«Ինքնանկար»</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul><li>«Հովանոցով կինը»</li></ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul><li>«Մտածողը»</li><li>«Մարդ-քաղաքը»</li></ul>
</div>

<div class="letter-section"><div class="letter">Ք</div>
<ul><li>«Քիոսի կոտորածը»</li></ul>
</div>

<hr class="section-divider">
<h4>Նոր տեղանուններ — Հարադրավոր</h4>

<div class="letter-section"><div class="letter">Ա</div>
<ul>
<li>Արևելյան Գերմանիա</li><li>Արևելյան Եվրոպա</li>
<li>Ամերիկայի Միացյալ Նահանգներ</li><li>Ադրբեջանի Հանրապետություն</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Բ</div>
<ul><li>Բարձր Հայք</li></ul>
</div>

<div class="letter-section"><div class="letter">Ի</div>
<ul><li>Իտալիայի Հանրապետություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Հ</div>
<ul>
<li>Հյուսիսային Կորեա</li><li>Հարավային Կորեա</li>
<li>Հայաստանի Հանրապետություն</li><li>Հին Հռոմի հանրապետություն</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Չ</div>
<ul><li>Չինաստանի Ժողովրդական Հանրապետություն</li></ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul><li>Վրաստանի Հանրապետություն</li></ul>
</div>
"""
    },'rusac_lezou': {
        'title': 'Ռուսաց լեզու',
        'emoji': '🇷🇺',
        'color': '#2980b9',
        'pages': '43–66',
        'content': """
<h3>Հարադրավոր հատուկ անունների բոլոր բաղադրիչները գրվում են մեծատարով</h3>
<h4>Անձնանուններ</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-ru">Андрей Белый</span><span class="lang-am">Անդրեյ Բելի</span></div>
<div class="bilingual-item"><span class="lang-ru">Александр Грин</span><span class="lang-am">Ալեքսանդր Գրին</span></div>
<div class="bilingual-item"><span class="lang-ru">Александр Пешковский</span><span class="lang-am">Ալեքսանդր Պեշկովսկի</span></div>
<div class="bilingual-item"><span class="lang-ru">Алексей Толстой</span><span class="lang-am">Ալեքսեյ Տոլստոյ</span></div>
<div class="bilingual-item"><span class="lang-ru">Афанасий Фет</span><span class="lang-am">Աֆանասի Ֆետ</span></div>
<div class="bilingual-item"><span class="lang-ru">Антон Чехов</span><span class="lang-am">Անտոն Չեխով</span></div>
<div class="bilingual-item"><span class="lang-ru">Александр Блок</span><span class="lang-am">Ալեքսանդր Բլոկ</span></div>
<div class="bilingual-item"><span class="lang-ru">Анна Коптяева</span><span class="lang-am">Աննա Կոպտյաևա</span></div>
<div class="bilingual-item"><span class="lang-ru">Андрей Битов</span><span class="lang-am">Անդրեյ Բիտով</span></div>
<div class="bilingual-item"><span class="lang-ru">Александр Сергеевич Пушкин</span><span class="lang-am">Ալեքսանդր Սերգեևիչ Պուշկին</span></div>
<div class="bilingual-item"><span class="lang-ru">Антонио Солери</span><span class="lang-am">Անտոնիո Սոլերի</span></div>
<div class="bilingual-item"><span class="lang-ru">Арина Родионова</span><span class="lang-am">Արինա Ռոդիոնովա</span></div>
</div>

<div class="letter-section"><div class="letter">Բ</div>
<ul>
<li>Բորիս Պիլնյակ</li><li>Բորիս Պոլևոյ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Գ</div>
<ul>
<li>Գեորգի Գլադով</li><li>Գեորգի Մարկով</li>
<li>Գևորգ Ստեփանովիչ Գրիգորյան</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Դ</div>
<ul>
<li>Դմիտրի Լիխաչով</li><li>Դավիթ Սասունցի</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ե</div>
<ul><li>Եվգենի Եվտուշենկո</li></ul>
</div>

<div class="letter-section"><div class="letter">Ի</div>
<ul>
<li>Իվան Տուրգենև</li><li>Իլյա Էրենբուրգ</li><li>Իրինա Գրեկովա</li>
<li>Իվան Այվազովսկի</li><li>Իվան Բունին</li><li>Իվան Սիտին</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Լ</div>
<ul>
<li>Լեոնիդ Անդրեև</li><li>Լեոնիդ Լեոնով</li><li>Լև Տոլստոյ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Կ</div>
<ul>
<li>Կոնստանտին Պաուստովսկի</li><li>Կոնստանտին Ֆեդին</li><li>Կորնեյ Չուկովսկի</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Մ</div>
<ul>
<li>Միխայիլ Պրիշվին</li><li>Մարիետա Շահինյան</li><li>Մեսրոպ Մաշտոց</li>
<li>Միշել Լեգրան</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Յ</div>
<ul>
<li>Յուրի Կազակով</li><li>Յուլիա Միխայլովնա</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ն</div>
<ul>
<li>Նիկոլայ Նեկրասով</li><li>Նիկոլայ Դոբրոլյուբով</li><li>Նիկոլայ Տելեշով</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Շ</div>
<ul>
<li>Շարապ Չայկովսկի</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ս</div>
<ul>
<li>Սերգեյ Եսենին</li><li>Սերգեյ Արտամոնով</li><li>Սերգեյ Ակսակով</li>
<li>Սերգեյ Անտոնով</li><li>Սամուիլ Մարշակ</li><li>Սեմյոն Իվանովիչ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Վ</div>
<ul>
<li>Վիլյամ Սարոյան</li><li>Վալտեր Սկոտ</li><li>Վլադիմիր Արսենև</li>
<li>Վալենտին Կավերին</li><li>Վլադիմիր Կորոլենկո</li><li>Վերա Պանովա</li>
<li>Վլադիմիր Ռոզով</li><li>Վլադիմիր Սոլոուխին</li><li>Վլադիմիր Ստեփանով</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Ու</div>
<ul>
<li>Ուոլթ Դիսնեյ</li>
</ul>
</div>

<div class="letter-section"><div class="letter">Օ</div>
<ul>
<li>Օլգա Իվանովնա</li>
</ul>
</div>

<hr class="section-divider">
<h4>Տեղանուններ</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-ru">Башня Биг Бен</span><span class="lang-am">«Բիգ Բեն» աշտարակ</span></div>
<div class="bilingual-item"><span class="lang-ru">Древняя Греция</span><span class="lang-am">Հին Հունաստան</span></div>
<div class="bilingual-item"><span class="lang-ru">Собор Парижской Богоматери</span><span class="lang-am">Փարիզի Աստվածամոր տաճար</span></div>
</div>

<hr class="section-divider">
<h4>Լրացյալը հատուկ անուն չէ (Տեղանուններ)</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-ru">Академия наук</span><span class="lang-am">Գիտությունների ակադեմիա</span></div>
<div class="bilingual-item"><span class="lang-ru">Бюраканская обсерватория</span><span class="lang-am">Բյուրականի աստղադիտարան</span></div>
<div class="bilingual-item"><span class="lang-ru">Ереванский государственный университет</span><span class="lang-am">Երևանի պետական համալսարան</span></div>
<div class="bilingual-item"><span class="lang-ru">Хосровский заповедник</span><span class="lang-am">Խոսրովի արգելոց</span></div>
<div class="bilingual-item"><span class="lang-ru">Китайская фанза</span><span class="lang-am">Չինական տուն (ֆանզա)</span></div>
<div class="bilingual-item"><span class="lang-ru">Михайловский парк</span><span class="lang-am">Միխայլովյան զբոսայգի</span></div>
<div class="bilingual-item"><span class="lang-ru">Петровский парк</span><span class="lang-am">Պետրովյան զբոսայգի</span></div>
<div class="bilingual-item"><span class="lang-ru">Пушкинский заповедник</span><span class="lang-am">Պուշկինյան արգելոց</span></div>
<div class="bilingual-item"><span class="lang-ru">Спасская башня</span><span class="lang-am">Սպասյան աշտարակ</span></div>
<div class="bilingual-item"><span class="lang-ru">Средиземное море</span><span class="lang-am">Միջերկրական ծով</span></div>
<div class="bilingual-item"><span class="lang-ru">Сокольничий парк</span><span class="lang-am">Սոկոլնիկի զբոսայգի</span></div>
<div class="bilingual-item"><span class="lang-ru">Тригорский парк</span><span class="lang-am">Տրիգորսկի զբոսայգի</span></div>
</div>

<hr class="section-divider">
<h4>Ստեղծագործությունների անուններ (չակերտներով)</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-ru">«Девятый вал»</span><span class="lang-am">«Իններորդ ալիք»</span></div>
<div class="bilingual-item"><span class="lang-ru">«Интурист»</span><span class="lang-am">«Ինտուրիստ»</span></div>
<div class="bilingual-item"><span class="lang-ru">«Голос Армении»</span><span class="lang-am">«Գոլոս Արմենիի» (Հայաստանի ձայն)</span></div>
<div class="bilingual-item"><span class="lang-ru">«Надежда»</span><span class="lang-am">«Նադեժդա» (Հույս)</span></div>
<div class="bilingual-item"><span class="lang-ru">«Отцы и дети»</span><span class="lang-am">«Հայրեր և որդիներ»</span></div>
<div class="bilingual-item"><span class="lang-ru">«Энциклопедия»</span><span class="lang-am">«Հանրագիտարան»</span></div>
<div class="bilingual-item"><span class="lang-ru">«Москва»</span><span class="lang-am">«Մոսկվա»</span></div>
<div class="bilingual-item"><span class="lang-ru">«Золотая роза»</span><span class="lang-am">«Ոսկե վարդ»</span></div>
<div class="bilingual-item"><span class="lang-ru">«Война и мир»</span><span class="lang-am">«Պատերազմ և խաղաղություն»</span></div>
<div class="bilingual-item"><span class="lang-ru">«Белоснежка и семь гномов»</span><span class="lang-am">«Սպիտակաձյունիկը և յոթ թզուկները»</span></div>
<div class="bilingual-item"><span class="lang-ru">«Спартак»</span><span class="lang-am">«Սպարտակ»</span></div>
<div class="bilingual-item"><span class="lang-ru">«Руслану и Людмиле»</span><span class="lang-am">«Ռուսլան և Լյուդմիլա»</span></div>
</div>

<hr class="section-divider">
<h4>Պարզ հատուկ անուններ</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-ru">Андерсен</span><span class="lang-am">Անդերսեն</span></div>
<div class="bilingual-item"><span class="lang-ru">Андрей</span><span class="lang-am">Անդրեյ</span></div>
<div class="bilingual-item"><span class="lang-ru">Алёша</span><span class="lang-am">Ալյոշա</span></div>
<div class="bilingual-item"><span class="lang-ru">Гоголь</span><span class="lang-am">Գոգոլ</span></div>
<div class="bilingual-item"><span class="lang-ru">Дарвин</span><span class="lang-am">Դարվին</span></div>
<div class="bilingual-item"><span class="lang-ru">Левитан</span><span class="lang-am">Լևիտան</span></div>
<div class="bilingual-item"><span class="lang-ru">Маруся</span><span class="lang-am">Մարուսյա</span></div>
<div class="bilingual-item"><span class="lang-ru">Наполеон</span><span class="lang-am">Նապոլեոն</span></div>
</div>

<hr class="section-divider">
<h4>Տեղանուններ (պարզ)</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-ru">Азия</span><span class="lang-am">Ասիա</span></div>
<div class="bilingual-item"><span class="lang-ru">Австралия</span><span class="lang-am">Ավստրալիա</span></div>
<div class="bilingual-item"><span class="lang-ru">Гарни</span><span class="lang-am">Գառնի</span></div>
<div class="bilingual-item"><span class="lang-ru">Гегард</span><span class="lang-am">Գեղարդ</span></div>
<div class="bilingual-item"><span class="lang-ru">Гюмри</span><span class="lang-am">Գյումրի</span></div>
<div class="bilingual-item"><span class="lang-ru">Европа</span><span class="lang-am">Եվրոպա</span></div>
<div class="bilingual-item"><span class="lang-ru">Ереван</span><span class="lang-am">Երևան</span></div>
<div class="bilingual-item"><span class="lang-ru">Краков</span><span class="lang-am">Կրակով</span></div>
<div class="bilingual-item"><span class="lang-ru">Лондон</span><span class="lang-am">Լոնդոն</span></div>
<div class="bilingual-item"><span class="lang-ru">Лувр</span><span class="lang-am">Լուվր</span></div>
<div class="bilingual-item"><span class="lang-ru">Москва</span><span class="lang-am">Մոսկվա</span></div>
<div class="bilingual-item"><span class="lang-ru">Матенадаран</span><span class="lang-am">Մատենադարան</span></div>
<div class="bilingual-item"><span class="lang-ru">Париж</span><span class="lang-am">Փարիզ</span></div>
<div class="bilingual-item"><span class="lang-ru">Прага</span><span class="lang-am">Պրահա</span></div>
<div class="bilingual-item"><span class="lang-ru">Варшава</span><span class="lang-am">Վարշավա</span></div>
<div class="bilingual-item"><span class="lang-ru">Тайга</span><span class="lang-am">Տայգա</span></div>
<div class="bilingual-item"><span class="lang-ru">Тауэр</span><span class="lang-am">Տաուեր</span></div>
<div class="bilingual-item"><span class="lang-ru">Франция</span><span class="lang-am">Ֆրանսիա</span></div>
</div>

<hr class="section-divider">
<h4>Ռուսաստան — Պարզ հատուկ անուններ</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-ru">Алтай</span><span class="lang-am">Ալթայ</span></div>
<div class="bilingual-item"><span class="lang-ru">Александр</span><span class="lang-am">Ալեքսանդր</span></div>
<div class="bilingual-item"><span class="lang-ru">Арбат</span><span class="lang-am">Արբատ</span></div>
<div class="bilingual-item"><span class="lang-ru">Батуми</span><span class="lang-am">Բաթումի</span></div>
<div class="bilingual-item"><span class="lang-ru">Болгария</span><span class="lang-am">Բուլղարիա</span></div>
<div class="bilingual-item"><span class="lang-ru">Германия</span><span class="lang-am">Գերմանիա</span></div>
<div class="bilingual-item"><span class="lang-ru">Данко</span><span class="lang-am">Դանկո</span></div>
<div class="bilingual-item"><span class="lang-ru">Европа</span><span class="lang-am">Եվրոպա</span></div>
<div class="bilingual-item"><span class="lang-ru">Иван</span><span class="lang-am">Իվան</span></div>
<div class="bilingual-item"><span class="lang-ru">Ленинград</span><span class="lang-am">Լենինգրադ</span></div>
<div class="bilingual-item"><span class="lang-ru">Константинополь</span><span class="lang-am">Կոստանդնուպոլիս</span></div>
<div class="bilingual-item"><span class="lang-ru">Армения</span><span class="lang-am">Հայաստան</span></div>
<div class="bilingual-item"><span class="lang-ru">Крым</span><span class="lang-am">Ղրիմ</span></div>
<div class="bilingual-item"><span class="lang-ru">Максим</span><span class="lang-am">Մաքսիմ</span></div>
<div class="bilingual-item"><span class="lang-ru">Наполеон</span><span class="lang-am">Նապոլեոն</span></div>
<div class="bilingual-item"><span class="lang-ru">Николай</span><span class="lang-am">Նիկոլայ</span></div>
<div class="bilingual-item"><span class="lang-ru">Пушкин</span><span class="lang-am">Պուշկին</span></div>
<div class="bilingual-item"><span class="lang-ru">Россия</span><span class="lang-am">Ռուսաստան</span></div>
<div class="bilingual-item"><span class="lang-ru">Рим</span><span class="lang-am">Հռոմ</span></div>
<div class="bilingual-item"><span class="lang-ru">Сербия</span><span class="lang-am">Սերբիա</span></div>
<div class="bilingual-item"><span class="lang-ru">Валерий</span><span class="lang-am">Վալերի</span></div>
<div class="bilingual-item"><span class="lang-ru">Вера</span><span class="lang-am">Վերա</span></div>
<div class="bilingual-item"><span class="lang-ru">Воронеж</span><span class="lang-am">Վորոնեժ</span></div>
<div class="bilingual-item"><span class="lang-ru">Париж</span><span class="lang-am">Փարիզ</span></div>
<div class="bilingual-item"><span class="lang-ru">Франция</span><span class="lang-am">Ֆրանսիա</span></div>
</div>

<hr class="section-divider">
<h4>Պետությունների անուններ — բոլոր բաղադրիչները մեծատարով</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-ru">Азербайджанская Республика</span><span class="lang-am">Ադրբեջանի Հանրապետություն</span></div>
<div class="bilingual-item"><span class="lang-ru">Аргентинская Республика</span><span class="lang-am">Արգենտինայի Հանրապետություն</span></div>
<div class="bilingual-item"><span class="lang-ru">Республика Армения</span><span class="lang-am">Հայաստանի Հանրապետություն</span></div>
<div class="bilingual-item"><span class="lang-ru">Республика Беларусь</span><span class="lang-am">Բելառուսի Հանրապետություն</span></div>
<div class="bilingual-item"><span class="lang-ru">Федеративная Республика Германия</span><span class="lang-am">Գերմանիայի Դաշնային Հանրապետություն</span></div>
<div class="bilingual-item"><span class="lang-ru">Греческая Республика</span><span class="lang-am">Հունաստանի Հանրապետություն</span></div>
<div class="bilingual-item"><span class="lang-ru">Соединённое Королевство Великобритании</span><span class="lang-am">Մեծ Բրիտանիայի Միացյալ Թագավորություն</span></div>
<div class="bilingual-item"><span class="lang-ru">Российская Федерация</span><span class="lang-am">Ռուսաստանի Դաշնություն</span></div>
<div class="bilingual-item"><span class="lang-ru">Республика Казахстан</span><span class="lang-am">Ղազախստանի Հանրապետություն</span></div>
<div class="bilingual-item"><span class="lang-ru">Республика Польша</span><span class="lang-am">Լեհաստանի Հանրապետություն</span></div>
<div class="bilingual-item"><span class="lang-ru">Турецкая Республика</span><span class="lang-am">Թուրքիայի Հանրապետություն</span></div>
<div class="bilingual-item"><span class="lang-ru">Чешская Республика</span><span class="lang-am">Չեխիայի Հանրապետություն</span></div>
<div class="bilingual-item"><span class="lang-ru">Швейцарская Конфедерация</span><span class="lang-am">Շվեյցարական Համադաշնություն</span></div>
<div class="bilingual-item"><span class="lang-ru">Соединённые Штаты Америки</span><span class="lang-am">Ամերիկայի Միացյալ Նահանգներ</span></div>
<div class="bilingual-item"><span class="lang-ru">Эстонская Республика</span><span class="lang-am">Էստոնիայի Հանրապետություն</span></div>
</div>
"""
    },

    'angleren': {
        'title': 'Անգլերեն',
        'emoji': '🇬🇧',
        'color': '#1abc9c',
        'pages': '67–99',
        'content': """
<h3>Հարադրավոր հատուկ անունների բոլոր բաղադրիչները գրվում են մեծատարով</h3>
<h4>Անձնանուններ</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">Angela Merkel</span><span class="lang-am">Անգելա Մերկել</span></div>
<div class="bilingual-item"><span class="lang-en">Ardem Patapoutian</span><span class="lang-am">Արդեմ Փաթափության</span></div>
<div class="bilingual-item"><span class="lang-en">Betsy Ross</span><span class="lang-am">Բեթսի Ռոս</span></div>
<div class="bilingual-item"><span class="lang-en">David Julius</span><span class="lang-am">Դևիդ Ջուլիուս</span></div>
<div class="bilingual-item"><span class="lang-en">David Ogilvy</span><span class="lang-am">Դևիդ Օգիլվի</span></div>
<div class="bilingual-item"><span class="lang-en">Doctor Julius</span><span class="lang-am">դոկտոր Ջուլիուս</span></div>
<div class="bilingual-item"><span class="lang-en">Doctor Park</span><span class="lang-am">դոկտոր Փարկ</span></div>
<div class="bilingual-item"><span class="lang-en">Doctor Patapoutian</span><span class="lang-am">դոկտոր Փաթափության</span></div>
<div class="bilingual-item"><span class="lang-en">Elizabeth 2nd</span><span class="lang-am">Եղիսաբեթ 2-րդ</span></div>
<div class="bilingual-item"><span class="lang-en">Thomas Perlman</span><span class="lang-am">Թոմաս Պերլման</span></div>
<div class="bilingual-item"><span class="lang-en">Levon Ter-Petrosyan</span><span class="lang-am">Լևոն Տեր-Պետրոսյան</span></div>
<div class="bilingual-item"><span class="lang-en">Liz Adamyan</span><span class="lang-am">Լիզ Ադամյան</span></div>
<div class="bilingual-item"><span class="lang-en">King Charles 3rd</span><span class="lang-am">Թագավոր Չարլզ 3-րդ</span></div>
<div class="bilingual-item"><span class="lang-en">Hamlet Baldryan</span><span class="lang-am">Համլետ Բալդրյան</span></div>
<div class="bilingual-item"><span class="lang-en">Mane Baghdasaryan</span><span class="lang-am">Մանե Բաղդասարյան</span></div>
<div class="bilingual-item"><span class="lang-en">Margaret Thatcher</span><span class="lang-am">Մարգարետ Թետչեր</span></div>
<div class="bilingual-item"><span class="lang-en">Martin Luther King Jr</span><span class="lang-am">Մարտին Լյութեր Քինգ կրտսեր</span></div>
<div class="bilingual-item"><span class="lang-en">Miss Benson</span><span class="lang-am">օրիորդ Բենսոն</span></div>
<div class="bilingual-item"><span class="lang-en">Minister Petrosyan</span><span class="lang-am">նախարար Պետրոսյան</span></div>
<div class="bilingual-item"><span class="lang-en">Mister Green</span><span class="lang-am">պարոն Գրին</span></div>
<div class="bilingual-item"><span class="lang-en">Mister Oliver</span><span class="lang-am">պարոն Օլիվեր</span></div>
<div class="bilingual-item"><span class="lang-en">Mister Petrosyan</span><span class="lang-am">պարոն Պետրոսյան</span></div>
<div class="bilingual-item"><span class="lang-en">Nelson Mandela</span><span class="lang-am">Նելսոն Մանդելա</span></div>
<div class="bilingual-item"><span class="lang-en">President Harry S. Truman</span><span class="lang-am">Նախագահ Հարրի Ս. Թրուման</span></div>
<div class="bilingual-item"><span class="lang-en">Jim Rohn</span><span class="lang-am">Ջիմ Ռոն</span></div>
<div class="bilingual-item"><span class="lang-en">George Clinton</span><span class="lang-am">Ջորջ Քլինթոն</span></div>
<div class="bilingual-item"><span class="lang-en">Robert Kelley</span><span class="lang-am">Ռոբերտ Քելի</span></div>
<div class="bilingual-item"><span class="lang-en">Saro Zargaryan</span><span class="lang-am">Սարո Զարգարյան</span></div>
<div class="bilingual-item"><span class="lang-en">Steve Jobs</span><span class="lang-am">Սթիվ Ջոբս</span></div>
<div class="bilingual-item"><span class="lang-en">William Driver</span><span class="lang-am">Ուիլյամ Դրայվեր</span></div>
<div class="bilingual-item"><span class="lang-en">Francis Hopkinson</span><span class="lang-am">Ֆրենսիս Հոփկինսոն</span></div>
<div class="bilingual-item"><span class="lang-en">Francis Scott Key</span><span class="lang-am">Ֆրենսիս Սքոթ Քի</span></div>
</div>
<hr class="section-divider">
<h4>Տեղանուններ</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">La Jolla</span><span class="lang-am">Լա Հոյա</span></div>
<div class="bilingual-item"><span class="lang-en">Mazmanyan Street</span><span class="lang-am">Մազմանյան փողոց</span></div>
<div class="bilingual-item"><span class="lang-en">US / United States</span><span class="lang-am">ԱՄՆ / Միացյալ Նահանգներ</span></div>
<div class="bilingual-item"><span class="lang-en">United Kingdom / Great Britain</span><span class="lang-am">Միացյալ Թագավորություն / Մեծ Բրիտանիա</span></div>
<div class="bilingual-item"><span class="lang-en">North America</span><span class="lang-am">Հյուսիսային Ամերիկա</span></div>
<div class="bilingual-item"><span class="lang-en">Northern Ireland</span><span class="lang-am">Հյուսիսային Իռլանդիա</span></div>
<div class="bilingual-item"><span class="lang-en">Nagorno-Karabakh</span><span class="lang-am">Լեռնային Ղարաբաղ</span></div>
<div class="bilingual-item"><span class="lang-en">South Africa</span><span class="lang-am">Հարավային Աֆրիկա</span></div>
<div class="bilingual-item"><span class="lang-en">South America</span><span class="lang-am">Հարավային Ամերիկա</span></div>
<div class="bilingual-item"><span class="lang-en">Soviet Union</span><span class="lang-am">Խորհրդային Միություն</span></div>
<div class="bilingual-item"><span class="lang-en">Washington DC</span><span class="lang-am">Վաշինգտոն Կ.Հ.</span></div>
</div>

<hr class="section-divider">
<h4>Կազմակերպությունների անուններ</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">Commonwealth of Nations (CWN)</span><span class="lang-am">Ազգերի համագործակցություն</span></div>
<div class="bilingual-item"><span class="lang-en">United States Government</span><span class="lang-am">ԱՄՆ կառավարություն</span></div>
<div class="bilingual-item"><span class="lang-en">National Assembly</span><span class="lang-am">Ազգային ժողով</span></div>
<div class="bilingual-item"><span class="lang-en">National Museum of American History</span><span class="lang-am">Ամերիկյան պատմության ազգային թանգարան</span></div>
<div class="bilingual-item"><span class="lang-en">Supreme Court</span><span class="lang-am">Գերագույն դատարան</span></div>
<div class="bilingual-item"><span class="lang-en">European Union (EU)</span><span class="lang-am">Եվրոպական միություն</span></div>
<div class="bilingual-item"><span class="lang-en">House of Lords</span><span class="lang-am">Լորդերի պալատ</span></div>
<div class="bilingual-item"><span class="lang-en">Parliament</span><span class="lang-am">Խորհրդարան</span></div>
<div class="bilingual-item"><span class="lang-en">Congress</span><span class="lang-am">Կոնգրես</span></div>
<div class="bilingual-item"><span class="lang-en">Constitution of Armenia</span><span class="lang-am">Հայաստանի Սահմանադրություն</span></div>
<div class="bilingual-item"><span class="lang-en">House of Commons</span><span class="lang-am">Համայնքների պալատ</span></div>
<div class="bilingual-item"><span class="lang-en">Howard Hughes Medical Institute</span><span class="lang-am">Հովարդ Հյուզի բժշկական ինստիտուտ</span></div>
<div class="bilingual-item"><span class="lang-en">NATO</span><span class="lang-am">Հյուսիսատլանտյան դաշինք</span></div>
<div class="bilingual-item"><span class="lang-en">Republic of Armenia</span><span class="lang-am">Հայաստանի Հանրապետություն</span></div>
<div class="bilingual-item"><span class="lang-en">United Nations (UN)</span><span class="lang-am">Միավորված ազգերի կազմակերպություն</span></div>
<div class="bilingual-item"><span class="lang-en">Microsoft Excel</span><span class="lang-am">Մայքրոսոֆթ Էքսել</span></div>
<div class="bilingual-item"><span class="lang-en">The White House</span><span class="lang-am">Սպիտակ տուն</span></div>
</div>

<hr class="section-divider">
<h4>Ստեղծագործությունների անուններ (չակերտներով)</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">«Amulsar Gold Quartzite Mining»</span><span class="lang-am">«Ամուլսարի ոսկու կվարցիտային հանքավայրի շահագործում»</span></div>
<div class="bilingual-item"><span class="lang-en">«Gulliver's Travels»</span><span class="lang-am">«Գուլիվերի ճանապարհորդությունները»</span></div>
<div class="bilingual-item"><span class="lang-en">«The Picture Of Dorian Gray»</span><span class="lang-am">«Դորիան Գրեյի դիմանկարը»</span></div>
<div class="bilingual-item"><span class="lang-en">«If»</span><span class="lang-am">«Եթե»</span></div>
<div class="bilingual-item"><span class="lang-en">«Alone»</span><span class="lang-am">«Միայնակ»</span></div>
<div class="bilingual-item"><span class="lang-en">«The seven ages of man»</span><span class="lang-am">«Մարդու յոթ տարիքները»</span></div>
<div class="bilingual-item"><span class="lang-en">«We Are Few But We Are Called Armenians»</span><span class="lang-am">«Մենք քիչ ենք, սակայն մեզ հայ են ասում»</span></div>
<div class="bilingual-item"><span class="lang-en">«Gone With The Wind»</span><span class="lang-am">«Քամուց քշվածները»</span></div>
</div>

<hr class="section-divider">
<h4>Լրացյալը հատուկ անուն չէ (Տեղանուններ)</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">«Artsvanic Tailings Dump»</span><span class="lang-am">«Արծվանիկի պոչամբար»</span></div>
<div class="bilingual-item"><span class="lang-en">«Bermuda Triangle»</span><span class="lang-am">«Բերմուդյան եռանկյունի»</span></div>
<div class="bilingual-item"><span class="lang-en">«Pacific Ocean»</span><span class="lang-am">«Խաղաղ օվկիանոս»</span></div>
<div class="bilingual-item"><span class="lang-en">«Lake Sevan»</span><span class="lang-am">«Սևանա լիճ»</span></div>
<div class="bilingual-item"><span class="lang-en">«Mother Teresa»</span><span class="lang-am">«Մայր Թերեզա»</span></div>
<div class="bilingual-item"><span class="lang-en">«Tigranes the Great»</span><span class="lang-am">«Տիգրան Մեծ»</span></div>
</div>

<hr class="section-divider">
<h4>Պատմական իրադարձություններ</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">«World War I»</span><span class="lang-am">«Առաջին համաշխարհային պատերազմ»</span></div>
<div class="bilingual-item"><span class="lang-en">«World War II»</span><span class="lang-am">«Երկրորդ համաշխարհային պատերազմ»</span></div>
<div class="bilingual-item"><span class="lang-en">«The Great Patriotic War»</span><span class="lang-am">«Հայրենական մեծ պատերազմ»</span></div>
<div class="bilingual-item"><span class="lang-en">«The Battle of Sarikhamish»</span><span class="lang-am">«Սարիղամիշի ճակատամարտ»</span></div>
<div class="bilingual-item"><span class="lang-en">«March 8»</span><span class="lang-am">«Մարտի 8»</span></div>
<div class="bilingual-item"><span class="lang-en">«New Year»</span><span class="lang-am">«Ամանոր»</span></div>
</div>

<hr class="section-divider">
<h4>Մրցանակներ և շքանշաններ</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">Grammy</span><span class="lang-am">Գրեմմի</span></div>
<div class="bilingual-item"><span class="lang-en">Nobel Peace Prize</span><span class="lang-am">Խաղաղության Նոբելյան մրցանակ</span></div>
<div class="bilingual-item"><span class="lang-en">Oscar</span><span class="lang-am">Օսկար</span></div>
</div>

<hr class="section-divider">
<h4>Հապավումներ</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">FBI (Federal Bureau of Investigation)</span><span class="lang-am">ՀԴԲ (Հետաքննությունների դաշնային բյուրո)</span></div>
<div class="bilingual-item"><span class="lang-en">USA (United States of America)</span><span class="lang-am">ԱՄՆ (Ամերիկայի Միացյալ Նահանգներ)</span></div>
<div class="bilingual-item"><span class="lang-en">ISS (International Space Station)</span><span class="lang-am">ՄՏԿ (Միջազգային տիեզերակայան)</span></div>
<div class="bilingual-item"><span class="lang-en">UK (United Kingdom)</span><span class="lang-am">ՄԹ (Միացյալ Թագավորություն)</span></div>
<div class="bilingual-item"><span class="lang-en">UN (United Nations)</span><span class="lang-am">ՄԱԿ (Միավորված ազգերի կազմակերպություն)</span></div>
<div class="bilingual-item"><span class="lang-en">NATO</span><span class="lang-am">ՆԱՏՕ (Հյուսիսատլանտյան դաշինքի կազմակերպություն)</span></div>
<div class="bilingual-item"><span class="lang-en">NASA</span><span class="lang-am">ՆԱՍԱ (Օդագնացության և տիեզերական տարածության հետազոտությունների ազգային վարչություն)</span></div>
</div>

<hr class="section-divider">
<h4>Մոլորակներ, գալակտիկաներ, աստղեր</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">Solar System</span><span class="lang-am">Արեգակնային համակարգ</span></div>
<div class="bilingual-item"><span class="lang-en">Earth</span><span class="lang-am">Երկիր</span></div>
<div class="bilingual-item"><span class="lang-en">Mercury</span><span class="lang-am">Մերկուրի</span></div>
<div class="bilingual-item"><span class="lang-en">Mars</span><span class="lang-am">Մարս</span></div>
<div class="bilingual-item"><span class="lang-en">Jupiter</span><span class="lang-am">Յուպիտեր</span></div>
<div class="bilingual-item"><span class="lang-en">Neptune</span><span class="lang-am">Նեպտուն</span></div>
<div class="bilingual-item"><span class="lang-en">Pluto</span><span class="lang-am">Պլուտոն</span></div>
<div class="bilingual-item"><span class="lang-en">Saturn</span><span class="lang-am">Սատուրն</span></div>
<div class="bilingual-item"><span class="lang-en">Venus</span><span class="lang-am">Վեներա</span></div>
<div class="bilingual-item"><span class="lang-en">Uranus</span><span class="lang-am">Ուրան</span></div>
<div class="bilingual-item"><span class="lang-en">Moon</span><span class="lang-am">Լուսին</span></div>
<div class="bilingual-item"><span class="lang-en">Sun</span><span class="lang-am">Արեգակ</span></div>
</div>

<hr class="section-divider">
<h4>Հարադրավոր — բոլոր բաղադրյալները մեծատարով</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">Adolf Hitler</span><span class="lang-am">Ադոլֆ Հիտլեր</span></div>
<div class="bilingual-item"><span class="lang-en">Alexander the Great</span><span class="lang-am">Ալեքսանդր Մակեդոնացի</span></div>
<div class="bilingual-item"><span class="lang-en">Abraham Lincoln</span><span class="lang-am">Աբրահամ Լինքոլն</span></div>
<div class="bilingual-item"><span class="lang-en">Elon Musk</span><span class="lang-am">Իլոն Մասկ</span></div>
<div class="bilingual-item"><span class="lang-en">Louis Armstrong</span><span class="lang-am">Լուի Արմսթրոնգ</span></div>
<div class="bilingual-item"><span class="lang-en">Julius Caesar</span><span class="lang-am">Հուլիոս Կեսար</span></div>
<div class="bilingual-item"><span class="lang-en">Victoria Burnzyan</span><span class="lang-am">Վիկտորյա Բուռնազյան</span></div>
<div class="bilingual-item"><span class="lang-en">Srap Gevorgyan</span><span class="lang-am">Սրապ Գևորգյան</span></div>
<div class="bilingual-item"><span class="lang-en">Sara Teasdale</span><span class="lang-am">Սառա Թիսդեյլ</span></div>
<div class="bilingual-item"><span class="lang-en">William Shakespeare</span><span class="lang-am">Ուիլյամ Շեքսպիր</span></div>
<div class="bilingual-item"><span class="lang-en">Michael Jackson</span><span class="lang-am">Մայքլ Ջեքսոն</span></div>
<div class="bilingual-item"><span class="lang-en">Martin Luther King</span><span class="lang-am">Մարտին Լյութեր Քինգ</span></div>
<div class="bilingual-item"><span class="lang-en">Malala Yousafzai</span><span class="lang-am">Մալալա Յուսուֆզայ</span></div>
<div class="bilingual-item"><span class="lang-en">Moses of Khoren</span><span class="lang-am">Մովսես Խորենացի</span></div>
<div class="bilingual-item"><span class="lang-en">Johannes Kepler</span><span class="lang-am">Յոհան Կեպլեր</span></div>
<div class="bilingual-item"><span class="lang-en">Yuri Gagarin</span><span class="lang-am">Յուրի Գագարին</span></div>
<div class="bilingual-item"><span class="lang-en">Napoleon Bonaparte</span><span class="lang-am">Նապոլեոն Բոնապարտ</span></div>
<div class="bilingual-item"><span class="lang-en">Neil Armstrong</span><span class="lang-am">Նիլ Արմսթրոնգ</span></div>
<div class="bilingual-item"><span class="lang-en">Charles Darwin</span><span class="lang-am">Չարլզ Դարվին</span></div>
</div>

<hr class="section-divider">
<h4>Տեղանուններ — հարադրավոր</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">Eastern Anatolia</span><span class="lang-am">Արևելյան Անատոլիա</span></div>
<div class="bilingual-item"><span class="lang-en">United Arab Emirates</span><span class="lang-am">Արաբական Միացյալ Էմիրություններ</span></div>
<div class="bilingual-item"><span class="lang-en">Republic of Armenia</span><span class="lang-am">Հայաստանի Հանրապետություն</span></div>
<div class="bilingual-item"><span class="lang-en">Ancient Greece</span><span class="lang-am">Հին Հունաստան</span></div>
<div class="bilingual-item"><span class="lang-en">South Korea</span><span class="lang-am">Հարավային Կորեա</span></div>
<div class="bilingual-item"><span class="lang-en">North Korea</span><span class="lang-am">Հյուսիսային Կորեա</span></div>
<div class="bilingual-item"><span class="lang-en">North Macedonia</span><span class="lang-am">Հյուսիսային Մակեդոնիա</span></div>
<div class="bilingual-item"><span class="lang-en">South Africa</span><span class="lang-am">Հարավային Աֆրիկա</span></div>
<div class="bilingual-item"><span class="lang-en">United Kingdom</span><span class="lang-am">Միացյալ Թագավորություն</span></div>
</div>

<hr class="section-divider">
<h4>Կանոն — Անգլերենի և Հայերենի տարբերություններ</h4>

<div class="rule-box">
<p><strong>Կանոն.</strong> Անգլերենում առանձին բառեր հատուկ անուններ են համարվում, սակայն հայերենում՝ ոչ: Օրերը, շաբաթները, ամիսները, պատմական անցքերը, ազգություններն ու կրոններն անգլերենում մեծատարով են գրվում, հայերենում՝ փոքրատարով:</p>
</div>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">Monday</span><span class="lang-am">երկուշաբթի</span></div>
<div class="bilingual-item"><span class="lang-en">Tuesday</span><span class="lang-am">երեքշաբթի</span></div>
<div class="bilingual-item"><span class="lang-en">Wednesday</span><span class="lang-am">չորեքշաբթի</span></div>
<div class="bilingual-item"><span class="lang-en">Thursday</span><span class="lang-am">հինգշաբթի</span></div>
<div class="bilingual-item"><span class="lang-en">Friday</span><span class="lang-am">ուրբաթ</span></div>
<div class="bilingual-item"><span class="lang-en">Saturday</span><span class="lang-am">շաբաթ</span></div>
<div class="bilingual-item"><span class="lang-en">Sunday</span><span class="lang-am">կիրակի</span></div>
<div class="bilingual-item"><span class="lang-en">January</span><span class="lang-am">հունվար</span></div>
<div class="bilingual-item"><span class="lang-en">June</span><span class="lang-am">հունիս</span></div>
<div class="bilingual-item"><span class="lang-en">July</span><span class="lang-am">հուլիս</span></div>
<div class="bilingual-item"><span class="lang-en">August</span><span class="lang-am">օգոստոս</span></div>
<div class="bilingual-item"><span class="lang-en">September</span><span class="lang-am">սեպտեմբեր</span></div>
<div class="bilingual-item"><span class="lang-en">November</span><span class="lang-am">նոյեմբեր</span></div>
<div class="bilingual-item"><span class="lang-en">Armenian</span><span class="lang-am">հայ</span></div>
<div class="bilingual-item"><span class="lang-en">Italian</span><span class="lang-am">իտալացի</span></div>
<div class="bilingual-item"><span class="lang-en">Spanish</span><span class="lang-am">իսպանացի</span></div>
<div class="bilingual-item"><span class="lang-en">French</span><span class="lang-am">ֆրանսիացի</span></div>
<div class="bilingual-item"><span class="lang-en">American</span><span class="lang-am">ամերիկացի</span></div>
<div class="bilingual-item"><span class="lang-en">Greek</span><span class="lang-am">հույն</span></div>
<div class="bilingual-item"><span class="lang-en">Kurd</span><span class="lang-am">քուրդ</span></div>
<div class="bilingual-item"><span class="lang-en">English</span><span class="lang-am">անգլերեն</span></div>
<div class="bilingual-item"><span class="lang-en">German</span><span class="lang-am">գերմաներեն</span></div>
<div class="bilingual-item"><span class="lang-en">Russian</span><span class="lang-am">ռուսերեն</span></div>
<div class="bilingual-item"><span class="lang-en">Chinese</span><span class="lang-am">չինարեն</span></div>
</div>

<hr class="section-divider">
<h4>Պարզ հատուկ անուններ (Անձնանուններ)</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">Albert</span><span class="lang-am">Ալբերտ</span></div>
<div class="bilingual-item"><span class="lang-en">Anna</span><span class="lang-am">Աննա</span></div>
<div class="bilingual-item"><span class="lang-en">Anush</span><span class="lang-am">Անուշ</span></div>
<div class="bilingual-item"><span class="lang-en">Aram</span><span class="lang-am">Արամ</span></div>
<div class="bilingual-item"><span class="lang-en">Aristotle</span><span class="lang-am">Արիստոտել</span></div>
<div class="bilingual-item"><span class="lang-en">Ben</span><span class="lang-am">Բեն</span></div>
<div class="bilingual-item"><span class="lang-en">Gohar</span><span class="lang-am">Գոհար</span></div>
<div class="bilingual-item"><span class="lang-en">Daniel</span><span class="lang-am">Դանիել</span></div>
<div class="bilingual-item"><span class="lang-en">David</span><span class="lang-am">Դևիդ</span></div>
<div class="bilingual-item"><span class="lang-en">Ella</span><span class="lang-am">Էլլա</span></div>
<div class="bilingual-item"><span class="lang-en">Emma</span><span class="lang-am">Էմմա</span></div>
<div class="bilingual-item"><span class="lang-en">Tom</span><span class="lang-am">Թոմ</span></div>
<div class="bilingual-item"><span class="lang-en">Lana</span><span class="lang-am">Լանա</span></div>
<div class="bilingual-item"><span class="lang-en">Lucy</span><span class="lang-am">Լյուսի</span></div>
<div class="bilingual-item"><span class="lang-en">Harvey</span><span class="lang-am">Հարվի</span></div>
<div class="bilingual-item"><span class="lang-en">Harry</span><span class="lang-am">Հարրի</span></div>
<div class="bilingual-item"><span class="lang-en">Mary</span><span class="lang-am">Մերի</span></div>
<div class="bilingual-item"><span class="lang-en">Mariam</span><span class="lang-am">Մարիամ</span></div>
<div class="bilingual-item"><span class="lang-en">Nina</span><span class="lang-am">Նինա</span></div>
<div class="bilingual-item"><span class="lang-en">Charlotte</span><span class="lang-am">Շարլոտ</span></div>
<div class="bilingual-item"><span class="lang-en">Picasso</span><span class="lang-am">Պիկասո</span></div>
<div class="bilingual-item"><span class="lang-en">George</span><span class="lang-am">Ջորջ</span></div>
<div class="bilingual-item"><span class="lang-en">Jack</span><span class="lang-am">Ջեք</span></div>
<div class="bilingual-item"><span class="lang-en">Sam</span><span class="lang-am">Սեմ</span></div>
<div class="bilingual-item"><span class="lang-en">Sarah</span><span class="lang-am">Սառա</span></div>
<div class="bilingual-item"><span class="lang-en">Peter</span><span class="lang-am">Փիթեր</span></div>
<div class="bilingual-item"><span class="lang-en">Carol</span><span class="lang-am">Քերոլ</span></div>
<div class="bilingual-item"><span class="lang-en">Fiona</span><span class="lang-am">Ֆիոնա</span></div>
</div>

<hr class="section-divider">
<h4>Տեղանուններ (պարզ)</h4>

<div class="bilingual-list">
<div class="bilingual-item"><span class="lang-en">Arlington</span><span class="lang-am">Առլինգտոն</span></div>
<div class="bilingual-item"><span class="lang-en">Asia</span><span class="lang-am">Ասիա</span></div>
<div class="bilingual-item"><span class="lang-en">Baltimore</span><span class="lang-am">Բալթիմոր</span></div>
<div class="bilingual-item"><span class="lang-en">Germany</span><span class="lang-am">Գերմանիա</span></div>
<div class="bilingual-item"><span class="lang-en">Gyumri</span><span class="lang-am">Գյումրի</span></div>
<div class="bilingual-item"><span class="lang-en">Yerevan</span><span class="lang-am">Երևան</span></div>
<div class="bilingual-item"><span class="lang-en">Europe</span><span class="lang-am">Եվրոպա</span></div>
<div class="bilingual-item"><span class="lang-en">Italy</span><span class="lang-am">Իտալիա</span></div>
<div class="bilingual-item"><span class="lang-en">California</span><span class="lang-am">Կալիֆոռնիա</span></div>
<div class="bilingual-item"><span class="lang-en">Armenia</span><span class="lang-am">Հայաստան</span></div>
<div class="bilingual-item"><span class="lang-en">Rome</span><span class="lang-am">Հռոմ</span></div>
<div class="bilingual-item"><span class="lang-en">Japan</span><span class="lang-am">Ճապոնիա</span></div>
<div class="bilingual-item"><span class="lang-en">Maryland</span><span class="lang-am">Մերիլենդ</span></div>
<div class="bilingual-item"><span class="lang-en">Scotland</span><span class="lang-am">Շոտլանդիա</span></div>
<div class="bilingual-item"><span class="lang-en">Russia</span><span class="lang-am">Ռուսաստան</span></div>
<div class="bilingual-item"><span class="lang-en">Virginia</span><span class="lang-am">Վիրջինիա</span></div>
<div class="bilingual-item"><span class="lang-en">Tennessee</span><span class="lang-am">Տենեսի</span></div>
<div class="bilingual-item"><span class="lang-en">Tokyo</span><span class="lang-am">Տոկիո</span></div>
<div class="bilingual-item"><span class="lang-en">Philadelphia</span><span class="lang-am">Ֆիլադելֆիա</span></div>
<div class="bilingual-item"><span class="lang-en">Pennsylvania</span><span class="lang-am">Փենսիլվանիա</span></div>
<div class="bilingual-item"><span class="lang-en">Wales</span><span class="lang-am">Ուելս</span></div>
</div>
"""
    }
}

# ============================================================
# Роутинг Flask (Flask routes)
# ============================================================

@app.route('/')
def index():
    return render_template('index.html', intro=INTRO, sections=SECTIONS)

@app.route('/section/<section_id>')
def section(section_id):
    if section_id not in SECTIONS:
        return "Բաժինը չի գտնվել", 404
    return render_template(
        'section.html',
        section=SECTIONS[section_id],
        section_id=section_id,
        sections=SECTIONS
    )

if __name__ == '__main__':
    app.run(debug=True)
