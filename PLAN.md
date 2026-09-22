# Dərs 8 — Template və static

> **Arxa monitor üçün.** Canlı kodu yazarkən **`ADDIMLAR.pdf`**-ə bax — orada hər addımda hansı faylda
> hansı sətirləri yazacağın yaşıl rənglə göstərilib. Bu fayl isə dərsin qısa xəritəsidir.
> Bu qovluq dərsin SONUNDAKI tam layihədir (Dərs 7-nin üzərində).
> Kodda nişanlar: `[DƏRS 8]` = sən yazırsan · `[PRAKTİKA 8]` = tələbə yazır · `[EV 8]` = ev tapşırığı.
> Köhnə `[DƏRS 7]` / `[EV 7]` nişanları sətrin hansı dərsdə yarandığını göstərir.
> I hissədə yalnız `[DƏRS 8]` hissələrini yaz. Qalanına toxunma, onlar tələbənindir.

**Dərsin sonunda:** eyni ünvanlar, amma blog sayt kimi görünür: navbar, kartlar, footer, CSS.
View-larda artıq `HttpResponse` və f-string HTML yoxdur, hamısı `render()` işlədir.

**Dərsdən əvvəl hazırla:** `static/css/style.css` faylını Telegram/Classroom-a qoy. Tələbə CSS yazmır.

## Bu layihəni işə salmaq (standart qayda)
```bash
cd project/django/lesson-08
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver         # → http://127.0.0.1:8000
```

---

## Vaxt planı

| Vaxt | Nə | Slayd | ADDIMLAR |
|---|---|---|---|
| 0:00–0:10 | 5 sual + ev tapşırığına baxış. Problem: HTML Python-un içindədir | 1–4 | 2 |
| 0:10–0:35 | **CANLI:** `settings` DIRS, qovluqlar, `render()`, `about.html`, `post_list.html` (`for`/`empty`/`if`), `post_detail`. Mikro | 5–13 | 3–7 |
| 0:35–0:45 | **CANLI:** filter-lər kartda və detalda | 14–16 | 8 |
| 0:45–1:10 | **CANLI:** `base.html` + `extends` + `block`, `_post_card.html` + `include`, `{% url %}`. Mikro | 17–24 | 9–12 |
| 1:10–1:25 | **CANLI:** `static/`, `{% load static %}`, CSS qoşulur. Xəta cədvəli | 25–29 | 13 |
| 1:25–1:35 | Commit + push. Sual-cavab | — | 14–15 |
| 1:35–1:45 | **Fasilə** | | |
| 1:45–2:50 | **PRAKTİKA:** 3 blok × ~22 dəq, hər blokun sonunda checkpoint | 30–34 | 16 |
| 2:50–3:00 | Son push, ev tapşırığı vərəqi, növbəti dərsin anonsu | 35 | 17–18 |

---

## CANLI KOD — addım-addım

### Addım 0 — başlanğıc (0:00)
Hamı öz reposunu `git clone` edir → `python3 -m venv .venv` → `source .venv/bin/activate` →
`pip install -r requirements.txt` → `runserver`. (Eyni kompüterdədirsə: `git pull` + `activate` bəsdir.)
Kateqoriya səhifələri Dərs 7-nin **ev tapşırığı** idi — yazmayan tələbəyə `project/django/lesson-07/`-dən
`category_list` / `category_detail`-i ver, yoxsa praktikada ilişəcək.
Dərs 7-nin saytını aç, `Ctrl+U` (view-source) göstər.
**De:** “Bu HTML-i biz f-string ilə yığmışıq. 20 səhifə olsa, navbar-ı 20 dəfə yazacağıq?”

### Addım 1 — settings + qovluqlar (0:10)
`config/settings.py` → `TEMPLATES` → `'DIRS': [BASE_DIR / 'templates']` (fayldakı `[DƏRS 8]` sətri).
Qovluqlar:
```
templates/                  ← layihə kökündə (manage.py-ın yanında)
blog/templates/blog/        ← app-ın içində, İKİ dəfə blog
```
**De:** “Niyə iki dəfə blog? Sabah `shop` app-ında da `list.html` olacaq. Django ilk tapdığını götürür.
`blog/list.html` desək, səhv fayl gəlməz. Dərs 7-dəki `app_name` ilə eyni fikirdir.”

