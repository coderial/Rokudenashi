# 이 파일에 게임 스크립트를 입력합니다.

# image 문을 사용해 이미지를 정의합니다.
# image eileen happy = "eileen_happy.png"

# 게임에서 사용할 캐릭터를 정의합니다.



# 여기에서부터 게임이 시작합니다.
label start:
    $ renpy.free_memory()
    $ skip_mode = False

    menu:
        "테스트용":
            jump go_end
        "다봐":
            pass

    play music pleasant_morning
    scene blackout with fade
    window hide dissolve
    centered "이것은 어느 날 이른 아침의 풍경." with dissolve
    window show
    scene back with wipeleft
    show ch_glenn at left with dissolve
    show ch_celica at right with dissolve
    
    glenn "뭐랄까~ 난 진심으로 이렇게 생각해. 일하는 건 곧 지는 거라고.\n내가 살아 있는 건 네 덕분이야. 네가 있어서 정말 다행이지 뭐냐."
    celica "후, 그러냐. 죽어, 밥벌레."
    glenn "아하하! 세리카는 엄격한걸! 아, 한 그릇 더."
    celica "넌 참으로 뻔뻔하군.\n보통 공짜밥 먹는 식객이라는 건 좀 더 겸허한 법이다만."
    glenn "아~ 오늘 음식은 약간 짜더라. 난 좀 더 담백한 맛이 취향인데."
    celica "게다가 불평까지? 정말 기가 막히는군."
    $ renpy.music.set_pause(True, 'music')
    celica "《뭐·어쨌든·폭발해라》."

    scene blackout
    show explosion with vpunch
    play sound exp_sound
    scene back with fade
    show ch_glenn at bury with dissolve
    show ch_celica at right with dissolve


    $ renpy.music.set_pause(False, 'music')
    glenn "쿨럭쿨럭… 이, 이 바보가! 너, 날 죽일 작정이야?!"
    celica "죽여? 그게 무슨 소리냐. 쓰레기를 치우는 건 청소라고 말하는 거란다. 글렌."
    glenn "아이의 실수를 부드럽게 타이르는 엄마 같은 말투로 할 말이 아니잖아! 하다못해 인간 취급이라도 해달라고요!"
    celica "하아…"


    hide ch_celica with dissolve
    show ch_celica at center with dissolve
    show ch_glenn at ani_harp_stand
    pause(0.5)

    celica "그건 그렇고 이봐, 글렌. ……너 슬슬 일자리를 찾아보는 게 어때?"
    celica "네가 전에 하던 일을 그만두고 내 집의 식객이 된 지 벌써 1년이다."
    celica "넌 매일같이 먹고 자고, 먹고 자면서 아무 일도 하지 않으며 멍하니 시간만 보낼 뿐.{w}\n그런 건 수명 낭비라고 생각하지 않아?"
    glenn "괜찮아. 난 지금의 내가 좋거든."
    show ch_glenn at ani_stand
    pause(0.5)

    glenn "사회의 톱니바퀴가 되어서 완만하게 죽어가던 예전의 나보다는 지금의 내가 훨씬 더 빛나고 있으니까!"
    celica "뭘 어떻게 비교해야 집 안에 틀어박혀서 밥만 축내는 삶이 더 빛난다고 할 수 있는 거냐. 차라리 그냥 죽어. 제발."
    celica "너란 녀석은 참…… 옛 친분으로 널 돌봐주고 있는 나에게 조금이라도 미안하다는 생각은 안 드는 거냐?"
    glenn "훗, 나랑 너 사이에 이제 와서 무슨 섭섭한 소릴."


    $ renpy.music.set_pause(True, 'music')

    show Magic_Circle at onHand with dissolve
    celica "《그대는 섭리의 원환으로 귀환하라·오대원소는 오대원소로·상(象)과 섭리를……."
    show ch_glenn at left_backstep
    glenn "잠깐만?! 그건 【익스팅션 레이】잖아?! 기, 기다려! 그것만은 참아줘! 완전히 산산조각 날 거라고! 으아아아아아!"
    pause(1.0)
    hide Magic_Circle with dissolve
    $ renpy.music.set_pause(False, 'music')
    celica "하아… 뭐, 됐다. 너 같은 놈을 마술로 처분하는 건 그야말로 마술에 대한 모독일 테니까. 전설의 검을 바퀴벌레에게 겨누는 거나 마찬가지겠지."
    glenn "그거 말이 좀 심하지 않아? 바퀴벌레에게 실례잖아."
    celica "지적하는 건 그쪽이냐?! 일단 자각은 있는 건가. 정말 못 말리겠군!"
    celica "뭐, 어쨌든 슬슬 너도 앞으로 나아가야 할 때라고 생각해. 계속 이렇게 시간을 낭비하고 있을 수는 없잖아? 그건 너 자신도 잘 알고 있을 테지?"
    glenn "그렇다고는 해도…… 이제 와서 일이라니…… 대체 내가 뭘 할 수 있겠어?"
    celica "너라면 그렇게 말할 줄 알았지. 그러니 내가 너에게 일자리를 하나 알선해주마."
    
    show ch_glenn at goLeft
    glenn "일자리?"
    celica "그래. 실은 지금 알자노 제국 마술학원에 강사 자리가 하나 비어 있다."
    glenn "마술학원?"
    celica "갑작스러운 일이다 보니 대신할 강사를 찾기가 곤란하더군. 그러니 잠시 네가 계약직 강사를 맡아줬으면 해."
    glenn "잠깐 기다려봐. 그런데 하필이면 왜 나야? 거기에는 할 일 없는 교수놈들이 우글거리고 있잖아. 임시 강사라면 그놈들한테 시키면 되는 거 아냐?"
    celica "너무 그렇게 말하지 마라. 우리 교수진은 이제 곧 제도에서 열리는 제국 종합 마술학회에 참가할 준비를 하느라 다들 바빠. 안타깝지만 지금 이 시기에 학생들을 신경 쓸 여유는 없어."
    glenn "아~ 그러고 보니 그런 시기였던가."
    celica "아무튼 기간은 한 달. 급료도 특별히 정규직 강사와 같은 액수가 지급되도록 힘써 주마. 네 업무능력에 따라서는 정규직으로 전환하는 것도 생각하도록 하지. 어때? 나쁘지 않은 이야기지?"
    glenn "흥……."
    glenn "……무리겠지."
    celica "무리라고? 어째서지? 글렌."
    glenn "너도 알잖아? 나에겐 다른 사람을 가르칠 자격이 없다는걸……."
    celica "그야 그렇겠지. 넌 교사 자격증이 없으니까."
    glenn "야, 사람이 모처럼 무게 좀 잡아보려는데 현실을 들이밀지 말라고."
    celica "뭐, 자격증은 걱정하지 마라. 학원에서의 내 지위와 권한으로 어떻게 든 될 테니까. 그리고 네가 실적을 올리기만 하면 뒷구멍으로 자격증을 따는 건 그리 어려운 일이 아니야."
    glenn "야, 잠깐! 그건 직권 남용이잖아!"
    celica "네 능력이라면 마술강사로 일하는 것에 문제는 없을 터. 너도 옛날에는 나름 마술을 공부한 몸이니까 말이지. 어때, 한번 해보는 건?"
    glenn "흠, 어떻게 할까……"
    glenn "좋아. 살짝 불안하기는 하지만 여기서는 일단 온힘을 다해서 거절해볼까♪"
    celica "그 동작, 징그러운 데다가 짜증까지 나는군. 게다가 거절까지? 진심으로 나가 죽으라는 생각이 무럭무럭 드는데."
    celica "참고로 너에게 거부권은 없어."
    glenn "흐음? 그래도 싫다고 한다면?"
    celica "벼락을 맞는 게 취향이냐? 아니면 불꽃으로 바비큐는 어때? 아, 꽁꽁 얼려버리는 것도 후보에 넣어줄까?"
    glenn "훗, 말로 안 되겠으니 바로 폭력에 호소하겠다는 건가? 그게 근본적인 해결책이 될 거라고 생각하는 건 아니겠지?"
    celica "지긋지긋할 정도로 정론이기는 하지만, 그게 네가 할 소리냐!"
    
    show Magic_Circle at onHand with dissolve

    glenn "멍청한 녀석. 넌 아직도 내 진정한 무서움을 모르는 모양이군……."
    glenn "넌 알고 있을 텐데. 내가 『그럴 마음』만 먹는다면 너 정도의 마술사는 전혀 문제되지 않는다는 사실을……."
    celica "칫."
    glenn "네 싸구려 협박은 내가 『그럴 마음』을 먹게 했을 뿐이야!"


    pause(1.0)
    show ch_glenn at ani_bow
    pause(1.0)


    glenn "부양해주세요!"
    celica "……확실히 난 너에게 전율을 느꼈다."
    glenn "부탁입니다! 세리카 씨! 전 절대로 일하고 싶지 않다고요! 제발 절 부양해주세요오오오오! 신발이든 뭐든 핥으라면 핥을 테니까요!"
    celica "너 말이다……. 넌 인간으로서의 자긍심도 없는 거냐?"
    glenn "멍청아! 자긍심이 누구 밥 먹여줘?! 엉?! 어디 한 번 대답해보시지!"
    celica "게다가 이번에는 적반하장으로 나오는 거냐. 이젠 진짜로 죽여버리고 싶은걸."
    glenn "……훗, 너에게 날 부양할 권리를 주마."
    celica "죽어!"

    hide Magic_Circle
    show ch_celica at Left_TreadOn
    play sound hit
    pause(2.0)

    celica "에잇, 아무튼 일을 해! 싫으면 이 집에서 나가! 안 나간다면 진심으로 분해해주마! 난 이제 네 한심스러운 꼬락서니를 보는 건 지긋지긋하다고!"
    glenn "너, 넌 악마냐?! 내가 무슨 세계 평화 같은 거창한 걸 바라는 것도 아니잖아! 난 그저 지극히 평범하게, 평온하고도 평화로운 은둔형 외톨이 생활을 계속하고 싶은 것뿐이라고!"
    glenn "그런 소박한 소원을 가지는 것도 죄라는 거야?! 애초에 너에겐 날 평생 부양하고도 남을 재산이 있으면서!"
    glenn "그리고 너도 알잖아?! 내가 마술을, 그 이름을 듣는 것조차 싫을 정도로 혐오한다는걸!"
    celica "……글렌."
    show ch_celica at goCenter
    glenn "아무튼 난 이제 절대로! 무슨 일이 있어도! 두 번 다시 마술과 연관되고 싶지 않아! 흥이다! 마술강사 같은 걸 할 정도라면 차라리 길바닥에서 구걸하는 편이 더 낫─."
    show Magic_Circle at onHand with dissolve
    stop music
    celica "《그대는 섭리의 원환으로 귀환하라·오대원소는 오대원소로·상과 섭리를 잇는 인연은 괴리할지어다》."

    scene blackout
    play sound big_ex
    show extinction

    $ renpy.pause(3,hard=True)

    scene hole
    play sound distroyed
    show ch_celica at center
    show ch_glenn at left_corner
    pause(0.5)
    show ch_glenn at LeftCorner_shake
    celica "칫, 빗나갔나."
    celica "이번에는 맞출 거야……"
    
    show Magic_Circle at onHand with dissolve
    celica "《그대는 섭리의 원환으로 귀환하라·오대원소는 오대원소로·상과 섭리를……."
    glenn "마, 마마아아아아아아아아?!"

    scene blackout
    centered "이렇게 해서 글렌의 새로운 직장은 반강제적으로 정해졌다." with dissolve
    centered "1년 만에 얻은 그의 직업은 영광스러운 알자노 제국 마술학원의 계약직 강사." with dissolve
    centered "단, 한 달이라는 기한이 전제로 붙은 여러모로 장래가 불안해지는 직업이었다." with dissolve



    return

label go_end:
    scene fegite
    play music refresh
    

    return
