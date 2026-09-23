from django.db import migrations, models
import django.db.models.deletion


def create_categories_and_link_posts(apps, schema_editor):
    Category = apps.get_model("blog", "Category")
    Post = apps.get_model("blog", "Post")

    categories = [
        ("proqramlasdirma", "Proqramlaşdırma", "Kod, dillər və alətlər"),
        ("oyunlar", "Oyunlar", "Oyunlar, taktikalar və maraqlı faktlar"),
        ("kitablar", "Kitablar", "Oxuduqlarımız və tövsiyələr"),
    ]
    for slug, name, description in categories:
        category = Category(slug=slug, name=name, description=description)
        category.save()
        Post.objects.filter(category=slug).update(category_new=category)

    posts = [
        ("python-da-ilk-addim", "Python-da ilk addım", "nigar", "proqramlasdirma", "Python öyrənməyə haradan başlamaq lazımdır? Əvvəlcə dəyişənlər, sonra şərtlər və döngülər. Ən vacibi isə hər gün bir az kod yazmaqdır."),
        ("minecraft-da-redstone-ile-kalkulyator", "Minecraft-da redstone ilə kalkulyator", "murad", "oyunlar", "Redstone əslində elektrik dövrəsidir. AND, OR və NOT qapılarından istifadə edib oyunun içində işləyən kalkulyator qurmaq olur."),
        ("git-nedir-ve-niye-lazimdir", "Git nədir və niyə lazımdır?", "nigar", "proqramlasdirma", "Git kodun tarixçəsini saxlayır. Səhv etsən, köhnə versiyaya qayıda bilərsən. GitHub isə bu tarixçəni internetdə saxlayan saytdır."),
        ("harri-potter-kitablarini-hansi-ardicilliqla-oxumali", "Harri Potter kitablarını hansı ardıcıllıqla oxumalı?", "aysel", "kitablar", "Yeddi kitabın hamısını çıxış ilinə görə oxumaq ən yaxşısıdır. Filmlərə isə kitabları bitirəndən sonra baxmağı məsləhət görürəm."),
        ("fifa-da-en-yaxsi-taktika", "FIFA-da ən yaxşı taktika", "murad", "oyunlar", "4-3-3 sxemi hücum üçün, 5-3-2 isə müdafiə üçün yaxşıdır. Amma ən vacibi oyunçuların formasıdır."),
    ]
    for slug, title, author, category_slug, content in posts:
        if Post.objects.filter(slug=slug).first() is None:
            post = Post(
                slug=slug,
                title=title,
                author=author,
                category_new=Category.objects.filter(slug=category_slug).first(),
                content=content,
            )
            post.save()


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("slug", models.SlugField(unique=True)),
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="category_new",
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name="posts", to="blog.category"),
        ),
        migrations.RunPython(create_categories_and_link_posts, migrations.RunPython.noop),
        migrations.RemoveField(
            model_name="post",
            name="category",
        ),
        migrations.RenameField(
            model_name="post",
            old_name="category_new",
            new_name="category",
        ),
        migrations.AlterField(
            model_name="post",
            name="category",
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="posts", to="blog.category"),
        ),
    ]