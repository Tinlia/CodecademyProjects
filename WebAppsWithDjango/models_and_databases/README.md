# models.py

This is a file used for reference when creating and manipulating models.

## Additional notes
### Migrating Models
When applying a change to any models, a migration must occur to save the changes. this can be done using
`$ python3 manage.py makemigrations` in the project root

This will create a new file called 0001_name.py which saves the migration details.

To finalize the migrations process, the command `$ python3 manage.py migrate` can be used in the project root.

### Reverting Migrations
To revert to a previous migration, we can use the command `$ python3 manage.py migrate <app_name> <migration_name>` in the project root, where `<app_name>`
is the app name, and `<migration_name>` is the number leading the migrations file. 

For example, say we have the following migrations for the app "Garden:"
- 0001_initial.py
- 0002_gardenmap.py
- 0003_gardenemployees.py

If we are currently in the latest migration and wish to go back to `0002_gardenmap.py`, then we will use the command `$ python3 migrate.py migrate Garden 0002`.
