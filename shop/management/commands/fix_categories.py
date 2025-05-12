from django.core.management.base import BaseCommand
from shop.models import Category
from django.template.defaultfilters import slugify

class Command(BaseCommand):
    help = 'Автоматически проставляет уникальные slug для категорий без slug'

    def handle(self, *args, **kwargs):
        updated = 0
        for category in Category.objects.all():
            if not category.slug or category.slug.strip() == '':
                base_slug = slugify(category.title)  # ВОТ ТУТ ИСПРАВЛЕНО
                slug = base_slug
                counter = 1
                while Category.objects.filter(slug=slug).exclude(id=category.id).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                category.slug = slug
                category.save()
                self.stdout.write(self.style.SUCCESS(f"✅ {category.title} → {category.slug}"))
                updated += 1

        if updated == 0:
            self.stdout.write(self.style.WARNING("Все категории уже имеют slug. Ничего не обновлено."))
        else:
            self.stdout.write(self.style.SUCCESS(f"🎉 Обновлено категорий: {updated}"))
