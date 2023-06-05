# Generated by Django 4.2.1 on 2023-06-04 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GPT_rpg', '0004_character_player_alter_story_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='World',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=512)),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPT_rpg.player')),
                ('story_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPT_rpg.story')),
            ],
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=512)),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPT_rpg.player')),
                ('story_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPT_rpg.story')),
                ('world_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GPT_rpg.world')),
            ],
        ),
    ]