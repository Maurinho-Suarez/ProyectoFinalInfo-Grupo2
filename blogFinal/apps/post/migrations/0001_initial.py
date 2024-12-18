import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=80)),
                ('autor', models.CharField(max_length=80)),
                ('descripcion_post', models.TextField()),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_editado', models.DateTimeField(auto_now=True)),
                ('imagen', models.ImageField(blank=True, default='posts/post_default.png', null=True, upload_to='post')),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='post.categoria')),
            ],
        ),
]
