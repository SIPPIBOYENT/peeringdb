# Generated by Django 3.2.18 on 2023-03-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peeringdb_server', '0108_campus_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='ixfmemberdata',
            name='extra_notifications_net_date',
            field=models.DateTimeField(blank=True, help_text='Last time extra notifications were sent to the network for this proposal.', null=True),
        ),
        migrations.AddField(
            model_name='ixfmemberdata',
            name='extra_notifications_net_num',
            field=models.PositiveIntegerField(default=0, help_text='Indicates how many extra notifications were sent to the network for this proposal. Extra notifications can be sent for stale netixlan entries over time.'),
        ),
    ]
