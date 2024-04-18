# Django-REST-Framework-CRUD-operations
DRF-based project is a RESTful API for managing posts and comments, with user authentication using JWT tokens and features like CRUD operations and liking/unliking posts and comments.

## Installation

1. **Clone the repository:**
   ```terminal
   git clone https://github.com/singhvikash99/Django-REST-Framework-CRUD-operations.git
3. **Navigate to the Repository Directory:**
   ```terminal
   cd Django-CRUD-project-
4. **Create and activate a virtual environment:**
   ```terminal
   python -m venv env
5. **Activate virtual environment:**
   ```terminal
   source env/bin/activate  # On Unix/macOS
   env\Scripts\activate    # On Windows
6. **Install dependencies:**
   ```terminal
   pip install -r requirements.txt
## Database Setup
1. **Apply migrations to create database tables:**
   ```terminal
   python manage.py migrate
## Running the Application
1. **Start the development server:**
   ```terminal
   python manage.py runserver
## Testing
1. **Run tests using the following command:**
   ```terminal
   python manage.py test
## Getting JWT Token
To authenticate and obtain a JWT token, you can follow these steps:
1. **Create a superuser:**
   ```terminal
   python manage.py createsuperuser
2. Obtain JWT Token:
   - Once you have created a superuser, you can obtain a JWT token by sending a POST request to the token endpoint with the superuser credentials.
     ```terminal
     curl -X POST -d "grant_type=password&username=<your_username>&password=<your_password>" http://localhost:8000/api/token/
## API Documentation
### Posts
#### List Posts
- **URL:** `/api/posts/`
- **Method:** `GET`
- **Description:** Retrieve a list of all posts.
- **Authentication:** Required (JWT Token)
   **Example:**
   ```terminal
   curl -X GET -H "Authorization: Bearer <your_access_token>" http://localhost:8000/api/posts/
**Output:**

    {
            "title": "post1",
            "content": "postcontent1",
            "author": 2,
            "published_date": "2024-04-15T15:47:35.208689Z",
            "likes": 0,
            "comments": [
                {
                    "id": 1,
                    "text": "new comment",
                    "created_date": "2024-04-15T15:48:43.189958Z",
                    "post": 1,
                    "author": 2
                },
                {
                    "id": 5,
                    "text": "new comment2",
                    "created_date": "2024-04-15T15:49:03.912435Z",
                    "post": 1,
                    "author": 2
                },
                {
                    "id": 6,
                    "text": "new comment3",
                    "created_date": "2024-04-15T15:49:08.439367Z",
                    "post": 1,
                    "author": 2
                }
#### Create Posts
- **URL:** `/api/posts/`
- **Method:** `POST`
- **Description:** Create a new post.
- **Request Body**: JSON object containing post data (title, content)
- **Authentication:** Required (JWT Token)
   **Example:**
   ```terminal
   curl -X POST -H "Authorization: Bearer <your_access_token>" -H "Content-Type: application/json" -d '{"title": "New Post", "content": "This is the content of the new post"}' http://localhost:8000/api/posts/
**Output:**

    {
        "title": "New Post",
        "content": "This is the content of the new post",
        "author": 1,
        "published_date": "2024-04-14T04:56:08.508546Z",
        "likes": 0
        "comments": []
    }
#### Retrive Posts
- **URL:** `/api/posts/<post_id>/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific post by its ID.
- **Request Parameters:** `<post_id>` (path parameter): The unique identifier of the post to retrieve.
- **Authentication:** Required (JWT Token)
   **Example:**
   ```terminal
   curl -X GET -H "Authorization: Bearer <your_access_token>" http://localhost:8000/api/posts/<post_id>/
**Output:**

    {
       "title": "testpost3",
       "content": "testpost content3",
       "author": 1,
       "published_date": "2024-04-18T01:06:57.498070Z",
       "likes": 0,
       "comments": []
    }
#### Update Posts
- **URL:** `/api/posts/<post_id>/`
- **Method:** `PUT`
- **Description:** Update an existing post.
- **Request Body**: JSON object containing updated post data (title, content)
- **Request Parameters:** `<post_id>` (path parameter): The unique identifier of the post to update.
- **Authentication:** Required (JWT Token)
   **Example:**
   ```terminal
   curl -X PUT -H "Authorization: Bearer <your_access_token>" -H "Content-Type: application/json" -d '{"title": "Updated Title", "content": "Updated Content"}' http://localhost:8000/api/posts/<post_id>/
**Output:**

    {
        "title": "Updated Post",
        "content": "Updated Content",
        "author": "1",
        "published_date": "2024-04-14T04:42:03.584415Z",
        "likes": 0"
        "comments": []
        
    }
#### Deleting a Post
- **URL:** `/api/posts/<post_id>/`
- **Method:** `DELETE`
- **Description:** Delete an existing post.
- **Request Parameters:** `<post_id>` (path parameter): The unique identifier of the post to delete.
- **Authentication:** Required (JWT Token)
   **Example:**
   ```terminal
   curl -X DELETE -H "Authorization: Bearer <your_access_token>" http://localhost:8000/api/posts/<post_id>/
