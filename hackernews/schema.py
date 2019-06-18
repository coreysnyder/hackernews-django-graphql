import graphene
import graphql_jwt

import links.schema
import users.schema

class Query(links.schema.Query, users.schema.Query, graphene.ObjectType):
    pass


class Mutation(
    users.schema.Mutation, links.schema.Mutation, graphene.ObjectType,):

    # These 3 lines expose 3 new endpoints for us to use for Auth.
    # Given a username and password it returns a JSON Web token
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # To confirm that the token is valid, passing it as an argument.
    verify_token = graphql_jwt.Verify.Field()
    # Lets us obtain a new token within the renewed expiration
    refresh_token = graphql_jwt.Refresh.Field()

    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