### Addım 2 — ilk template: about (0:15)
`blog/templates/blog/about.html` → hələlik **extends-siz**, sadə `<h1>` + `<p>`.
`views.about` → `return render(request, "blog/about.html")`.
**Mikro (slayd 13, 5 dəq):** hamı eyni şeyi etsin. `TemplateDoesNotExist` çıxan olacaq.
Qovluq adına bax: `templates` sonda **s**. Yeni qovluqdan sonra `runserver`-i yenidən başlatmaq lazım ola bilər.

### Addım 3 — post_list.html (0:20)
`views.post_list` → `context = {"posts": POSTS}` → `render(...)`.
`post_list.html`: `{% for post in posts %}` → `<h2>{{ post.title }}</h2>` → `{% empty %}` → `{% endfor %}`.
**Göstər:** `{{ post["title"] }}` yaz → `TemplateSyntaxError`. **De:** “Template Python deyil. Hər şey nöqtə ilə.”
**Göstər:** `{{ post.rejissor }}` (olmayan açar) → xəta yox, boş. **De:** “Template səssizdir, diqqətli ol.”
**Göstər:** `{% empty %}`: `context = {"posts": []}` et → “Hələ post yoxdur.” Geri qaytar.
Başlığa `({{ posts|length }})` əlavə et.

`post_detail` → `render(request, "blog/post_detail.html", {"post": post})`. `Http404` olduğu kimi qalır.
**De:** “View-da nə dəyişdi? HTML getdi, məlumat qaldı.” (slayd 23-ü sonra göstərəcəksən)

### Addım 4 — filter-lər (0:35)
Detalda: `{{ post.created_at|date:"d F Y" }}` → “01 Sentyabr 2026” (`LANGUAGE_CODE='az'` sayəsində).
Siyahıda: `{{ post.content|truncatewords:12 }}`. Detalda: `{{ post.content|linebreaks }}`.
**Göstər:** `date: "d.m.Y"` (boşluqla) → `TemplateSyntaxError`. **De:** “Bir boşluq bütün səhifəni sındırır.”

### Addım 5 — base.html + extends (0:45)
`templates/base.html`: `<title>{% block title %}Blog{% endblock %} · STEP Blog</title>`,
**navbar-ı birbaşa base.html-in içində yaz** (partial-a köçürmək ev tapşırığıdır):
```html
<header class="navbar">
  <div class="container nav-inner">
    <a class="logo" href="{% url 'blog:post_list' %}">STEP<span>Blog</span></a>
    <nav>
      <a href="{% url 'blog:post_list' %}">Postlar</a>
      <a href="{% url 'blog:about' %}">Haqqımızda</a>
    </nav>
  </div>
</header>
<main class="container">{% block content %}{% endblock %}</main>
<footer class="footer"><div class="container">STEP IT Academy · Blog layihəsi</div></footer>
```
⚠ Layihə faylındakı `base.html`-də navbar artıq `{% include "partials/navbar.html" %}` ilə gəlir,
`{% now "Y" %}` də var. Bunlar `[EV 8]`-dir, dərsdə **yazma**.

`post_list.html` və `post_detail.html` → birinci sətir `{% extends "base.html" %}`, məzmun `{% block content %}`-ə.
**De:** “Dərs 4: `class Child(Parent)`. İndi: `{% extends "base.html" %}`. Block-u doldurmaq = override.”
**Göstər:** `extends`-i ikinci sətrə qoy → xəta. Geri qaytar.
**Mikro (slayd 24, 5 dəq):** `about.html`-i base-ə bağlasınlar.

### Addım 6 — include + {% url %} (0:55)
Kartı `blog/_post_card.html`-ə çıxar: badge (`post.category`), tarix, başlıq-link, `truncatewords:12`.
⚠ Layihədəki kartda `@author` linki `[EV 8]`-dir. Dərsdə müəllifi **yazma**, onu tələbə evdə edəcək.
`post_list.html` → `<div class="grid">{% for %}{% include "blog/_post_card.html" %}{% empty %}...`
Linklər: `{% url 'blog:post_detail' post.id %}`, `{% url 'blog:category_detail' post.category %}`.
**De:** “`reverse("blog:post_detail", args=[...])` ilə eynidir. Arqument boşluqla, vergülsüz.”
**De:** “Kart 3 yerdə lazım olacaq: ana səhifə, kateqoriya (praktika), müəllif (ev). Dizayn bir faylda.”

