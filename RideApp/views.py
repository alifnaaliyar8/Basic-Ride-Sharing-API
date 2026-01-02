import jwt
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed, PermissionDenied
from RideApp.models import Ride
from RideApp.serializers import RideSerializer, RideStatusSerializer, RideTrackingSerializer
from AuthApp.models import User

# Create your views here.

class RideViewSet(ModelViewSet):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer

    def get_user_from_token(self, request):
        token = request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Unauthenticated")

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except:
            raise AuthenticationFailed("Unauthenticated")

        user = User.objects.get(id=payload['id'])
        return user


    def create(self, request, *args, **kwargs): #  Create Ride
        user = self.get_user_from_token(request)

        serializer = RideSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(rider=user)

        return Response(serializer.data)


    @action(detail=True, methods=['post']) # Driver accepts ride
    def accept_ride(self, request, pk=None):
        user = self.get_user_from_token(request)
        ride = self.get_object()

        if ride.status != 'requested':
            return Response({"error": "Ride already accepted"})

        ride.driver = user
        ride.status = 'accepted'
        ride.save()

        return Response({"message": "Ride accepted"})


    @action(detail=True, methods=['patch']) #  Update ride status
    def update_status(self, request, pk=None):
        user = self.get_user_from_token(request)
        ride = self.get_object()

        if user != ride.driver:
            raise PermissionDenied("Only driver can update status")

        serializer = RideStatusSerializer(ride, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    @action(detail=True, methods=['patch'])
    def track(self, request, pk=None):
        self.get_user_from_token(request)  # auth check
        ride = self.get_object()

        serializer = RideTrackingSerializer(ride, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)




