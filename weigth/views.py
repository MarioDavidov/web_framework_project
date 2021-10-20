from rest_framework import generics, mixins

from weigth.models import Weight
from weigth.serializers import WeigthSerializer


class WeighListtApiView(generics.ListCreateAPIView):
    queryset = Weight.objects.all()
    serializer_class = WeigthSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class WeightDetailsApiView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Weight.objects.all()
    serializer_class = WeigthSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
