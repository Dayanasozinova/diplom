from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver, Signal
from django.db.models.signals import post_save
from backend.models import ConfirmEmailToken, User

new_user_registered = Signal()
new_order = Signal()


@receiver(post_save, sender=User)
def password_reset_token_created(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)

    msg = EmailMultiAlternatives(
        f"Password Reset Token for {created.user}",
        created.key,
        settings.EMAIL_HOST_USER,
        [created.user.email])
    msg.send()


@receiver(post_save, sender=User)
def new_user_registered_signal(user_id, **kwargs):
    """
    отправляем письмо с подтрердждением почты
    """
    token = ConfirmEmailToken.objects.get_or_create(user_id=user_id)

    msg = EmailMultiAlternatives(
        f"Password Reset Token for {token.user.email}",
        token.key,
        settings.EMAIL_HOST_USER,
        [token.user.email])
    msg.send()

@receiver(new_order)
def new_order_signal(user_id, **kwargs):
    """
    отправяем письмо при изменении статуса заказа
    """
    user = User.objects.get(id=user_id)

    msg = EmailMultiAlternatives(
        f"Обновление статуса заказа",
        'Заказ сформирован',
        settings.EMAIL_HOST_USER,
        [user.email])
    msg.send()
