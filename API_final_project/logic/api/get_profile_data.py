import logging

from requests import RequestException

from infra.logging_basicConfig import LoggingSetup
from infra.api.response_wrapper import ResponseWrapper
from logic.api.base_init import BaseInit


class GetProfileData(BaseInit):
    def __init__(self, request):
        super().__init__(request)

    def get_profile_data_api_get(self, profile_username):
        """
        this function returns profile data using GET
        """
        try:
            return self._request.get_request(f"{self.config["base_url"]}/?username={profile_username}",
                                                    self.config["header"])

        except RequestException:
            logging.error("Error in receiving API data from 'get_profile_data' function")

