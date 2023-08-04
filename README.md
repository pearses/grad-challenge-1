CRUD RestAPI Software Engineering Challenge

 

Introduction

 

In this software engineering challenge, you will be tasked with creating a CRUD (Create, Read, Update, Delete) RestAPI for a single database table.

The goal is to demonstrate your understanding of RESTful API principles, database operations, and software design best practices.

 

Requirements

 

1. Use either springboot or flask framework to build the RestAPI.

 

2. Choose a single database table to work with. The table should have at least the following fields:

   - `id` (unique identifier for each record)

   - `name` (string, representing the name of an item)

   - `description` (string, providing additional information about the item)

   - You can add more fields if you wish, but the above three are mandatory.

 

3. Implement the following endpoints:

 

   - Create (HTTP POST):

     - Endpoint: `/items`

     - Description: Allows the user to create a new item by providing the `name` and `description` in the request body.

     - Response: Returns the created item with its unique `id`.

 

   - Read (HTTP GET):

     - Endpoint: `/items/:id`

     - Description: Retrieves the details of a specific item by providing its unique `id`.

     - Response: Returns the item's details (including `name`, `description`, and `id`) if it exists, or an appropriate error message if not found.

 

   - Update (HTTP PUT or PATCH):

     - Endpoint: `/items/:id`

     - Description: Allows the user to update an existing item's `name` and/or `description` by providing the updated values in the request body. The `id` should remain unchanged.

     - Response: Returns the updated item.

 

   - Delete (HTTP DELETE):

     - Endpoint: `/items/:id`

     - Description: Deletes an item with the provided `id`.

     - Response: Returns a success message or an appropriate error message if the item doesn't exist.

 

4. Properly handle error cases, such as invalid requests, non-existent items, or server errors.

 

5. Use swagger to explain and demo how to use your RestAPI, including the endpoints, expected request and response formats, and any additional details.

 

6. Use best practices for code organization, security, and error handling.

 

Submission

 

Once you complete the challenge, create a public GitHub repository and upload your code, along with the documentation, to the repository. Share the repository link with the team.

 

Evaluation

 

Your submission will be evaluated based on the following criteria:

 

- Functionality: Does the RestAPI fulfill the CRUD requirements for the chosen database table?

- Code Quality: Is the code well-organized, maintainable, and follows best practices?

- Error Handling: Are errors handled gracefully, with appropriate error messages?

- Documentation: Is the documentation clear, detailing the endpoints, request/response formats, and any other relevant information?

- Overall Design: Does the RestAPI demonstrate good software design principles?