# models.py

This is a file used for reference when creating and manipulating models.

# Additional notes
## Models
### Migrating Models
When applying a change to any number of models, a migration must occur to save the changes. This can be done using
`$ python3 manage.py makemigrations` in the project root

This will create a new file called <nnnn>_<name>.py, which saves the migration details. (i.e., the first migration may be called `0001_initial.py`)

To finalize the migrations process, the command `$ python3 manage.py migrate` can be used in the project root.

### Reverting Migrations
To revert to a previous migration, we can use the command `$ python3 manage.py migrate <app_name> <migration_name>` in the project root, where `<app_name>`
is the app name, and `<migration_name>` is the number leading the migrations file. 

For example, say we have the following migrations for the app "Garden:"
- 0001_initial.py
- 0002_gardenmap.py
- 0003_gardenemployees.py

If we are currently in the latest migration and wish to go back to `0002_gardenmap.py`, then we will use the command `$ python3 migrate.py migrate Garden 0002`.

## Instances
### Creating Instances
An instance is like a collection of objects produced from values inputted into a Model. For example, if a model is like an outline, filling in the outline with values corresponding to a person or item (like a renter or a bike) produces an output known as an Instance of the Model. 

In `BikeModels.py`, this can be seen using the `Renter` model. The `Renter` model takes in the following values:
```py
first_name = models.CharField(max_length=30)
last_name = models.CharField(max_length=30)
phone = models.CharField(max_length=15)
vip_num = models.IntegerField(default=0)
```

After importing the model into bash, we can create an instance using the following code:
```bash
evan = Renter(first_name="Evan", last_name="Kimpton", phone="123-456-7890", vip_num=1)
```

This will create an instance of `Renter` named Evan.
