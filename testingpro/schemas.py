from marshmallow import Schema


# Schema for user tweets
class TweetSchema(Schema):
    class Meta:
        # Fields to expose
        fields = ("text", )
