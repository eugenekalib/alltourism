from django.core.management.base import BaseCommand
from shop.models import Product
from django.template.defaultfilters import slugify


class Command(BaseCommand):
    help = 'Автоматически проставляет уникальные slug для товаров без slug'

    def handle(self, *args, **kwargs):
        updated = 0
        for product in Product.objects.all():
            if not product.slug or product.slug.strip() == '':
                base_slug = slugify(product.title)
                slug = base_slug
                counter = 1
                while Product.objects.filter(slug=slug).exclude(id=product.id).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                product.slug = slug
                product.save()
                self.stdout.write(self.style.SUCCESS(f"✅ {product.title} → {product.slug}"))
                updated += 1

        if updated == 0:
            self.stdout.write(self.style.WARNING("Все товары уже имеют slug. Ничего не обновлено."))
        else:
            self.stdout.write(self.style.SUCCESS(f"🎉 Обновлено товаров: {updated}"))
