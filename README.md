

| **Endpoint**                             | **Request** | **Definition**                                    | **Authentication** | **Permission**  | **In data**                                                                     |
|------------------------------------------|-------------|---------------------------------------------------|--------------------|-----------------|---------------------------------------------------------------------------------|
| auth/token         | POST        | Return an access and refresh JSON web token pair. | -                  | -               | Required: [username, password]                                                  |
| auth/token/refresh | POST        | Return an access type JSON web token.             | -                  | -               | Required: [refresh]                                                             |
|                                          |             |                                                   |                    |                 |                                                                                 |
| user/              | GET         | Return all existing users ordered by id.          | JWTAuthentication  | IsAdminUser     |                                                                                 |
| user/register      | POST        | Create a new user.                                | -                  | AllowAny        | Required: [username, password]  <br /> Optional: [first_name, last_name, email] |
| user/<int:id>      | GET         | Return a user by it's id.                         | JWTAuthentication  | IsAuthenticated |                                                                                 |
| user/<int:id>      | PUT         | Update a user by it's id.                         | JWTAuthentication  | IsAuthenticated | Required: [username, password, first_name, last_name, email]                    |
| user/<int:id>      | PATCH       | Update a user by it's id.                         | JWTAuthentication  | IsAuthenticated | Optional: [username, password, first_name, last_name, email]                    |
| user/<int:id>      | DELETE      | Delete a user by it's id.                         | JWTAuthentication  | IsAuthenticated |                                                                                 |
|                                          |             |                                                   |                    |                 |                                                                                 |
| post/              | GET         | Return all existing posts ordered by id.          | JWTAuthentication  | IsAdminUser     |                                                                                 |
| post/create        | POST        | Create a new post.                                | JWTAuthentication  | IsAuthenticated | Required: [title, body]                                                         |
| post/<slug:slug>   | GET         | Return a post by it's slug.                       | JWTAuthentication  | IsAuthenticated |                                                                                 |
| post/<slug:slug>   | PUT         | Update a post by it's slug.                       | JWTAuthentication  | IsAuthenticated | Required: [title, body]                                                         |
| post/<slug:slug>   | PATCH       | Update a post by it's slug.                       | JWTAuthentication  | IsAuthenticated | Optional: [title, body]                                                         |
| post/<slug:slug>   | DELETE      | Delete a post by it's slug.                       | JWTAuthentication  | IsAuthenticated |                                                                                 |

