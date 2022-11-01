# Generated by Django 3.2.16 on 2022-11-01 06:58

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import garpix_notify.mixins.user_notify_mixin
import garpix_notify.utils.file


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fcm_django', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default='', max_length=30, verbose_name='Телефон')),
                ('telegram_chat_id', models.CharField(blank=True, default='', max_length=200, verbose_name='Telegram ID пользователя/чата')),
                ('telegram_secret', models.CharField(default=garpix_notify.mixins.user_notify_mixin.generate_uuid, max_length=150, unique=True, verbose_name='Ключ подключения Telegram')),
                ('viber_chat_id', models.CharField(blank=True, default='', max_length=200, verbose_name='Viber ID пользователя/чата')),
                ('viber_secret_key', models.CharField(blank=True, default='', max_length=200, verbose_name='Ключ подключения Viber')),
                ('subject', models.CharField(blank=True, default='', max_length=255, verbose_name='Тема')),
                ('text', models.TextField(verbose_name='Текст')),
                ('html', models.TextField(blank=True, default='', verbose_name='HTML')),
                ('email', models.EmailField(blank=True, help_text='Используется только в случае отсутствия указанного пользователя', max_length=255, null=True, verbose_name='Email Получателя')),
                ('sender_email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Email Отправителя')),
                ('state', models.IntegerField(choices=[(1, 'Доставлено'), (-1, 'Отклонено'), (0, 'В ожидании'), (-2, 'Не отправлено (отправка запрещена настройками)')], default=0, verbose_name='Состояние')),
                ('event', models.IntegerField(blank=True, choices=[(1, 'Example')], null=True, verbose_name='Событие')),
                ('room_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название комнаты')),
                ('type', models.IntegerField(choices=[(0, 'E-mail'), (1, 'SMS'), (2, 'Push'), (3, 'Telegram'), (4, 'Viber'), (5, 'System'), (6, 'Call'), (7, 'WhatsApp')], verbose_name='Тип')),
                ('is_read', models.BooleanField(default=False, verbose_name='Прочитано')),
                ('data_json', models.TextField(blank=True, null=True, verbose_name='Данные пуш-уведомления (JSON)')),
                ('send_at', models.DateTimeField(blank=True, null=True, verbose_name='Время начала отправки')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('sent_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата отправки')),
                ('is_delete_after', models.BooleanField(default=False, verbose_name='Удалять после отправки')),
            ],
            options={
                'verbose_name': 'Уведомление',
                'verbose_name_plural': 'Уведомления',
            },
        ),
        migrations.CreateModel(
            name='NotifyCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('template', models.TextField(default='{{text}}', verbose_name='Шаблон')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='NotifyConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodic', models.IntegerField(default=60, verbose_name='Периодичность отправки уведомлений (сек.)')),
                ('email_max_day_limit', models.IntegerField(default=240, verbose_name='Дневной лимит отправки писем')),
                ('email_max_hour_limit', models.IntegerField(default=40, verbose_name='Часовой лимит отправки писем')),
                ('sms_url_type', models.IntegerField(choices=[(0, 'sms.ru'), (1, 'web.szk-info.ru'), (2, 'iqsms.ru'), (3, 'infosmska.ru'), (4, 'smsc.ru'), (5, 'sms-sending.ru'), (6, 'sms-prosto.ru')], default=0, verbose_name='URL СМС провайдера')),
                ('sms_api_id', models.CharField(blank=True, default='1234567890', max_length=255, verbose_name='API ID СМС провайдера')),
                ('sms_login', models.CharField(blank=True, default='', max_length=255, verbose_name='Логин пользователя СМС провайдера')),
                ('sms_password', models.CharField(blank=True, default='', max_length=255, verbose_name='Пароль для api СМС провайдера')),
                ('sms_from', models.CharField(blank=True, default='', help_text='Например, Garpix', max_length=255, verbose_name='Отправитель СМС')),
                ('call_url_type', models.IntegerField(choices=[(0, 'sms.ru API'), (1, 'sms.ru LOGIN'), (2, 'smsc.ru'), (3, 'ucaller.ru')], default=0, verbose_name='URL звонка провайдера')),
                ('call_api_id', models.CharField(blank=True, default='1234567890', max_length=255, verbose_name='API ID оператора связи')),
                ('call_login', models.CharField(blank=True, default='', max_length=255, verbose_name='Логин/Индетификатор сервиса оператора связи')),
                ('call_password', models.CharField(blank=True, default='', max_length=255, verbose_name='Пароль/Секретный ключ оператора связи')),
                ('telegram_api_key', models.CharField(blank=True, default='000000000:AAAAAAAAAA-AAAAAAAA-_AAAAAAAAAAAAAA', max_length=255, verbose_name='Telegram API Key')),
                ('telegram_bot_name', models.CharField(blank=True, default='', help_text='Например, MySuperBot', max_length=255, verbose_name='Telegram Имя бота')),
                ('telegram_welcome_text', models.TextField(blank=True, default='Добрый день! Здесь вы можете получать уведомления от нашего сайта', verbose_name='Telegram - Приветственный текст бота')),
                ('telegram_help_text', models.TextField(blank=True, default='Используйте команду /set <уникальный код> для того, чтобы получать сообщения от бота. Уникальный код вы можете получить на нашем сайте', verbose_name='Telegram - Текст помощи бота')),
                ('telegram_bad_command_text', models.TextField(blank=True, default='Неправильный формат команды', verbose_name='Telegram - Текст неправильной команды бота')),
                ('telegram_success_added_text', models.TextField(blank=True, default='Ваша учетная запись успешно привязана к боту. Вы будете получать уведомления!', verbose_name='Telegram - Текст успешно добавлен код')),
                ('telegram_failed_added_text', models.TextField(blank=True, default='Ошибка при привязке учетной записи. Пожалуйста, свяжитесь с техподдержкой', verbose_name='Telegram - Текст провал, не добавлен код')),
                ('telegram_parse_mode', models.CharField(blank=True, choices=[('', 'Без форматирования'), ('HTML', 'HTML'), ('Markdown', 'Markdown')], default='', max_length=100, verbose_name='Тип парсера телеграм сообщений')),
                ('telegram_disable_notification', models.BooleanField(default=False, verbose_name='Пользователи получат уведомление без звука')),
                ('telegram_disable_web_page_preview', models.BooleanField(default=False, verbose_name='Отключает предварительный просмотр ссылок в сообщениях')),
                ('telegram_allow_sending_without_reply', models.BooleanField(default=False, verbose_name='Разрешить, если сообщение должно быть отправлено, даже если ответное сообщение не найдено')),
                ('telegram_timeout', models.FloatField(blank=True, default=None, null=True, verbose_name='Тайм-аут чтения с сервера')),
                ('viber_api_key', models.CharField(blank=True, default='000000000:AAAAAAAAAA-AAAAAAAA-_AAAAAAAAAAAAAA', max_length=255, verbose_name='Viber API Key')),
                ('viber_bot_name', models.CharField(blank=True, default='Viber bot', max_length=255, verbose_name='Название viber бота')),
                ('whatsapp_sender', models.CharField(blank=True, default='', max_length=30, verbose_name='Телефон отправителя WhatsApp')),
                ('whatsapp_auth_token', models.CharField(blank=True, default='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', max_length=255, verbose_name='WhatsApp Auth Token')),
                ('whatsapp_account_sid', models.CharField(blank=True, default='ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX', max_length=255, verbose_name='WhatsApp Account SID')),
                ('is_email_enabled', models.BooleanField(default=True, verbose_name='Разрешить отправку Email')),
                ('is_sms_enabled', models.BooleanField(default=True, verbose_name='Разрешить отправку SMS')),
                ('is_call_enabled', models.BooleanField(default=True, verbose_name='Разрешить отправку звонков')),
                ('is_push_enabled', models.BooleanField(default=True, verbose_name='Разрешить отправку PUSH')),
                ('is_telegram_enabled', models.BooleanField(default=True, verbose_name='Разрешить отправку Telegram')),
                ('is_viber_enabled', models.BooleanField(default=True, verbose_name='Разрешить отправку Viber')),
                ('is_whatsapp_enabled', models.BooleanField(default=True, verbose_name='Разрешить отправку WhatsApp')),
                ('viber_success_added_text', models.TextField(blank=True, default='Ваша учетная запись успешно привязана к боту. Вы будете получать уведомления!', verbose_name='Viber - Текст успешно добавлен код')),
                ('viber_failed_added_text', models.TextField(blank=True, default='Ошибка при привязке учетной записи. Пожалуйста, свяжитесь с техподдержкой', verbose_name='Viber - Текст провал, не добавлен код')),
                ('viber_text_for_new_sub', models.TextField(blank=True, default='cпасибо за подписку, Введите secret_key чтобы получать сообщения от бота.', verbose_name='Viber - Текст  для новых подписчиков')),
                ('viber_welcome_text', models.TextField(blank=True, default='для активации бота нужно отправить любое сообщения', verbose_name='Viber - Приветственный текст бота')),
                ('email_malling', models.IntegerField(choices=[(0, 'Обычная рассылка'), (1, 'Скрытая рассылка')], default=1, help_text='Если выбрана обычная рассылка, то пользователи будут видеть email друг друга', verbose_name='Тип массовой рассылки')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
        migrations.CreateModel(
            name='NotifyErrorLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error', models.TextField(blank=True, default='', null=True, verbose_name='Ошибка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Лог отправки уведомления',
                'verbose_name_plural': 'Логи отправки уведомления',
            },
        ),
        migrations.CreateModel(
            name='NotifyFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(max_length=1000, upload_to=garpix_notify.utils.file.get_file_path, verbose_name='Файл')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Файл',
                'verbose_name_plural': 'Файлы',
            },
        ),
        migrations.CreateModel(
            name='NotifyTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default='', max_length=30, verbose_name='Телефон')),
                ('telegram_chat_id', models.CharField(blank=True, default='', max_length=200, verbose_name='Telegram ID пользователя/чата')),
                ('telegram_secret', models.CharField(default=garpix_notify.mixins.user_notify_mixin.generate_uuid, max_length=150, unique=True, verbose_name='Ключ подключения Telegram')),
                ('viber_chat_id', models.CharField(blank=True, default='', max_length=200, verbose_name='Viber ID пользователя/чата')),
                ('viber_secret_key', models.CharField(blank=True, default='', max_length=200, verbose_name='Ключ подключения Viber')),
                ('title', models.CharField(max_length=255, verbose_name='Название для админа')),
                ('subject', models.CharField(blank=True, default='', max_length=255, verbose_name='Заголовок')),
                ('is_delete_after', models.BooleanField(default=False, verbose_name='Удалять после отправки')),
                ('text', models.TextField(verbose_name='Текст')),
                ('html', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='HTML')),
                ('email', models.EmailField(blank=True, help_text='Используется только в случае отсутствия указанного пользователя', max_length=255, null=True, verbose_name='Email получатель')),
                ('type', models.IntegerField(choices=[(0, 'E-mail'), (1, 'SMS'), (2, 'Push'), (3, 'Telegram'), (4, 'Viber'), (5, 'System'), (6, 'Call'), (7, 'WhatsApp')], verbose_name='Тип')),
                ('event', models.IntegerField(blank=True, choices=[(1, 'Example')], null=True, verbose_name='Событие')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('send_at', models.DateTimeField(blank=True, null=True, verbose_name='Время начала отправки')),
            ],
            options={
                'verbose_name': 'Шаблон',
                'verbose_name_plural': 'Шаблоны',
            },
        ),
        migrations.CreateModel(
            name='NotifyUserList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название списка пользователей')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('mail_to_all', models.BooleanField(default=False, verbose_name='Массовая рассылка для всех пользователей сайта')),
            ],
            options={
                'verbose_name': 'Список пользователей для рассылки',
                'verbose_name_plural': 'Списки пользователей для рассылки',
            },
        ),
        migrations.CreateModel(
            name='NotifyUserListParticipant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, default='', max_length=30, verbose_name='Телефон')),
                ('telegram_chat_id', models.CharField(blank=True, default='', max_length=200, verbose_name='Telegram ID пользователя/чата')),
                ('telegram_secret', models.CharField(default=garpix_notify.mixins.user_notify_mixin.generate_uuid, max_length=150, unique=True, verbose_name='Ключ подключения Telegram')),
                ('viber_chat_id', models.CharField(blank=True, default='', max_length=200, verbose_name='Viber ID пользователя/чата')),
                ('viber_secret_key', models.CharField(blank=True, default='', max_length=200, verbose_name='Ключ подключения Viber')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('email', models.EmailField(blank=True, help_text='Используется только в случае отсутствия указанного пользователя', max_length=255, null=True, verbose_name='Email Получателя')),
            ],
            options={
                'verbose_name': 'Дополнительный участник списка рассылки',
                'verbose_name_plural': 'Дополнительные участники списка рассылки',
            },
        ),
        migrations.CreateModel(
            name='SMTPAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(default='smtp.yandex.com', max_length=255, verbose_name='Хост')),
                ('port', models.IntegerField(default=465, verbose_name='Порт')),
                ('is_use_tls', models.BooleanField(default=False, verbose_name='Использовать TLS?')),
                ('is_use_ssl', models.BooleanField(default=True, verbose_name='Использовать SSL?')),
                ('sender', models.CharField(blank=True, default='', max_length=255, verbose_name='Отправитель')),
                ('username', models.CharField(blank=True, default='', max_length=255, verbose_name='Имя пользователя')),
                ('password', models.CharField(blank=True, default='', max_length=255, verbose_name='Пароль пользователя')),
                ('timeout', models.IntegerField(default=5000, verbose_name='Таймаут (сек.)')),
                ('is_active', models.BooleanField(default=True, verbose_name='Включить аккаунт')),
                ('email_hour_used_times', models.IntegerField(default=0, verbose_name='Количество использований в час')),
                ('email_day_used_times', models.IntegerField(default=0, verbose_name='Количество использований в день')),
                ('email_hour_used_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата использований в час')),
                ('email_day_used_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата использований в день')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'SMTP аккаунт',
                'verbose_name_plural': 'SMTP аккаунты',
            },
        ),
        migrations.CreateModel(
            name='SystemNotify',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=255, verbose_name='Название')),
                ('state', models.IntegerField(choices=[(1, 'Доставлено'), (-1, 'Отклонено'), (0, 'В ожидании'), (-2, 'Не отправлено (отправка запрещена настройками)')], default=0, verbose_name='Состояние')),
                ('event', models.IntegerField(blank=True, choices=[(1, 'Example')], null=True, verbose_name='Событие')),
                ('room_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Название комнаты')),
                ('type', models.IntegerField(blank=True, choices=[(0, 'E-mail'), (1, 'SMS'), (2, 'Push'), (3, 'Telegram'), (4, 'Viber'), (5, 'System'), (6, 'Call'), (7, 'WhatsApp')], default=5, verbose_name='Тип')),
                ('data_json', models.JSONField(blank=True, default=dict, null=True, verbose_name='Данные JSON')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('sent_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата отправки')),
            ],
            options={
                'verbose_name': 'Ситемное уведомление',
                'verbose_name_plural': 'Системные уведомления',
            },
        ),
        migrations.CreateModel(
            name='NotifyDevice',
            fields=[
            ],
            options={
                'verbose_name': 'FCM аккаунт',
                'verbose_name_plural': 'FCM аккаунты',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('fcm_django.fcmdevice',),
        ),
        migrations.CreateModel(
            name='SystemNotifyErrorLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('error', models.TextField(blank=True, default='', null=True, verbose_name='Ошибка')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('notify', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logs', to='garpix_notify.systemnotify', verbose_name='SystemNotify')),
            ],
            options={
                'verbose_name': 'Лог отправки системного уведомления',
                'verbose_name_plural': 'Логи отправки системных уведомлений',
            },
        ),
    ]
