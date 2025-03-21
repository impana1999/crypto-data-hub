from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Organization
import logging

logger = logging.getLogger(__name__)  # Set up logging

@receiver(post_save, sender=Organization)
def log_organization_created(sender, instance, created, **kwargs):
    """✅ Log when an organization is created"""
    if created:
        logger.info(f"🚀 Organization '{instance.name}' (ID: {instance.id}) was created.")

@receiver(post_delete, sender=Organization)
def log_organization_deleted(sender, instance, **kwargs):
    """✅ Log when an organization is deleted"""
    logger.warning(f"⚠️ Organization '{instance.name}' (ID: {instance.id}) was deleted.")
