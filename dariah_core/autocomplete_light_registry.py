"""
    DARIAH Contribute - DARIAH-EU Contribute: edit your DARIAH contributions.

    Copyright 2014 Data Archiving and Networked Services

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

from django.template.loader import render_to_string

from taggit.models import Tag
from .models import DcCreator, DcContributor

import autocomplete_light


class DcCreatorAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['^first_name', 'last_name_prefix', 'last_name']
    model = DcCreator
    add_another_url_name = 'dariah_core:dccreator_create'

    attrs = {
        # This will set the input placeholder attribute:
        'placeholder': 'Start typing...',
        # This will set the yourlabs.Autocomplete.minimumCharacters
        # options, the naming conversion is handled by jQuery
        'data-autocomplete-minimum-characters': 1,
    }
    widget_attrs = {}

    @property
    def empty_html_format(self):
        data = {'model': self.model.lowercase_underscore_name(),
                'url': self.add_another_url_name}
        return render_to_string('dariah_core/_creator-contrib_autocomplete_empty_html_format.html', data)


class DcContributorAutocomplete(DcCreatorAutocomplete):
    model = DcContributor
    add_another_url_name = 'dariah_core:dccontributor_create'


autocomplete_light.register(Tag)
autocomplete_light.register(DcCreator, DcCreatorAutocomplete)
autocomplete_light.register(DcContributor, DcContributorAutocomplete)
