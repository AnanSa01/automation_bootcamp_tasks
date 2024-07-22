import logging

from requests import RequestException

from infra.api.response_wrapper import ResponseWrapper
from infra.logging_basicConfig import LoggingSetup

from logic.api.base_init import BaseInit


class GetProfilePostsComments(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_profile_posts_comments_api_get(self, profile_urn):
        """
        this function returns profile posts comments using GET
        """
        try:
            response = self._request.get_request(
                f"{self.config["base_url"]}/get-profile-posts-comments?urn={profile_urn}&sort=mostRelevant",
                self.config["header"])

            return ResponseWrapper(ok=response.ok, status_code=response.status_code, body=response.json())

        except RequestException:
            logging.error("Error in receiving API data from 'get_profile_posts_comments' function")
