"""
Module to provide a combined storage and data classes for specified data models.
The classes include pydantic validation of the data and storage of the data via
a selected storage class.


Available methods
'init_database'
    - method to define name and alias for the database
    - if needed host info and credentials can be added to the arguments

>>> configure_database(host="localhost", port=27017, username="user", password="pass")


available Dataclasses
- GeoNameDataClass, data class aimed at storing data from GeoNames website
- RetailLocationsDataClass, data class aimed at storing retail locations

avaialble fieldtypes (to be used to instantiatie specific dataclasses fields)
- PointField


Objects for discovery of available dataclasses
- ALL_MODEL_CLASSES: List with all data models
- ALL_GDG_MODEL_NAMES: List with class_names of all dataclasses.
- model_name_to_model: method to retrieve the actual data class for its name.
"""