### Addım 7 — static (1:10)
`static/css/style.css` — paylaşdığın faylı qovluğa qoysunlar.
`settings.py` → `STATICFILES_DIRS = [BASE_DIR / 'static']`.
`base.html` birinci sətir `{% load static %}`, `<head>`-də `<link rel="stylesheet" href="{% static 'css/style.css' %}">`.
Brauzeri yenilə → sayt dəyişdi. **Bu, dərsin “vau” anıdır, bir dəqiqə ver.**
⚠ Dizayn gəlmirsə: `static/` qovluğu `manage.py`-ın yanında olmalıdır, sonra `Ctrl+Shift+R`.
**De:** “Class adları hazırdır: `card`, `grid`, `badge`, `list`, `empty`, `active`. CSS-ə toxunmayın.”

### Addım 8 — commit (1:25)
```bash
git add .
git commit -m "Dərs 8: template-lər və CSS"
git push
```

---

## PRAKTİKA — tələbə kateqoriyaları template-ə keçirir

| Blok | Tapşırıq | Checkpoint (ekranda yoxla) |
|---|---|---|
| A (~22 dəq) | `category_list.html` (extends, `ul.list`, ad-link + təsvir), view → `render` | `/categories/` navbar+CSS ilə, 3 kateqoriya, linklər işləyir |
| B (~22 dəq) | `category_detail` view: kateqoriya + **süzülmüş** `posts` siyahısı context-ə. `category_detail.html`: ad + `lead` təsvir. 404 qalır | `/category/oyunlar/` tab adı “Oyunlar”, `/category/futbol/` → 404 |
| C (~22 dəq) | Detalda `_post_card` include + `{% empty %}` “Bu kateqoriyada hələ post yoxdur.” + navbar-a “Kateqoriyalar” + push | `/category/oyunlar/`-da 2 kart, navbar-da link, GitHub-da commit |

**Qaydan:** yeni heç nə izah etmə. “Öz `post_list.html` və `post_detail.html`-inə bax. Eyni quruluşdur.”
**Vacib nüans (B):** postları süzmək view-da olur (`posts = []` + döngü + `append`), template-də `{% if post.category == ... %}` ilə yox.
Template-də süzən olsa, işləyir, amma göstər: “Məntiq view-dadır.”

**Post sayı haqqında:** kateqoriya siyahısında post sayını hələ göstərmirik. Soruşan olsa: “Dərs 10-da ForeignKey ilə bir sətir olacaq.”

### Tez-tez çıxan xətalar (praktikada)
| Xəta | Səbəb |
|---|---|
| `TemplateDoesNotExist: blog/category_list.html` | Fayl `blog/templates/blog/` içində deyil, ya da adında hərf səhvi |
| `TemplateSyntaxError: ... expected 'endblock'` / `'endfor'` | Bağlanış tag-ı unudulub |
| Səhifədə navbar var, məzmun yox | Məzmun `{% block content %}`-dən kənardadır, ya da block adı səhvdir |
| `NoReverseMatch` | `{% url 'blog:category_detail' category.slug %}` — slug unudulub, ya da ad səhvdir |
| `'dict' object has no attribute ...` / boş dəyər | Context açarı ilə template-dəki ad fərqlidir (`categories` vs `category`) |
| Kartlar görünür, amma boşdur | Include-dan əvvəl dövr dəyişəni `post` deyil (`for p in posts`) → kart `post` gözləyir |

---

## Növbəti dərsə körpü
Dərs 9-un əvvəlində: “Yeni post əlavə etmək üçün nə edirik? `data.py`-ı açıb kod yazırıq.
Sayt işləyərkən yeni post yaranarmı? Server yenidən başlasa, dəyişiklik qalarmı?” → verilənlər bazası, model, admin.
Template-lər demək olar dəyişməyəcək: `post.title` dict-də də, model obyektində də eyni yazılır.
