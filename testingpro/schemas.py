from marshmallow import Schema


class TweetSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ("text", )
