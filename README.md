# djangoDemoProject
A Project demonstrating understanding of the Django framework.

# Prerequisites
Python with django, python-dotenv, psycopg2 installed
PostGreSQL installed, database and user created for application

# Details
## Structure
The project uses a template structure where a main single page is used as a "shell" for content. This is done so that, in a production setting, SEO information and other metadata can be set to either use a Django context for certain values (i.e. page titles, oembed data, summary info, etc.).

Every component has its particular javascript and css that it needs tied directly to it. In a situation where the app is larger, I would use static files to maintain scripts.

The application serves server-side-rendered (i.e. template rendered) data when it is being retrieved, and uses API endpoints for other interactions. This is done this way because it allows for more precise data management - In case of this application, pagination is done on the server side so that clients benefit from the speed of paginated data.

The "New User" page uses a validation "Rule Engine" pattern to evaluate rules and dynamically handle a variety of validation cases. The ones included only check if fields are not empty, and one that validates that the ZIP Code is in the correct format.

