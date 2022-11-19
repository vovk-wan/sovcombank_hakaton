"""
make-currency.py
----------------
Модуль реализует первичное наполнение словаря валюты
"""
import csv
from pathlib import Path

from django.core.management import BaseCommand
from loguru import logger

from app_portfolio.models import CurrencyModel


def import_(folder: Path):
    """импорт документов в базу"""
    csv_file = folder / Path("physical_currency_list.csv")
    image_file = folder / Path("currency.png")

    with open(csv_file, "r", encoding="cp1251") as fl, open(
        image_file, "rb"
    ) as image_fl:
        image = image_fl.read()
        reader = csv.DictReader(fl)
        objects = []
        CurrencyModel.objects.all().delete()
        for item in reader:
            logger.info(item)
            objects.append(
                CurrencyModel(
                    description=item["название валюты"], name=item["currency code"]
                )
            )
        CurrencyModel.objects.bulk_create(objects)

    # for file in flag_folder.glob("*.png"):
    #     try:
    #         if product := ProductModel.objects.get(belongs=belongs):
    #             with file.open(mode="rb") as fl:
    #                 product.flag = File(fl, file.name)
    #                 product.save()
    #     except Exception as e:
    #         print(e)


class Command(BaseCommand):
    help = "импорт документов"

    def handle(self, *args, **options):
        """Обработчик команды"""
        path = Path(
            r"./info/physical_currency_list.csv"
        ).parent.parent.parent.parent.parent / Path("info")
        logger.info(f"start: {path.absolute()}")
        import_(path)
        logger.info(f"импорт завершён")
