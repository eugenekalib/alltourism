from django.core.management.base import BaseCommand
from orders.models import Order  # Убедись, что модель Order действительно находится в orders.models


class Command(BaseCommand):
    help = 'Удаляет все заказы из базы данных'

    def handle(self, *args, **kwargs):
        order_count = Order.objects.count()

        if order_count == 0:
            self.stdout.write(self.style.WARNING("📭 Нет заказов для удаления."))
            return

        Order.objects.all().delete()

        self.stdout.write(self.style.SUCCESS(f"🗑 Удалено заказов: {order_count}"))
        self.stdout.write(self.style.SUCCESS("✅ Все заказы успешно очищены."))
