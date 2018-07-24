from mapwidgets.widgets import GooglePointFieldWidget

class LocationsAdminForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = ('geographic_location')
        widgets = {
            'geographic_location': GooglePointFieldWidget,
        }
