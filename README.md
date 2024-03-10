#0x00. Airbnb clone - the console 


## content

* Introductuion
* starting the command interpreter
* Interpreter Usage
* Examples

<INTRODUCTION>

the project is a console interpreter for managing objects in an application similar to AIRBNB.
it allows users to create , display , edit objects like Users, places , reviews etc..


<STARTING THE CLI>

to start the commend line interpreter, just run/execute the following command

--------------------------
./console.py
-------------------------

<USAGE>

After running the CLI we can use the following commands.

-create <name>: Create the new instance of a specific class
-show <name><id>: display the details of the instance specified.
-destroy <name><id>: delete the instance specified
-all : display all instances
-update <name><id><attribute-name> <new-vale>: update the specified attribute of the specified
  instance using it's id

 <EXAMPLE>
----------------------------------------------------------------------------------------------------

/to create a new user/
----------------------------
 (hbnb) create User
----------------------------


/to show details of user/
----------------------------
(hbnb) show User <id>
----------------------------


/to delete a user instance/
----------------------------
(hbnb) destroy User <id>
----------------------------


/to update a user instance/
----------------------------
(hbnb) update User <id> name "Ayyoub EZ"
----------------------------


/to display All/
----------------------------
(hbnb) all User
----------------------------

------------------------------------------------------------------------------------------------------
