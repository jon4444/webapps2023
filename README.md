# Webapps2023- Django Project

## Overview

This project aims to create an online payment system that allows users to transfer money between their online accounts. Unlike traditional online payment services, the assumption is made that users do not have any bank account connections and start with a fixed amount of money upon registration. 

To register, users are required to provide their basic information such as username, first and last name, email address, and password. Users can select their account currency during registration, and the system will automatically make the appropriate conversion to assign the right initial amount of money.
Users can make direct payments to other registered users and can also request payments from other users. The system facilitates these transactions within a single Django transaction, and users can check for notifications regarding payments and requests in their accounts. 

Users can access all their transactions, including sent and received payments and requests for payments, as well as their current account balance.
The system administrator has access to all user accounts and transactions. In addition, the project requires a separate RESTful web service to implement currency conversion, with exchange rates being statically assigned and hard-coded in the source code.

Overall, this project aims to provide a simple and efficient online payment system for users, with the ability to track transactions and account balances. The use of Django and a RESTful web service for currency conversion ensures scalability and modularity for future development.

## Usage 

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
OR
python manage.py runserver_plus --cert-file domain_name.crt --key-file domain_name.key
PEM passphrase: webapps
```
