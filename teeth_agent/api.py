"""
Copyright 2013 Rackspace, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from teeth_rest.component import APIComponent, APIServer
from teeth_rest.responses import (
    ItemResponse
)


class TeethAgentAPI(APIComponent):
    """
    The primary Teeth Agent API.
    """

    def __init__(self, agent):
        super(TeethAgentAPI, self).__init__()
        self.agent = agent

    def add_routes(self):
        """
        Called during initialization. Override to map relative routes to methods.
        """
        self.route('GET', '/status', self.get_agent_status)

    def get_agent_status(self, request):
        """
        Get the status of the agent.
        """
        return ItemResponse(self.agent.get_status())


class TeethAgentAPIServer(APIServer):
    """
    Server for the teeth agent API.
    """

    def __init__(self, agent):
        super(TeethAgentAPIServer, self).__init__()
        self.add_component('/v1.0', TeethAgentAPI(agent))
