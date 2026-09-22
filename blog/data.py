# Hələlik verilənlər bazası yoxdur — məlumat adi Python siyahısıdır.
# Bu, Dərs 1-dəki list[dict] strukturudur.
# Dərs 9-da bu məlumat bazaya köçürüləcək və fayl silinəcək.

from datetime import date

# [DƏRS 7] müəllim yazır
POSTS = [
    {
        "id": 1,
        "title": "Python-da ilk addım",
        "author": "nigar",
        "category": "proqramlasdirma",
        "created_at": date(2026, 9, 1),
        "content": "Python öyrənməyə haradan başlamaq lazımdır? Əvvəlcə dəyişənlər, "
                   "sonra şərtlər və döngülər. Ən vacibi isə hər gün bir az kod yazmaqdır.",
    },
    {
        "id": 2,
        "title": "Minecraft-da redstone ilə kalkulyator",
        "author": "murad",
        "category": "oyunlar",
        "created_at": date(2026, 9, 5),
        "content": "Redstone əslində elektrik dövrəsidir. AND, OR və NOT qapılarından "
                   "istifadə edib oyunun içində işləyən kalkulyator qurmaq olur.",
    },
    {
        "id": 3,
        "title": "Git nədir və niyə lazımdır?",
        "author": "nigar",
        "category": "proqramlasdirma",
        "created_at": date(2026, 9, 9),
        "content": "Git kodun tarixçəsini saxlayır. Səhv etsən, köhnə versiyaya qayıda "
                   "bilərsən. GitHub isə bu tarixçəni internetdə saxlayan saytdır.",
    },
    {
        "id": 4,
        "title": "Harri Potter kitablarını hansı ardıcıllıqla oxumalı?",
        "author": "aysel",
        "category": "kitablar",
        "created_at": date(2026, 9, 12),
        "content": "Yeddi kitabın hamısını çıxış ilinə görə oxumaq ən yaxşısıdır. "
                   "Filmlərə isə kitabları bitirəndən sonra baxmağı məsləhət görürəm.",
    },
    {
        "id": 5,
        "title": "FIFA-da ən yaxşı taktika",
        "author": "murad",
        "category": "oyunlar",
        "created_at": date(2026, 9, 15),
        "content": "4-3-3 sxemi hücum üçün, 5-3-2 isə müdafiə üçün yaxşıdır. "
                   "Amma ən vacibi oyunçuların formasıdır.",
    },
]

# [PRAKTİKA 7] bu siyahı slayddan hazır verilir, tələbə yalnız view-ları yazır
CATEGORIES = [
    {"slug": "proqramlasdirma", "name": "Proqramlaşdırma", "description": "Kod, dillər və alətlər"},
    {"slug": "oyunlar", "name": "Oyunlar", "description": "Oyunlar, taktikalar və maraqlı faktlar"},
    {"slug": "kitablar", "name": "Kitablar", "description": "Oxuduqlarımız və tövsiyələr"},
]
