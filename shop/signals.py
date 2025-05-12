# shop/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from shop.models import Category, Product
from django.core.management import call_command

@receiver(post_save, sender=Category)
def run_fix_categories(sender, instance, created, **kwargs):
    if created:
        call_command('fix_categories')

@receiver(post_save, sender=Product)
def run_fix_products(sender, instance, created, **kwargs):
    if created:
        call_command('fix_slugs')
