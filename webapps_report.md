# Candidate No: 260032

## Webapps Report

> During the development of this project, I encountered several issues with the IntelliJ IDE. I began the project with IntelliJ but later on in development, my IDE faced a lot of errors that could not be ultimately fixed. I sought help from coursemates and our T.A, Kannen Joshi, but the different errors it produced each time could not be completely fixed. As a result I had no choice but to complete the remainder of the project with different IDE to meet the deadline of the project.

---

## Introduction

This project aims to create an online payment system that allows users to transfer money between their online accounts. Unlike traditional online payment services, the assumption is made that users do not have any bank account connections and start with a fixed amount of money upon registration. To register, users are required to provide their basic information such as username, first and last name, email address, and password. Users can select their account currency during registration, and the system will automatically make the appropriate conversion to assign the right initial amount of money.

Users can make direct payments to other registered users and can also request payments from other users. The system facilitates these transactions within a single Django transaction, and users can check for notifications regarding payments and requests in their accounts. Users can access all their transactions, including sent and received payments and requests for payments, as well as their current account balance.

The system administrator has access to all user accounts and transactions. In addition, the project requires a separate RESTful web service to implement currency conversion, with exchange rates being statically assigned and hard-coded in the source code.

Overall, this project aims to provide a simple and efficient online payment system for users, with the ability to track transactions and account balances. The use of Django and a RESTful web service for currency conversion ensures scalability and modularity for future development.

---

## 1 - Presentation Layer

The application has five main functionalities. Firstly, it enables registered users to transfer money to other registered users. This core feature is the primary purpose of the application. Secondly, users can also request funds from other registered users. This feature allows users to initiate a transaction by requesting funds from another user. Thirdly, administrators have the privilege to see all the user accounts on the platform. This feature allows the admin to keep track of all users on the platform. Fourthly, the admin can also see all the transactions made between users. This feature provides an overview of all the transactions taking place on the platform, allowing the admin to monitor and ensure the integrity of the system. Finally, the admin can register new users and other admins. This feature allows the admin to manage user accounts and create new admins when needed. These functionalities are essential to ensure that the system is secure, reliable, and easy to use for all stakeholders involved.
The website can be accessed via the link: `https://127.0.0.1:8000/webapps2023/home/`

Before you can access the homepage, you will be asked to register your credentials:
![register](/templates/static/images/register.png)
*Figure 1*

Following this you can login with the details you registered with:
![login](/templates/static/images/login.png)
*Figure 2*

When the user is registered and logged in they are directed to the landing page as seen in figure 3
![landing](/templates/static/images/landing.png)
*Figure 3*

From figure 4 we can see each user's balance form the admin page

![admin view balance](/templates/static/images/admin_view_balance.png)*Figure 4*

Admin can also see each user's transfer to another user
![admin view transfer](/templates/static/images/admin_view_transfer.png)*Figure 5*

Admin can also see each user's request to another user
![admin view request](/templates/static/images/admin_view_request.png)*Figure 6*

Admin can also see all the users in the system
![admin view users](/templates/static/images/admin_view_users.png)*Figure 7*

---

## 2 - Business Logic Layer

The views layer is a critical component of this project, as it contains the code responsible for accessing the models. The views layer employs the use of the Django framework's built-in `transaction.atomic()` function to guarantee transaction atomicity. By wrapping a block of code with this function, the views layer ensures that all database operations inside the block either succeed or fail entirely as a single unit of work. This approach is vital to maintain data consistency and integrity, especially in the face of concurrent database access.

Furthermore, the views layer guarantees the ACID properties of the database. ACID properties ensure that transactions are reliable and consistent, as they provide guarantees that the database will remain in a consistent state before and after each transaction. The views layer adheres to the four ACID properties, which are: the entire transaction takes place at once, the database is consistent before and after the transaction, multiple transactions occur independently, and the changes of the successful transaction occur even when a system failure occurs.

From the figure 8 we can see the page where users can transfer money to other registered users

![transfer](/templates/static/images/transfer.png)*Figure 8*
![transfer code](/templates/static/images/transfer_code.png)*Figure 9*

After the transaction has taken place, we can see each balance for the sender and the receiever in figure 10

![view transactions](/templates/static/images/view_transactions.png)*Figure 10*

Likewise the users can also make a request to another registered user for funds and get a confirmation message, as seen in figure 11
![request](/templates/static/images/request.png)*Figure 11*
![request code](/templates/static/images/request_code.png)*Figure 12*
![request message](/templates/static/images/request_sent.png)*Figure 13*

---

## 3 - Data Access Layer

The data storage of the application is handled by the Models layer, which is responsible for managing the data and interactions with the database. In this layer, all the data models that the application uses are defined. For this project, SQLite was selected as the Relational Database Management System (RDBMS) to store the application data. SQLite is a lightweight, file-based RDBMS that offers a good balance between ease of use and functionality. The database was named `db.webapps`. This layer ensures that the data is correctly stored and retrieved from the database, and that it is presented in a format that is easy for the other layers to use.

Figure 14 is the database table for the user balances:
![balance_table](/templates/static/images/balance_table.png)*Figure 14*

The database table for user transfers:
![transfer_table](/templates/static/images/transfer_table.png)*Figure 15*

The database table for user requests:
![request_table](/templates/static/images/request_table.png)*Figure 15*

---

## 4 - Security Layer

User registration, login, and logout are essential functionalities in the system, and access is restricted to authorized users only, i.e., registered users and administrators.

To ensure secure data transmission between the client and server, the web application is accessed via HTTPS, which encrypts all data. Protection against cross-site request forgery (CSRF) is also implemented to prevent malicious users from executing unauthorized actions on behalf of a legitimate user.
The certificate can be seen in figure 16:
![view_certificate](/templates/static/images/view_certificate.png)*Figure 16*

The system has a registered admin account with the credentials *username: admin1, password:admin1.* This account is used by the administrator to perform tasks such as managing user accounts, monitoring transactions, and registering new administrators.

---

## 5 - Web Services

The project implemented a REST service that can be accessed by the business logic layer. The RESTful web service is designed to respond only to GET requests, with the resource having the name `conversion` in the path.

![conversion](/templates/static/images/currency_conversion.png)*Figure 17*

The RESTful service returns `USD` to `EUR` conversion rate as an HTTP response with status code `200`.
The URL can be accessed via: `https://127.0.0.1:8000/conversion/?base_currency=USD&target_currency=EUR&amount=100`.
