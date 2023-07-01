from django.shortcuts import get_list_or_404
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import NotificationAccount
from .serializers import NotificationAccountSerializer


class PersonalNotificationViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                                  mixins.UpdateModelMixin, viewsets.GenericViewSet):
    """
    View set for notifications.
    """

    serializer_class = NotificationAccountSerializer
    queryset = NotificationAccount.objects.all()

    @action(
        detail=True,
        methods=[
            'post',
        ],
        url_path='viewed',
    )
    def viewed(self, request, **kwargs):
        """
        Mark notification as viewed.
        """

        notification = get_list_or_404(NotificationAccount, id=kwargs['pk'])
        notification[0].is_viewed()
        return Response(NotificationAccountSerializer(notification).data)
