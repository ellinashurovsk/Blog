

| **Endpoint**                             | **Request** | **Definition**                                    | **Authentication** | **Permission**  | **In data**                                                                     |
|------------------------------------------|-------------|---------------------------------------------------|--------------------|-----------------|---------------------------------------------------------------------------------|
| http://127.0.0.1:8000/auth/token         | POST        | Return an access and refresh JSON web token pair. | -                  | -               | Required: [username, password]                                                  |
| http://127.0.0.1:8000/auth/token/refresh | POST        | Return an access type JSON web token.             | -                  | -               | Required: [refresh]                                                             |
|                                          |             |                                                   |                    |                 |                                                                                 |
| http://127.0.0.1:8000/user/              | GET         | Return all existing users ordered by id.          | JWTAuthentication  | IsAdminUser     |                                                                                 |
| http://127.0.0.1:8000/user/register      | POST        | Create a new user.                                | -                  | AllowAny        | Required: [username, password]  <br /> Optional: [first_name, last_name, email] |
| http://127.0.0.1:8000/user/<int:id>      | GET         | Return a user by it's id.                         | JWTAuthentication  | IsAuthenticated |                                                                                 |
| http://127.0.0.1:8000/user/<int:id>      | PUT         | Update a user by it's id.                         | JWTAuthentication  | IsAuthenticated | Required: [username, password, first_name, last_name, email]                    |
| http://127.0.0.1:8000/user/<int:id>      | PATCH       | Update a user by it's id.                         | JWTAuthentication  | IsAuthenticated | Optional: [username, password, first_name, last_name, email]                    |
| http://127.0.0.1:8000/user/<int:id>      | DELETE      | Delete a user by it's id.                         | JWTAuthentication  | IsAuthenticated |                                                                                 |
|                                          |             |                                                   |                    |                 |                                                                                 |
| http://127.0.0.1:8000/post/              | GET         | Return all existing posts ordered by id.          | JWTAuthentication  | IsAdminUser     |                                                                                 |
| http://127.0.0.1:8000/post/create        | POST        | Create a new post.                                | JWTAuthentication  | IsAuthenticated | Required: [title, body]                                                         |
| http://127.0.0.1:8000/post/<slug:slug>   | GET         | Return a post by it's slug.                       | JWTAuthentication  | IsAuthenticated |                                                                                 |
| http://127.0.0.1:8000/post/<slug:slug>   | PUT         | Update a post by it's slug.                       | JWTAuthentication  | IsAuthenticated | Required: [title, body]                                                         |
| http://127.0.0.1:8000/post/<slug:slug>   | PATCH       | Update a post by it's slug.                       | JWTAuthentication  | IsAuthenticated | Optional: [title, body]                                                         |
| http://127.0.0.1:8000/post/<slug:slug>   | DELETE      | Delete a post by it's slug.                       | JWTAuthentication  | IsAuthenticated |                                                                                 |

