from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Register",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("UserId", models.CharField(max_length=50)),
                ("UserPassword", models.CharField(max_length=50)),
                ("UserName", models.CharField(max_length=10)),
                ("UserEmail", models.CharField(max_length=50)),
                ("UserPhone", models.CharField(max_length=50)),
                ("UserAddress", models.CharField(max_length=50)),
            ],
        ),
    ]
