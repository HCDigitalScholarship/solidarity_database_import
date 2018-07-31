# solidarity_database_import
Solidarity-database-import is a database admin application for the Solidarity Economy project. It builds on *Django-import-export* so that users can not only simply create, read, update, or delete the data, but also import a large number of new data or export existing data in CSV format for certain tables (ex. ‘contacts’, ‘organizations’, ‘locations’). And this app makes good use of the workflow of Django-import-export to customize certain functions: (1) It incorporates with *GeoDjango* and *Geocoding* --when users import location data, the app will auto-generate the values for Pointfield based on the address information provided in the importing file, and display them on the google map widget; (2) When importing NCUA’s location data, the app will delete the old entries which are not in the importing file. It also uses *Proxy model* to create another admin interface for the same database, to satisfy different requirements of the data of different sub-types.

For more information about how this application works, please go to our [Wiki documentation](https://github.com/HCDigitalScholarship/solidarity_database_import/wiki).
