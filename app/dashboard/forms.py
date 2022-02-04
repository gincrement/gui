from crispy_forms.helper import FormHelper
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from dashboard.models import (
    ReportItem,
    GRAPH_TIMESERIES,
    GRAPH_TIMESERIES_STACKED,
    GRAPH_CAPACITIES,
    GRAPH_BAR,
    GRAPH_PIE,
    GRAPH_LOAD_DURATION,
    GRAPH_SANKEY,
)
from dashboard.helpers import KPI_PARAMETERS
from projects.models import ENERGY_VECTOR, Project


class ReportItemForm(ModelForm):

    scenarios = forms.MultipleChoiceField(label=_("Scenarios"))

    def __init__(self, *args, **kwargs):
        proj_id = kwargs.pop("proj_id", None)
        super().__init__(*args, **kwargs)

        if proj_id is not None:
            project = Project.objects.get(id=proj_id)
            self.fields["scenarios"].choices = [
                c
                for c in project.get_scenarios_with_results().values_list("id", "name")
            ]

        # TODO here set multiple choice for scenarios on or off depending on the report_type
        self.fields["scenarios"].widget.attrs = {"multiple": False}

    class Meta:
        model = ReportItem
        fields = ["report_type", "title"]
        labels = [_("Type of report item"), _("Title")]

    field_order = ["scenarios", "report_type", "title"]


class TimeseriesGraphForm(forms.Form):
    vector = forms.ChoiceField(
        label=_("Energy vector"), choices=ENERGY_VECTOR, initial=ENERGY_VECTOR[1][0]
    )
    y = forms.MultipleChoiceField(
        label=_("Timeseries variable(s)"),
        choices=tuple([(k, KPI_PARAMETERS[k]["verbose"]) for k in KPI_PARAMETERS]),
    )


def graph_parameters_form_factory(report_type, *args, **kwargs):
    if report_type == GRAPH_TIMESERIES:
        answer = TimeseriesGraphForm(*args, **kwargs)
    # GRAPH_TIMESERIES_STACKED,
    # GRAPH_CAPACITIES,
    # GRAPH_BAR,
    # GRAPH_PIE,
    # GRAPH_LOAD_DURATION,
    # GRAPH_SANKEY,
    return answer
