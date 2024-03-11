# Generated by Django 4.2.4 on 2024-03-11 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=50)),
                ('subject1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject1_students', to='student_app.subject')),
                ('subject2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject2_students', to='student_app.subject')),
                ('subject3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject3_students', to='student_app.subject')),
                ('subject4', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject4_students', to='student_app.subject')),
                ('subject5', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject5_students', to='student_app.subject')),
            ],
        ),
    ]
