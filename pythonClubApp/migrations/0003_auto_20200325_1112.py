from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0002_auto_20200325_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingminutes',
            name='meetingID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='club.Meeting'),
        ),
    ]