# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI and Pydantic models. Students will practice defining routes, handling JSON payloads, using path and query parameters, and returning proper HTTP responses.

## 📝 Tasks

### 🛠️ Create the FastAPI application

#### Description
Use `starter-code.py` to define a FastAPI app, set up an in-memory item list, and create reusable data models with Pydantic.

#### Requirements
Completed program should:

- Define a Pydantic `Item` model with fields for `id`, `name`, `description`, `price`, and `in_stock`.
- Create a FastAPI app instance in `starter-code.py`.
- Use an in-memory list of item data as the application data store.
- Include instructions for running the app with `uvicorn`.

### 🛠️ Implement REST endpoints

#### Description
Add API routes for listing, creating, retrieving, updating, and deleting items.

#### Requirements
Completed program should:

- Provide a `GET /items` endpoint that returns all items.
- Provide a `GET /items/{item_id}` endpoint that returns a single item by ID.
- Provide a `POST /items` endpoint that accepts JSON data and adds a new item.
- Provide a `PUT /items/{item_id}` endpoint that updates an existing item.
- Provide a `DELETE /items/{item_id}` endpoint that removes an item.
- Return the correct HTTP status codes for success and error cases.

### 🛠️ Handle validation and error responses

#### Description
Ensure the API validates incoming data and responds clearly when an item cannot be found or a request is invalid.

#### Requirements
Completed program should:

- Use FastAPI and Pydantic validation to parse request bodies.
- Return a `404` response for missing item IDs.
- Return a `400` response when attempting to create an item with a duplicate ID.
- Keep the application logic organized in functions where appropriate.
