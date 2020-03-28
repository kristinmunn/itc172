from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingminutes',
            name='meetingID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='club.Meeting'),
        ),
    ]