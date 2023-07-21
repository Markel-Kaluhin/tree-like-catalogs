## Instructions on how to run each part of the challenge.
### Prerequisites:
> To launch all parts of the application, namely the database, server, and WebUI at once, you need to use Docker Compose. The entire system is designed so that the user worries as little as possible about infrastructure matters.

1. First, install Docker Compose. The page contains links to instructions for all common operating systems.
1. Navigate to the root directory of the project.
1. At this stage, please make sure that ports 80, 8080, and 5432 are available at the time of running my solution. They are all necessary for the application to work.
1. Execute the command docker-compose up.
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

## Brief description of key challenges
### Frontend side
1. Since I was given two test tasks, I nevertheless integrated the client application with the server side

### Backend side
1. Instead of the described protocol, I developed my own, which provided a high level of entity control, reentrancy and reduced the complexity of the algorithms for its maintenance. That is, instead of this:
```
• "Engine1":
    • "Thrust": 9.493
    ...
```
I did this:
```
{
    "id": 6,
    "parentId": 4,
    "name": "Engine1",
    "children": [],
    "properties": [
        {
          "id": 1,
          "name": "Thrust",
          "value": 9.493,
          "createdAt": "2023-07-21T04:24:50.967985+00:00"
        }
    ],
    "createdAt": "2023-07-21T04:24:50.967985+00:00"
}
```
3. Slightly changed the structure of the API to avoid conflicts with important tools that I use in my work, such as Swagger. You can find the description of the API at this address `http://0.0.0.0:8080/docs`. Added `/api/rocket/construction` to all endpoints of the task at the beginning
   1. Where is `api` to avoid conflict with Swagger
   1. `rocket` to define the business object we are working with within this API
   1. `construction` to avoid conflict with endpoints described below
1. Added two new endpoints `/api/rocket/node/{node_id}` and `/api/rocket/property/{property_id}` with `HTTP` methods `DELETE` to delete properties and nodes
1. Enriched the data model with the createdAt field because it was necessary to complete the frontend task, although it was not listed in the backend task

## Solution caveats and potential downfall
Due to time constraints in the middle of the week, I had to make some choices, and one of the sacrifices I made was skipping unittests, which I usually write.

However, I still took precautions and carefully tested my API for any unexpected behavior by making numerous requests with different scenarios. I addressed all the issues I encountered during testing.

As for the UI's interaction with the backend, I'm not overly concerned about unexpected behavior because the client doesn't utilize many of the API's capabilities. Therefore, I believe it should work smoothly for the specific use cases it handles.

## What I'd do differently in a production environment
1. I'd focus on improving the UI design to enhance the readability of elements. The current level is sufficient to demonstrate my skills and meet the immediate requirements, but it may not be enough for an industrial environment with numerous users
1. Implement notifications for successful and unsuccessful operations on the UI, displaying them as toasts
1. Write unit tests for all parts of the application, along with integration tests. I frequently use them to ensure the quality and reliability of my solutions
1. Describe CI/CD based on either a version control system or specialized solutions
1. Reworked the method `apps.rocket.repository.RocketRepository.get_latest_node_id` to change the recursive requests to the subqueries set
1. Would deploy an application in Kubernetes or Swarm in one of the clouds
