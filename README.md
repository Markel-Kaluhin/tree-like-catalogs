![Tests Pass Badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Markel-Kaluhin/e8d23650144c1dd611a941789d52721a/raw/tree-like-catalogs__tests_passed.json)
![Coverage Badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/Markel-Kaluhin/e8d23650144c1dd611a941789d52721a/raw/tree-like-catalogs__coverage.json)

# 🌳 Tree-like Catalogs
*Designed by Markel Kaluhin 🎨*

Email: [_markel.kaluhin@gmail.com_](mailto:markel.kaluhin@gmail.com) 📧


## Description

The project showcases a data management system for components of complex assemblies, organized in a tree-like structure. It allows efficient handling and organization of data related to various components and their relationships within complex assemblies.

### Key Features
1. Efficient Data Representation
   - **Description**: Representing components of complex assemblies in a structured and intuitive tree format.
   - **Implementation**: Utilizing a tree data structure to efficiently organize and visualize the relationships between components.

1. Node Creation and Modification
   - **Description**: Capability to create, edit, and manage nodes representing individual components or sub-assemblies within the system.
   - **Implementation**: API endpoints allowing for the creation and modification of nodes and their attributes.
 
1. Relationship Mapping
   - **Description**: Mapping and managing relationships between different components, providing insights into the structure of complex assemblies.
   - **Implementation**: Enabling the creation and visualization of relationships between nodes within the tree structure.

1. Streamlined Data Access
   - **Description**: Ensuring quick and easy access to relevant data for components, facilitating efficient decision-making and analysis.
   - **Implementation**: Implementing APIs that enable swift retrieval and updating of component data.

1. Error Handling and Validation
   - **Description**: Implementing a robust system to handle errors and validate user inputs to maintain data integrity and accuracy.
   - **Implementation**: Incorporating validation checks and error handling mechanisms within the API to provide a reliable user experience.


## Instructions on how to run each part of the challenge.
### Prerequisites:
> To launch all parts of the application, namely the database, server, and WebUI at once, you need to use Docker Compose. The entire system is designed so that the user worries as little as possible about infrastructure matters.

1. First, install Docker Compose. The page contains links to instructions for all common operating systems.
1. Navigate to the root directory of the project.
1. At this stage, please make sure that ports 80, 8080, and 5432 are available at the time of running my solution. They are all necessary for the application to work.
1. Execute the command **`docker-compose up`**.
1. Wait for all services to be built, and migrations to be applied.
1. Open your browser and go to http://0.0.0.0 to see the results of the test task.

## Brief description of rationale behind each tool/language/framework of choice.
### Frontend side
- **Angular 16** - I have a lot of experience with it, I like working with it, and it is perfect for the task
- **@ng-bootstrap/ng-bootstrap** - In order to make it possible to quickly implement modal windows, sidebars and other things that I needed to complete the task
- **@ngrx/[data, effects, entity, store]** - To provide the most optimal data class structure, context management, and stable event model

### Backend side
- **fastapi** - Firstly, because it was indicated in the position description, and secondly, because this is my favorite framework and I had to show you how I can work with it
- **fastapi-utils** - To use CVB (Class Based Views)
- **uvicorn** - Needed to run the Starlette app
- **sqlalchemy** - ORM to provide an adequate object model for the application I'm working with
- **pydantic** - Serialization / validation. They are essential; without them, nothing can be achieved
- **asyncpg** - Asynchronous database driver for asynchronous framework
- **dependency-injector** - An alternative to the built-in dependency injector that is head and shoulders above the feature set
- **humps** - Advanced text preprocessor for converting snakecase to camelcase and vice versa. For integration with WebUI
- **greenlet** - Required as one of the third party dependencies for FastAPI
- **gunicorn** - Used as application server
- **alembic** - Migration manager, has the ideal integration with SQLAlchemy
- **coverage, flake8, isort, mypy, pre, pylint, pytest, black** - My gentleman's set of linters, no one project could be bootstrapped without it

# 📝 API Description

>This API is built using FastAPI and follows the OpenAPI 3.1.0 specification.

## Endpoints

### Get Tree
- **Endpoint:** `/api/non_flat_attrs/construction/{route_path}`
- **HTTP Method:** GET
- **Summary:** Get the tree structure.
- **Parameters:**
  - `route_path` (Path, String, Required): Route path for the construction.
- **Responses:**
  - 200: Successful response. Returns the tree structure in JSON format.
  - 422: Validation error. Returns detailed validation errors in JSON format.

### Create Node
- **Endpoint:** `/api/non_flat_attrs/construction/{route_path}`
- **HTTP Method:** POST
- **Summary:** Create a new node.
- **Parameters:**
  - `route_path` (Path, String, Required): Route path for the construction.
- **Request Body:**
  - JSON body with the properties of the node.
- **Responses:**
  - 200: Successful response. Returns the created node in JSON format.
  - 422: Validation error. Returns detailed validation errors in JSON format.

### Delete Node
- **Endpoint:** `/api/non_flat_attrs/node/{node_id}`
- **HTTP Method:** DELETE
- **Summary:** Delete a node by ID.
- **Parameters:**
  - `node_id` (Path, Integer, Required): Node ID.
- **Responses:**
  - 200: Successful response. Returns `true` if the node was successfully deleted.
  - 422: Validation error. Returns detailed validation errors in JSON format.

### Delete Property
- **Endpoint:** `/api/non_flat_attrs/property/{property_id}`
- **HTTP Method:** DELETE
- **Summary:** Delete a property by ID.
- **Parameters:**
  - `property_id` (Path, Integer, Required): Property ID.
- **Responses:**
  - 200: Successful response. Returns `true` if the property was successfully deleted.
  - 422: Validation error. Returns detailed validation errors in JSON format.

### Health Check
- **Endpoint:** `/health`
- **HTTP Method:** GET
- **Summary:** Check the health of the API.
- **Responses:**
  - 200: Successful response. Returns the health status in JSON format.

## Data Models

### NonFlatAttrsNodeSchema
- **Description:** Base model representing a node in the non-flat attributes tree.
- **Properties:**
  - `id` (Integer): Node ID.
  - `parentId` (Integer): Parent Node ID.
  - `name` (String): Node name.
  - `children` (Array): Children nodes.
  - `properties` (Array): Properties of the node.
  - `createdAt` (String): Date and time of creation.
- **Required Properties:** `id`, `name`, `createdAt`

### NonFlatAttrsPropertyCreateSchema
- **Description:** Base model for creating a property for a node in the non-flat attributes tree.
- **Properties:**
  - `id` (Integer): Property ID.
  - `name` (String): Property name.
  - `value` (Number): Property value.
- **Required Properties:** `name`, `value`

### NonFlatAttrsPropertySchema
- **Description:** Base model representing a property of a node in the non-flat attributes tree.
- **Properties:**
  - `id` (Integer): Property ID.
  - `name` (String): Property name.
  - `value` (Number): Property value.
  - `createdAt` (String): Date and time of creation.
- **Required Properties:** `name`, `value`, `createdAt`
