from django.core.management.base import BaseCommand
from shop.models import Product, Category


class Command(BaseCommand):
    help = 'Удаляет все товары и категории из базы данных'

    def handle(self, *args, **kwargs):
        product_count = Product.objects.count()
        category_count = Category.objects.count()

        if product_count == 0 and category_count == 0:
            self.stdout.write(self.style.WARNING("📭 Нет товаров и категорий для удаления."))
            return

        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(f"🗑 Удалено товаров: {product_count}"))
        self.stdout.write(self.style.SUCCESS(f"🗑 Удалено категорий: {category_count}"))
        self.stdout.write(self.style.SUCCESS("✅ Все данные успешно очищены."))
