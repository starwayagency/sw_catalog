# Generated by Django 3.0.7 on 2020-07-03 16:54

import sw_shop.sw_catalog.utils.utils
import sw_utils.models
import colorfield.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import django.utils.timezone
import mptt.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sw_global_config', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sw_currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Код')),
                ('name', models.CharField(max_length=50, verbose_name='Назва')),
                ('name_uk', models.CharField(max_length=50, null=True, verbose_name='Назва')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Назва')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'атрибут',
                'verbose_name_plural': 'атрибути',
            },
        ),
        migrations.CreateModel(
            name='AttributeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('name_uk', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'категорія атрибутів',
                'verbose_name_plural': 'категорії атрибутів',
            },
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='Код')),
                ('value', models.CharField(max_length=255, verbose_name='Значення')),
                ('value_uk', models.CharField(max_length=255, null=True, verbose_name='Значення')),
                ('value_en', models.CharField(max_length=255, null=True, verbose_name='Значення')),
                ('value_ru', models.CharField(max_length=255, null=True, verbose_name='Значення')),
                ('attribute', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_catalog.Attribute', verbose_name='Атрибут')),
            ],
            options={
                'verbose_name': 'значення атрибуту',
                'verbose_name_plural': 'значення атрибутів',
            },
        ),
        migrations.CreateModel(
            name='CatalogConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Налаштування каталогу',
                'verbose_name_plural': 'Налаштування каталогу',
            },
        ),
        migrations.CreateModel(
            name='CatalogueConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items_per_page', models.PositiveIntegerField(default=24, null=True, verbose_name='Товарів на сторінці сайту')),
                ('posts_per_page', models.PositiveIntegerField(default=50, verbose_name='Статей на сторінці блоґу')),
                ('clear_catalogue', models.BooleanField(default=False, verbose_name=' Очистити каталог товарів ')),
            ],
            options={
                'verbose_name': 'Налаштування каталогу',
                'verbose_name_plural': 'Налаштування каталогу',
            },
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('name_uk', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'назва характеристики',
                'verbose_name_plural': 'назви характеристик',
            },
        ),
        migrations.CreateModel(
            name='FeatureCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('name_uk', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'категорія характеристик',
                'verbose_name_plural': 'категорії характеристик',
            },
        ),
        migrations.CreateModel(
            name='FeatureValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='Значення')),
                ('value_uk', models.CharField(max_length=255, null=True, verbose_name='Значення')),
                ('value_en', models.CharField(max_length=255, null=True, verbose_name='Значення')),
                ('value_ru', models.CharField(max_length=255, null=True, verbose_name='Значення')),
            ],
            options={
                'verbose_name': 'значення характеристики',
                'verbose_name_plural': 'значення характеристик',
            },
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(blank=True, help_text='Kод для виводу в шаблоні', max_length=255, null=True, unique=True, verbose_name='Код')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('is_active', models.BooleanField(default=True, help_text='Відображення на сайті', verbose_name='Активність')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Оновлено')),
                ('meta_title', models.TextField(blank=True, help_text='Заголовок сторінки в браузері, який відображається у видачі пошукових систем', null=True, verbose_name='Мета-заголовок')),
                ('meta_title_uk', models.TextField(blank=True, help_text='Заголовок сторінки в браузері, який відображається у видачі пошукових систем', null=True, verbose_name='Мета-заголовок')),
                ('meta_title_en', models.TextField(blank=True, help_text='Заголовок сторінки в браузері, який відображається у видачі пошукових систем', null=True, verbose_name='Мета-заголовок')),
                ('meta_title_ru', models.TextField(blank=True, help_text='Заголовок сторінки в браузері, який відображається у видачі пошукових систем', null=True, verbose_name='Мета-заголовок')),
                ('meta_descr', models.TextField(blank=True, help_text='__', null=True, verbose_name='Мета-опис')),
                ('meta_descr_uk', models.TextField(blank=True, help_text='__', null=True, verbose_name='Мета-опис')),
                ('meta_descr_en', models.TextField(blank=True, help_text='__', null=True, verbose_name='Мета-опис')),
                ('meta_descr_ru', models.TextField(blank=True, help_text='__', null=True, verbose_name='Мета-опис')),
                ('meta_key', models.TextField(blank=True, help_text='Список ключових слів', null=True, verbose_name='Ключові слова')),
                ('meta_key_uk', models.TextField(blank=True, help_text='Список ключових слів', null=True, verbose_name='Ключові слова')),
                ('meta_key_en', models.TextField(blank=True, help_text='Список ключових слів', null=True, verbose_name='Ключові слова')),
                ('meta_key_ru', models.TextField(blank=True, help_text='Список ключових слів', null=True, verbose_name='Ключові слова')),
                ('slug', models.SlugField(max_length=255, null=True, verbose_name='Посилання')),
                ('alt', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт до картинки')),
                ('alt_uk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт до картинки')),
                ('alt_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт до картинки')),
                ('alt_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт до картинки')),
                ('title', models.CharField(max_length=255, verbose_name='Назва')),
                ('title_uk', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Опис')),
                ('description_uk', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Опис')),
                ('description_en', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Опис')),
                ('description_ru', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Опис')),
                ('multipack', models.PositiveIntegerField(blank=True, null=True, verbose_name='Мультиупаковка')),
                ('amount', models.PositiveIntegerField(blank=True, default=None, help_text='0 - товар відсутній. Порожнє поле - необмежена кількість.', null=True, verbose_name='Кількість')),
                ('image', models.ImageField(blank=True, null=True, storage=sw_utils.models.OverwriteStorage(), upload_to='shop/item/', verbose_name='Картинка')),
                ('discount_type', models.CharField(choices=[('p', '%'), ('v', 'сумма')], default='v', max_length=255, verbose_name='Тип знижки')),
                ('discount', models.FloatField(default=0, max_length=255, verbose_name='знижка')),
                ('price', models.FloatField(default=0, verbose_name='Ціна')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товари',
            },
        ),
        migrations.CreateModel(
            name='ItemAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_option', models.BooleanField(default=False, verbose_name='Опція?')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_catalog.Attribute', verbose_name='Атрибут')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_attributes', to='sw_catalog.Item', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'атрибут товару',
                'verbose_name_plural': 'атрибути товарів',
                'unique_together': {('item', 'attribute')},
            },
        ),
        migrations.CreateModel(
            name='ItemBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(blank=True, help_text='Kод для виводу в шаблоні', max_length=255, null=True, unique=True, verbose_name='Код')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('is_active', models.BooleanField(default=True, help_text='Відображення на сайті', verbose_name='Активність')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Оновлено')),
                ('meta_title', models.TextField(blank=True, help_text='Заголовок сторінки в браузері, який відображається у видачі пошукових систем', null=True, verbose_name='Мета-заголовок')),
                ('meta_title_uk', models.TextField(blank=True, help_text='Заголовок сторінки в браузері, який відображається у видачі пошукових систем', null=True, verbose_name='Мета-заголовок')),
                ('meta_title_en', models.TextField(blank=True, help_text='Заголовок сторінки в браузері, який відображається у видачі пошукових систем', null=True, verbose_name='Мета-заголовок')),
                ('meta_title_ru', models.TextField(blank=True, help_text='Заголовок сторінки в браузері, який відображається у видачі пошукових систем', null=True, verbose_name='Мета-заголовок')),
                ('meta_descr', models.TextField(blank=True, help_text='__', null=True, verbose_name='Мета-опис')),
                ('meta_descr_uk', models.TextField(blank=True, help_text='__', null=True, verbose_name='Мета-опис')),
                ('meta_descr_en', models.TextField(blank=True, help_text='__', null=True, verbose_name='Мета-опис')),
                ('meta_descr_ru', models.TextField(blank=True, help_text='__', null=True, verbose_name='Мета-опис')),
                ('meta_key', models.TextField(blank=True, help_text='Список ключових слів', null=True, verbose_name='Ключові слова')),
                ('meta_key_uk', models.TextField(blank=True, help_text='Список ключових слів', null=True, verbose_name='Ключові слова')),
                ('meta_key_en', models.TextField(blank=True, help_text='Список ключових слів', null=True, verbose_name='Ключові слова')),
                ('meta_key_ru', models.TextField(blank=True, help_text='Список ключових слів', null=True, verbose_name='Ключові слова')),
                ('slug', models.SlugField(max_length=255, null=True, verbose_name='Посилання')),
                ('alt', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт до картинки')),
                ('alt_uk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт до картинки')),
                ('alt_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт до картинки')),
                ('alt_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт до картинки')),
                ('image', models.ImageField(blank=True, null=True, storage=sw_utils.models.OverwriteStorage(), upload_to='', verbose_name='Картинка')),
                ('title', models.CharField(max_length=255, verbose_name='Назва')),
                ('title_uk', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Опис')),
                ('description_uk', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Опис')),
                ('description_en', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Опис')),
                ('description_ru', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Бренд',
                'verbose_name_plural': 'Бренди',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ItemManufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(blank=True, help_text='Kод для виводу в шаблоні', max_length=255, null=True, unique=True, verbose_name='Код')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('is_active', models.BooleanField(default=True, help_text='Відображення на сайті', verbose_name='Активність')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Оновлено')),
                ('name', models.CharField(max_length=255, verbose_name='Назва')),
                ('name_uk', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'виробник товарів',
                'verbose_name_plural': 'виробники товарів',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ItemStock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, unique=True, verbose_name='Текст')),
                ('text_uk', models.CharField(max_length=255, null=True, unique=True, verbose_name='Текст')),
                ('text_en', models.CharField(max_length=255, null=True, unique=True, verbose_name='Текст')),
                ('text_ru', models.CharField(max_length=255, null=True, unique=True, verbose_name='Текст')),
                ('availability', models.BooleanField(default=True, verbose_name='Можливість покупки')),
                ('colour', colorfield.fields.ColorField(default='#FFFFFF', max_length=255, verbose_name='Колір')),
            ],
            options={
                'verbose_name': 'статус наявності',
                'verbose_name_plural': 'статуси наявності',
            },
        ),
        migrations.CreateModel(
            name='ItemUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Назва')),
                ('name_uk', models.CharField(max_length=255, null=True, unique=True, verbose_name='Назва')),
                ('name_en', models.CharField(max_length=255, null=True, unique=True, verbose_name='Назва')),
                ('name_ru', models.CharField(max_length=255, null=True, unique=True, verbose_name='Назва')),
            ],
            options={
                'verbose_name': 'одиниця вимірювання товарів',
                'verbose_name_plural': 'одиниці вимірювання товарів',
            },
        ),
        migrations.CreateModel(
            name='ItemView',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sk', models.CharField(max_length=255, verbose_name='Ключ сесії')),
                ('ip', models.CharField(max_length=255, verbose_name='IP-адреса')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_catalog.Item', verbose_name='Товар')),
            ],
        ),
        migrations.CreateModel(
            name='ItemReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(blank=True, help_text='Kод для виводу в шаблоні', max_length=255, null=True, unique=True, verbose_name='Код')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('is_active', models.BooleanField(default=True, help_text='Відображення на сайті', verbose_name='Активність')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Оновлено')),
                ('text', models.CharField(blank=True, max_length=255, null=True, verbose_name='Текст')),
                ('phone', models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='E-mail')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name="Ім'я")),
                ('rating', models.CharField(blank=True, max_length=255, null=True, verbose_name='Оцінка')),
                ('item', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='sw_catalog.Item', verbose_name='Товар')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Відгук',
                'verbose_name_plural': 'Відгуки',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('image', models.ImageField(blank=True, null=True, upload_to=sw_shop.sw_catalog.utils.utils.item_image_folder, verbose_name='Ссилка зображення')),
                ('alt', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт')),
                ('alt_uk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт')),
                ('alt_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт')),
                ('alt_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='sw_catalog.Item', verbose_name='Товар')),
            ],
            options={
                'verbose_name': 'зображення товару',
                'verbose_name_plural': 'зображення товару',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='ItemFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активність')),
                ('code', models.SlugField(blank=True, null=True, unique=True, verbose_name='Код')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_catalog.FeatureCategory', verbose_name='Категорія')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_catalog.Item', verbose_name='Товар')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_catalog.Feature', verbose_name='Назва характеристики')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_catalog.FeatureValue', verbose_name='Значення характеристики')),
            ],
            options={
                'verbose_name': 'характеристика товара',
                'verbose_name_plural': 'характеристики товара',
            },
        ),
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.SlugField(blank=True, help_text='Kод для виводу в шаблоні', max_length=255, null=True, unique=True, verbose_name='Код')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
                ('is_active', models.BooleanField(default=True, help_text='Відображення на сайті', verbose_name='Активність')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Створено')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Оновлено')),
                ('meta_title', models.TextField(blank=True, help_text='Заголовок сторінки в браузері, який відображається у видачі пошукових систем', null=True, verbose_name='Мета-заголовок')),
                ('meta_title_uk', models.TextField(blank=True, help_text='Заголовок сторінки в браузері, який відображається у видачі пошукових систем', null=True, verbose_name='Мета-заголовок')),
                ('meta_title_en', models.TextField(blank=True, help_text='Заголовок сторінки в браузері, який відображається у видачі пошукових систем', null=True, verbose_name='Мета-заголовок')),
                ('meta_title_ru', models.TextField(blank=True, help_text='Заголовок сторінки в браузері, який відображається у видачі пошукових систем', null=True, verbose_name='Мета-заголовок')),
                ('meta_descr', models.TextField(blank=True, help_text='__', null=True, verbose_name='Мета-опис')),
                ('meta_descr_uk', models.TextField(blank=True, help_text='__', null=True, verbose_name='Мета-опис')),
                ('meta_descr_en', models.TextField(blank=True, help_text='__', null=True, verbose_name='Мета-опис')),
                ('meta_descr_ru', models.TextField(blank=True, help_text='__', null=True, verbose_name='Мета-опис')),
                ('meta_key', models.TextField(blank=True, help_text='Список ключових слів', null=True, verbose_name='Ключові слова')),
                ('meta_key_uk', models.TextField(blank=True, help_text='Список ключових слів', null=True, verbose_name='Ключові слова')),
                ('meta_key_en', models.TextField(blank=True, help_text='Список ключових слів', null=True, verbose_name='Ключові слова')),
                ('meta_key_ru', models.TextField(blank=True, help_text='Список ключових слів', null=True, verbose_name='Ключові слова')),
                ('slug', models.SlugField(max_length=255, null=True, verbose_name='Посилання')),
                ('alt', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт до картинки')),
                ('alt_uk', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт до картинки')),
                ('alt_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт до картинки')),
                ('alt_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Альт до картинки')),
                ('image', models.ImageField(blank=True, null=True, storage=sw_utils.models.OverwriteStorage(), upload_to='', verbose_name='Картинка')),
                ('title', models.CharField(max_length=255, verbose_name='Назва')),
                ('title_uk', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Назва')),
                ('description', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Опис')),
                ('description_uk', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Опис')),
                ('description_en', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Опис')),
                ('description_ru', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Опис')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='sw_currency.Currency', verbose_name='Валюта')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subcategories', to='sw_catalog.ItemCategory', verbose_name='Батьківська категорія')),
            ],
            options={
                'verbose_name': 'категорія',
                'verbose_name_plural': 'категорії',
                'ordering': ['order'],
                'unique_together': {('title', 'parent')},
            },
            managers=[
                ('_tree_manager', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='sw_catalog.ItemBrand', verbose_name='Бренд'),
        ),
        migrations.AddField(
            model_name='item',
            name='category',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='sw_catalog.ItemCategory', verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='item',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='sw_currency.Currency', verbose_name='Валюта'),
        ),
        migrations.AddField(
            model_name='item',
            name='in_stock',
            field=models.ForeignKey(blank=True, help_text=' ', null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_catalog.ItemStock', verbose_name='Наявність'),
        ),
        migrations.AddField(
            model_name='item',
            name='labels',
            field=models.ManyToManyField(blank=True, related_name='items', to='sw_global_config.GlobalLabel', verbose_name='Мітки'),
        ),
        migrations.AddField(
            model_name='item',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='items', to='sw_catalog.ItemManufacturer', verbose_name='Виробник'),
        ),
        migrations.AddField(
            model_name='item',
            name='markers',
            field=models.ManyToManyField(blank=True, related_name='items', to='sw_global_config.GlobalMarker', verbose_name='Маркери'),
        ),
        migrations.AddField(
            model_name='item',
            name='similars',
            field=models.ManyToManyField(blank=True, default=None, related_name='_item_similars_+', to='sw_catalog.Item', verbose_name='Супутні товари'),
        ),
        migrations.AddField(
            model_name='item',
            name='unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_catalog.ItemUnit', verbose_name='Одиниці вимірювання'),
        ),
        migrations.CreateModel(
            name='CatalogRecipientEmail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, verbose_name='Емайл')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активність')),
                ('config', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='sw_catalog.CatalogConfig', verbose_name='Налаштування')),
            ],
            options={
                'verbose_name': 'емейл для сповіщень про товари',
                'verbose_name_plural': 'емейли для сповіщень про товари',
            },
        ),
        migrations.AddField(
            model_name='attribute',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attributes', to='sw_catalog.AttributeCategory', verbose_name='Категорія'),
        ),
        migrations.CreateModel(
            name='ItemAttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Ціна')),
                ('amount', models.PositiveIntegerField(blank=True, default=None, help_text='0 - товар з таким значенням характеристики відсутній. Порожнє поле - необмежена кількість.', null=True, verbose_name='Кількість')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('description_uk', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('description_en', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('description_ru', models.TextField(blank=True, null=True, verbose_name='Опис')),
                ('currency', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sw_currency.Currency', verbose_name='Валюта')),
                ('item_attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='sw_catalog.ItemAttribute', verbose_name='Атрибут товару')),
                ('proposition', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sw_catalog.Item', verbose_name='Товарна пропозиція')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sw_catalog.AttributeValue', verbose_name='Значення')),
            ],
            options={
                'verbose_name': 'значення атрибутів товарів',
                'verbose_name_plural': 'значення атрибутів товарів',
                'unique_together': {('item_attribute', 'value')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='attribute',
            unique_together={('name', 'category')},
        ),
    ]