### Comments
#### Create Comments
- **URL:** `/api/posts/<post_id>/comments/`
- **Method:** `POST`
- **Description:** Create a new comment for a post.
- **Request Body:** JSON object containing comment data (text)
- **Request Parameters:** <post_id> (path parameter): The unique identifier of the post to retrieve comments for.
- **Authentication:** Required (JWT Token)
   **Example:**
   ```terminal
  curl -X POST -H "Authorization: Bearer <your_access_token>" -H "Content-Type: application/json" -d '{"text": "New Comment"}' http://localhost:8000/api/posts/<post_id>/comments/
**Output:**     

    {
        "id": 1,
        "text": "new comment",
        "created_date": "2024-04-14T04:51:01.377272Z",
        "post": 1,
        "author": 1
    }
#### List Comments
- **URL:** `/api/posts/<post_id>/comments/`
- **Method:** `GET`
- **Description:** Retrieve a list of all comments for a post.
- **Request Parameters:** <post_id> (path parameter): The unique identifier of the post to retrieve comments for.
- **Authentication:** Required (JWT Token)
   **Example:**
   ```terminal
  curl -X POST -H "Authorization: Bearer <your_access_token>" -H "Content-Type: application/json" -d '{"text": "New Comment"}' http://localhost:8000/api/posts/<post_id>/comments/
**Output:**     

    {
        "id": 1,
        "text": "new comment",
        "created_date": "2024-04-14T04:51:01.377272Z",
        "post": 1,
        "author": 1
    }
#### Retrieve Comment Details
- **URL:** `/api/posts/<post_id>/comments/<comment_id>/`
- **Method:** `GET`
- **Description:** Retrieve details of a specific comment.
- **Request Parameters:** <post_id> (path parameter): The unique identifier of the post containing the comment.<comment_id> (path parameter): The unique identifier of the comment to retrieve details for.
- **Authentication:** Required (JWT Token)
   **Example:**
   ```terminal
  curl -X GET -H "Authorization: Bearer <your_access_token>" http://localhost:8000/api/posts/<post_id>/comments/<comment_id>/
**Output:**    

    {
        "id": 1,
        "text": "new comment",
        "created_date": "2024-04-14T04:51:01.377272Z",
        "post": 1,
        "author": 1
    }
#### Update Comment
- **URL:** `/api/posts/<post_id>/comments/<comment_id>/`
- **Method:** `PUT`
- **Description:** Update an existing comment.
- **Request Body:** JSON object containing updated comment data (text)
- **Request Parameters:** <post_id> (path parameter): The unique identifier of the post containing the comment.<comment_id> (path parameter): The unique identifier of the comment to update.
- **Authentication:** Required (JWT Token)
   **Example:**
   ```terminal
  curl -X PUT -H "Authorization: Bearer <your_access_token>" -H "Content-Type: application/json" -d '{"text": "Updated Comment"}' http://localhost:8000/api/posts/<post_id>/comments/<comment_id>/
**Output:**    

    {
        "id": 1,
        "text": "new comment",
        "created_date": "2024-04-14T04:51:01.377272Z",
        "post": 1,
        "author": 1
    }
#### Delete Comment
- **URL:** `/api/posts/<post_id>/comments/<comment_id>/`
- **Method:** `DELETE`
- **Description:** Delete a comment.
- **Request Parameters:** <post_id> (path parameter): The unique identifier of the post containing the comment.<comment_id> (path parameter): The unique identifier of the comment to delete.
- **Authentication:** Required (JWT Token)
   **Example:**
   ```terminal
  curl -X DELETE -H "Authorization: Bearer <your_access_token>" http://localhost:8000/api/posts/<post_id>/comments/<comment_id>/
### Likes
#### Like Post
- **URL:** `/api/posts/<post_id>/like/`
- **Method:** `POST`
- **Description:** Like a post.
- **Request Parameters:** <post_id> (path parameter): The unique identifier of the post to like.
- **Authentication:** Required (JWT Token)
   **Example:**
   ```terminal
  curl -X POST -H "Authorization: Bearer <your_access_token>" http://localhost:8000/api/posts/<post_id>/like/
**Output:**    

    {
        "message": "Post liked successfully"
    }
#### Unlike Post
- **URL:** `/api/posts/<post_id>/like/`
- **Method:** `POST`
- **Description:** Unlike a post.
- **Request Parameters:** <post_id> (path parameter): The unique identifier of the post to unlike.
- **Authentication:** Required (JWT Token)
   **Example:**
   ```terminal
  curl -X POST -H "Authorization: Bearer <your_access_token>" http://localhost:8000/api/posts/<post_id>/like/
**Output:**  

    {
        "message": "Post unliked successfully"
    }
#### Like Comment
- **URL:** `/api/comments/<comment_id>/like/`
- **Method:** `POST`
- **Description:** Like a comment.
- **Request Parameters:** <comment_id> (path parameter): The unique identifier of the comment to like.
- **Authentication:** Required (JWT Token)
   **Example:**
   ```terminal
  curl -X POST -H "Authorization: Bearer <your_access_token>" http://localhost:8000/api/comments/<comment_id>/like/
**Output:**  

    {
        "message": "Comment liked successfully"
    }
#### Unlike Comment

- **URL:** `/api/comments/<comment_id>/unlike/`
- **Method:** `POST`
- **Description:** Unlike a comment.
- **Request Parameters:** <comment_id> (path parameter): The unique identifier of the comment to unlike.
- **Authentication:** Required (JWT Token)
   **Example:**
   ```terminal
  curl -X POST -H "Authorization: Bearer <your_access_token>" http://localhost:8000/api/comments/<comment_id>/unlike/
**Output:**  

      {
          "message": "Comment unliked successfully"
      }








Remember to replace <your_access_token> with your actual JWT token. Happy testing! 🚀🔍


