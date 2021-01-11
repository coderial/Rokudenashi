# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
init -2:
    # 배경
    image blackout = "images/background/blackground.png"
    image fegite = "images/background/street.png"

    # 기타 이미지
    image hole = "images/background/hole.png"
    image explosion = "images/etc/explosion.png"
    image Magic_Circle = "images/etc/magic.png"
    image extinction:
        "images/etc/explosion.png"
        pause 1
        "images/etc/explosion2.png"
        pause 1
        "images/etc/explosion3.png"
        pause 1
        "images/etc/explosion4.png"
        repeat


    # 효과음 & 배경음악
    define pleasant_morning = "sounds/start.mp3"
    define big_ex =  "sounds/Big Explosion.mp3"
    define exp_sound = "sounds/explosion.mp3"
    define distroyed = "sounds/distroy.mp3"
    define hit = "sounds/hit.mp3"
    define refresh = "sounds/Refresh Mornig.mp3"

    # 캐릭터
    image ch_glenn:
        "images/glenn/glenn_idle.png"

    image ch_celica:
        "images/celica/celica_idle.png"

    image ch_sistine:
        "images/sistine/sistine_idle.png"

    image ch_rumia:
        "images/rumia/rumia_idle.png"