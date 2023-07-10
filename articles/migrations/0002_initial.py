# Generated by Django 4.2.2 on 2023-07-10 03:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("articles", "0001_initial"),
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.AddField(
            model_name="recomment",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recomments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="recomment",
            name="comment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="articles.comment"
            ),
        ),
        migrations.AddField(
            model_name="recomment",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="like_recomments", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="recipeingredient",
            name="article",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="articles.article"
            ),
        ),
        migrations.AddField(
            model_name="recipeingredient",
            name="ingredient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="ingredients",
                to="articles.ingredient",
            ),
        ),
        migrations.AddField(
            model_name="ingredientlink",
            name="ingredient",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="articles.ingredient"
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="article",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="articles.article"
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="comments",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="like_comments", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="bookmark",
            field=models.ManyToManyField(
                blank=True, related_name="bookmarks", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="articles.category"
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="likes", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="tags",
            field=taggit.managers.TaggableManager(
                blank=True,
                help_text="A comma-separated list of tags.",
                through="taggit.TaggedItem",
                to="taggit.Tag",
                verbose_name="Tags",
            ),
        ),
    ]
