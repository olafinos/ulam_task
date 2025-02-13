from .serializers import DecodeSerializer, EncodeSerializer
from weird_text_app.weird_text.encoder import WeirdTextEncoder
from weird_text_app.weird_text.decoder import WeirdTextDecoder
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.schemas.coreapi import AutoSchema, coreapi, coreschema


class EncodeView(APIView):
    """
    post:
    Encode given text.
    """

    schema = AutoSchema(
        manual_fields=[
            coreapi.Field(
                name="text",
                required=True,
                location="body",
                description='{"text":str}',
                schema=coreschema.Object(),
            )
        ]
    )

    def post(self, request, format=None):
        serializer = EncodeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            encoder = WeirdTextEncoder(serializer.data["text"])
            return Response({"encoded_text": encoder.encode()}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class DecodeView(APIView):
    """
    post:
    Decode given text.
    """

    schema = AutoSchema(
        manual_fields=[
            coreapi.Field(
                name="text",
                required=True,
                location="body",
                description='{"text":str}',
                schema=coreschema.Object(),
            )
        ]
    )

    def post(self, request, format=None):
        serializer = DecodeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                decoder = WeirdTextDecoder(serializer.data["text"])
                return Response({"decoded_text": decoder.decode()}, status=HTTP_200_OK)
            except ValueError as error:
                return Response(serializer.data["text"], status=HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
