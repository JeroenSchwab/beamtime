# Generated by Django 3.2.3 on 2021-10-22 08:56

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('beamrequest', '0035_createbeamrequestmodel_different_beams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='createbeamrequestmodel',
            name='Beam_1',
        ),
        migrations.RemoveField(
            model_name='createbeamrequestmodel',
            name='Different_Beams',
        ),
        migrations.AddField(
            model_name='createbeamrequestmodel',
            name='Energy',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='Ion_Species', chained_model_field='Ion_Species', null=True, on_delete=django.db.models.deletion.CASCADE, to='beamrequest.energys'),
        ),
        migrations.AddField(
            model_name='createbeamrequestmodel',
            name='Flux',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='createbeamrequestmodel',
            name='Hours',
            field=models.IntegerField(default='1'),
        ),
        migrations.AddField(
            model_name='createbeamrequestmodel',
            name='Ion_Species',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='beamrequest.ionspecies'),
        ),
        migrations.DeleteModel(
            name='BeamModel',
        ),
    ]
