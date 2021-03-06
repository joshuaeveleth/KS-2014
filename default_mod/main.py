#
# Copyright 2013 National MEdiation Board.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Defines the routing for the app's non-admin handlers.
"""

from searchserver import *
import webapp2

"""handlers for client redirects"""
class SearchHandler(webapp2.RequestHandler):
  def get(self):
  	# self.redirect("ks/search.html")
    self.redirect("ks/build.html")

app = webapp2.WSGIApplication(
    [('/', SearchHandler),
    ('/kssearch', KSSearch)
    ],
    debug=True)