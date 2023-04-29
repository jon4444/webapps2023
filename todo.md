## Implementation Todo list

Users should:
- view all transactions
- make direct payments 
- request payments from registered users
- change the database name 

### Security Layer (25%)
Users should:
- Authentication functionality (i.e., registration, login, and logout)
- Access control to restrict access to web pages to non-authorised users
- Communication on top of HTTPS for every interaction with users and admins
Cross-site scripting (XSS), Cross-site request forgery (CSRF), SQL injection, and Clickjacking protection

### Web Services (10%)
- A currency conversion RESTful web service that responds only to GET requests. The exported resource should be named conversion in a path such as the following:
```
baseURL/conversion/{currency1}/{currency2}/{amount_of_currency1}
```
- The RESTful web service should return an HTTP response with the conversion rate (currency1 to currency2) or the appropriate HTTP status code if one or both of the provided currencies are not supported.