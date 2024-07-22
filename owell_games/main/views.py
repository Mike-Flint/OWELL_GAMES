from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def main(request):
    return render(request,"main/main.html", list["en"])

def languageSite(request,lang):
    global list
    print(lang)
    if lang.lower() in ["en","ua"]:
        print("sdfsd")
        return render(request,"main/main.html", list[lang.lower()])

    else:
        return render(request,"main/main.html", list["en"])

class MainAPILanguage(APIView):
    global list
    def get(self, request, lang):
        #["en","ua","fv","cn","es","in","kr","pl","tr","de","br","jp","it"]
        if lang.lower() in ["en","ua"]:
            print(lang)
            return Response(list[lang.lower()])
            
        return Response(list["en"])

list = {
    "ua" : {
        "lng" : "Ua",
        "About_us" : "Про нас",
        "owell_games" : "Owell games це українська команда розробки ігор. Яка зацікавленна в максимальній продуктивності та прекрасному результаті який принесе радість нашім гравцям. ",
        "more_about_us" : "Більше про нас",
        "subheader_history" : "ПОЧНЕМО НАШУ ІСТОРІЮ",
        "history" : "Команда Owell Games була зібрана Томом Овеллом в 2024 році. І починалась лише з Українських розробників. Першим проектом Owell Games важається Samurai Honor. Через деякий час же в результаті перемовин Том Овелл зміг отримати матеріали його не випущеної гри Box Storm. І нині обидва проекти активно опрацьовуються командою і сподіваються на великий потенціал проекту.",
        "subheader_idea" : "НАШІ ІДЕЇ",
        "idea" : "На сьогоднішній день нам очевидний той факт що без ідеї, ні один проект не досягне свого максимуму. Нехай ми і лише починаємо але навіть зараз в нас є ідеї і цілі на які ми націленні.",
        "subheader_platform" : "ПЛАТФОРМИ",
        "platform" : "На нашу думку, ігри мають бути доступні і тому будуть знаходитись на найдоступніших платформах, і будуть лише розширюватись. ",
        "platform_b" : "“Ваша зручність - наш пріоритет”",
        "subheader_language" : "МОВИ",
        "language" : "Інтерфейс і текст дуже важливий аспект ігрового процесу. Тому ми зацікавленні в тому аби вам було зручно грати в наші ігри на своїй рідній мові.",
        "subheader_community" : "СПІЛЬНОТА",
        "community" : "Наші ігри створенні в першу чергу для того аби дарувати нові та позитивні емоції. Тому ми готові слухати вас  та виправляти або додавати ті аспекти які покращать ваш ігровий досвід.",
        "subheader_convenience" : "ЗРУЧНІСТЬ - ПРІОРІТЕТ ЧОМУ?",
        "convenience" : "В нашій команді зручність ігрового досвіду та зручність в створенні є пріоритетом. Але чому саме зручність? Причина проста. Коли вам зручно ви можете отримувати оптимальний ігровий досвід. Коли зручно нам в розробці то ми по скоріше зможемо надати вам новий якісний проект. Тому нашим основним пріоритетом є саме зручність. Наші перші думки завжди “А чи буде гравцю зручно так грати?”. Або як приклад в розробці цього сайту були думки “А чи буде зручно користувачу читати інформацію? А чи буде зручно програмісту створювати наш дизайн?”. Вирішувати вже вам, наскільки якісно ми зробили нашу роботу.",
        "subheader_convenience_mb":"ЗРУЧНІСТЬ - ПРІОРІТЕТ ЧОМУ?",
        "convenience_mb" : "В нашій команді зручність ігрового досвіду та зручність в створенні є пріоритетом.  Але чому саме зручність? Причина проста. Коли вам зручно ви можете отримувати оптимальний ігровий досвід. Коли зручно нам в розробці то ми по скоріше зможемо надати вам новий якісний проект. Тому нашим основним пріоритетом є саме зручність.",
        "subheader_comfort_mb" : "МИ ДУМАЄМО ПРО КОМФОРТ",
        "comfort_mb" : "Наші перші думки завжди “А чи буде гравцю зручно так грати?”. Або як приклад в розробці цього сайту були думки “А чи буде зручно користувачу читати інформацію? А чи буде зручно програмісту створювати наш дизайн?”. Вирішувати вже вам, наскільки якісно ми зробили нашу роботу.",
        "subheader_projects" : "НАШІ АКТУАЛЬНІ ПРОЕКТИ",
        "projects" : "Наша команда активно працює над різними проектами. Нижче ви можете побачити актуальні проекти які ми підтримуємо або розробляємо.",
        "BS" : "Box storm. Це проект який почав свою розробку ще в січні 2024 року. Але через розбіжності поглядів Тома Овелла та його колеги проект було закрито. Через пів року Том створив свій проект Owell Games. І зміг повернути Box Storm. Який  зараз активно дороблюється та готується до виходу.",
        "more_about_BS" : "Детальніше про Box Storm",
        "SH" : "Samurai Honor. Дебютний проект Owell Games. В який було вкладенно дуже багато сил. І нехай Samurai Honor і є початковою точкою для Owell Games. Кожний з участників відається для проекту на всі 100%. В намагані створити для вас такий ігровий досвід який зможе принести для вас гарні та позитивні емоції! ",
        "more_about_SH" : "Детальніше про Samurai Honor"
    },
    "en" : {
        "lng" : "En",
        "About_us" : "About us",
        "owell_games" : "Owell games is a Ukrainian team game development team. Which is is interested in maximizing productivity and excellent results that will bring joy to our players. ",
        "more_about_us" : "More about us",
        "subheader_history" : "START OUR HISTORY",
        "history" : "The Owell Games team was assembled by Tom Owell in 2024. It started with Ukrainian developers only. The first project of Owell Games was Samurai Honor. After a while, as a result of negotiations, Tom Owell was able to get the materials of his unreleased game Box Storm. And now both projects are being actively worked on by the team and they hope for a great potential of the project.",
        "subheader_idea" : "OUR IDEAS",
        "idea" : "Today, it is obvious to us that fact that without an idea, no project will reach its maximum potential. Even though we are just starting out but even now we have ideas and goals that we are aiming at.",
        "subheader_platform" : "PLATFORMS",
        "platform" : "We believe that games should be be accessible and therefore will be be on the most accessible platforms, and will only expanding.",
        "platform_b" : "“Your convenience is our priority”",
        "subheader_language" : "LANGUAGES",
        "language" : "The interface and text are very important aspect of the game process. That's why we are interested in making it convenient for you to play our games in your native language.",
        "subheader_community" : "COMMUNITY",
        "community" : "Our games are created primarily and foremost to give new and positive emotions. That's why we are ready to listen to you  and correct or add those aspects that will improve your gaming experience.",
        "subheader_convenience" : "CONVENIENCE IS A PRIORITY WHY?",
        "convenience" : "In our team, the convenience of the gaming experience and the ease of in creation is a priority for us.  But why convenience? The reason is simple. When you are comfortable, you can get optimal gaming experience. When it is convenient for us in development we can provide you with a new high-quality project. Therefore, our main priority is is convenience. Our first thought is always “Will the player will it be convenient for the player to play this way?”. Or as an example, when developing this website, we thought, “Will it be convenient for the user to read the information? Will it be convenient for the programmer to create our design?”. It is up to you to decide how well we have done our job.",
        "subheader_convenience_mb": "CONVENIENCE IS A PRIORITY WHY?",
        "convenience_mb" : "In our team, the convenience of the gaming experience and the ease of in creation is a priority for us. But why convenience? The reason is simple. When you are comfortable, you can get optimal gaming experience. When it is convenient for us in development we can provide you with a new high-quality project. Therefore, our main priority is is convenience. ",
        "subheader_comfort_mb" : "WE THINK ABOUT COMFORT",
        "comfort_mb" : "Our first thought is always “Will the player will it be convenient for the player to play this way?”.  Or as an example, when developing this website, we thought, “Will it be convenient for the user to read the information? Will it be convenient for the programmer to create our design?”. It is up to you to decide how well we have done our job.",
        "subheader_projects" : "OUR CURRENT PROJECTS",
        "projects" : "Our team is actively working on various projects. Below you can see the current projects we are supporting or developing.",
        "BS" : "Box storm. This is a project that began its development in January 2024. But due to differences of opinion between Tom Owell and his colleagues, the project was closed. Six months later, Tom created his own project, Owell Games. And he was able to bring Box Storm back. Which is now being actively finalized and prepared for release.",
        "more_about_BS" : "Read more about Box Storm",
        "SH" : "Samurai Honor. The debut project of Owell Games. In which a lot of effort a lot of effort was put into it. And even if Samurai Honor is the starting point for Owell Games. Each of the participants is committed to the project 100% to the project. In an effort to create a gaming experience for you that will bring you good and positive emotions! ",
        "more_about_SH" : "Read more about Samurai Honor"
    }
}