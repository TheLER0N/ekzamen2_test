# Initial data from the exam sample spreadsheets.

from datetime import date

from django.core.management.color import no_style
from django.db import migrations


def reset_sequences(schema_editor, models):
    statements = schema_editor.connection.ops.sequence_reset_sql(no_style(), models)
    if statements:
        with schema_editor.connection.cursor() as cursor:
            for statement in statements:
                cursor.execute(statement)


def seed_data(apps, schema_editor):
    Gender = apps.get_model("gender", "Gender")
    Status = apps.get_model("guest", "Status")
    RoomType = apps.get_model("guest", "RoomType")
    Hotel = apps.get_model("guest", "Hotel")
    Room = apps.get_model("guest", "Room")
    Guest = apps.get_model("guest", "Guest")
    History = apps.get_model("guest", "History")

    Gender.objects.bulk_create([
        Gender(IdGender=1, GenderName="Мужской"),
        Gender(IdGender=2, GenderName="Женский"),
    ], ignore_conflicts=True)

    Status.objects.bulk_create([
        Status(IdStatus=1, StatusName="Обычный"),
        Status(IdStatus=2, StatusName="VIP"),
    ], ignore_conflicts=True)

    RoomType.objects.bulk_create([
        RoomType(IdRoomType=1, RoomTypeName="Эконом"),
        RoomType(IdRoomType=2, RoomTypeName="Стандарт"),
        RoomType(IdRoomType=3, RoomTypeName="Люкс"),
    ], ignore_conflicts=True)

    Hotel.objects.bulk_create([
        Hotel(IdHotel=1, HotelName="Олимпиада"),
        Hotel(IdHotel=2, HotelName="Артхаус"),
        Hotel(IdHotel=3, HotelName="Магний"),
    ], ignore_conflicts=True)

    Room.objects.bulk_create([
        Room(IdRoom=1, Number=1, RoomTypeId_id=1, HotelId_id=1),
        Room(IdRoom=2, Number=1, RoomTypeId_id=1, HotelId_id=2),
        Room(IdRoom=3, Number=1, RoomTypeId_id=1, HotelId_id=3),
        Room(IdRoom=4, Number=2, RoomTypeId_id=2, HotelId_id=1),
        Room(IdRoom=5, Number=2, RoomTypeId_id=2, HotelId_id=2),
        Room(IdRoom=6, Number=2, RoomTypeId_id=3, HotelId_id=3),
        Room(IdRoom=7, Number=1, RoomTypeId_id=3, HotelId_id=3),
        Room(IdRoom=8, Number=4, RoomTypeId_id=3, HotelId_id=3),
        Room(IdRoom=9, Number=5, RoomTypeId_id=1, HotelId_id=3),
    ], ignore_conflicts=True)

    Guest.objects.bulk_create([
        Guest(IdGuest=1, FullName="Ветров Иван Иванович", Birthday=date(2006, 12, 1), GenderId_id=1, StatusId_id=1),
        Guest(IdGuest=2, FullName="Веревкина Мария Ивановна", Birthday=date(2001, 1, 1), GenderId_id=2, StatusId_id=2),
        Guest(IdGuest=3, FullName="Петров Петр Петрович", Birthday=date(1988, 2, 3), GenderId_id=1, StatusId_id=1),
        Guest(IdGuest=4, FullName="Иванов Иван Иванович", Birthday=date(1978, 11, 2), GenderId_id=1, StatusId_id=2),
        Guest(IdGuest=5, FullName="Сидоров Сидор Сидорович", Birthday=date(1977, 1, 2), GenderId_id=1, StatusId_id=1),
        Guest(IdGuest=6, FullName="Соловьев Павел Анатольевич", Birthday=date(1987, 2, 5), GenderId_id=1, StatusId_id=1),
    ], ignore_conflicts=True)

    History.objects.bulk_create([
        History(IdHistory=1, GuestId_id=1, RoomId_id=1, CheckIn=date(2026, 2, 2), CheckOut=date(2026, 2, 3), Comment=None),
        History(IdHistory=2, GuestId_id=2, RoomId_id=2, CheckIn=date(2026, 3, 3), CheckOut=date(2026, 2, 3), Comment=None),
        History(IdHistory=3, GuestId_id=3, RoomId_id=3, CheckIn=date(2026, 1, 1), CheckOut=date(2026, 1, 10), Comment=None),
        History(IdHistory=4, GuestId_id=4, RoomId_id=4, CheckIn=date(2026, 2, 2), CheckOut=date(2026, 2, 3), Comment=None),
        History(IdHistory=5, GuestId_id=5, RoomId_id=5, CheckIn=date(2026, 3, 3), CheckOut=date(2026, 3, 5), Comment=None),
        History(IdHistory=6, GuestId_id=6, RoomId_id=6, CheckIn=date(2026, 5, 5), CheckOut=date(2026, 5, 6), Comment="Странный постоялец."),
        History(IdHistory=7, GuestId_id=6, RoomId_id=6, CheckIn=date(2025, 1, 1), CheckOut=date(2025, 2, 1), Comment=None),
        History(IdHistory=8, GuestId_id=1, RoomId_id=6, CheckIn=date(2025, 6, 1), CheckOut=date(2026, 6, 2), Comment=None),
        History(IdHistory=9, GuestId_id=2, RoomId_id=2, CheckIn=date(2025, 7, 8), CheckOut=date(2026, 7, 9), Comment=None),
        History(IdHistory=10, GuestId_id=1, RoomId_id=7, CheckIn=date(2026, 5, 5), CheckOut=date(2026, 6, 2), Comment=None),
        History(IdHistory=11, GuestId_id=3, RoomId_id=8, CheckIn=date(2026, 4, 12), CheckOut=date(2026, 5, 1), Comment=None),
        History(IdHistory=12, GuestId_id=4, RoomId_id=9, CheckIn=date(2026, 1, 1), CheckOut=date(2026, 4, 2), Comment=None),
    ], ignore_conflicts=True)

    reset_sequences(schema_editor, [Gender, Status, RoomType, Hotel, Room, Guest, History])


class Migration(migrations.Migration):
    dependencies = [
        ("gender", "0001_initial"),
        ("guest", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_data, migrations.RunPython.noop),
    ]
