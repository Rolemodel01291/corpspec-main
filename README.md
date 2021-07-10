# corpspec-main
Corpspec which is a python / Django app feeding genbase via API.

The project is a tool for companies to manage their contracts and policies for their different activities.
A typical workflow is for a user to fill in a form and the system will output a html that converts into a pdf that an end user can sign as part of the contract.
In the system there are also events which is a collection of activities and contracts that need to be signed together.

1) Do up the companies / subsidies folders.
	Within a users account, we want to allow users to manage multiple companies, either as a law firm on behalf of their clients or a HQ for their subsidies.
	A departments model has been created in genbase using https://django-mptt.readthedocs.io/en/latest/.
	I need you to do the API to CRUD a simple tree of companies.

	Tree Examples	https://reactjsexample.com/tag/tree/
	
2) KYC
	The following is an example of a tool where the user will be verified an account created for them.
	https://www.datazoo.com/

3) PDF signing after review.
	Again, an API to allow the user to enter in their PDF.
