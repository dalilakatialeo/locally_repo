#Locally
---

![locally-logo](https://user-images.githubusercontent.com/79177865/134760415-4ea74c9f-c274-4a30-9ee4-1f11843ac269.jpg)

A crowdfunding app created with Django Rest Framework (and React).
Filtering by location, users can view and donate to projects that matter to them and their community directly.

*Disclaimer: only Brisbane suburbs are currently supported.*

Deployed on [Heroku](https://locally-crowdfunding.herokuapp.com/projects).

---

### Stack

##### Backend
* Python
    * Django
    * Django Rest Framework (DRF)

##### Frontend
* Javascript
    * React


##### Tools
* VSCode
* Insomnia

---

## GET methods

#### GET all users

![image](https://user-images.githubusercontent.com/79177865/134761535-251d1eac-fc8b-4b48-92c2-b0014ae3cd2a.png)


#### GET user by ID

![image](https://user-images.githubusercontent.com/79177865/134761662-b3654081-3de3-42fd-b23d-42c2f62e05c4.png)

#### GET all projects

![image](https://user-images.githubusercontent.com/79177865/134761787-27b938fc-8d02-4be6-8b0a-80fb7a57733e.png)


#### GET project by ID

![image](https://user-images.githubusercontent.com/79177865/134761807-99e35265-2257-4230-b53b-524c87cee2a5.png)


#### GET all donations

![image](https://user-images.githubusercontent.com/79177865/134761729-a7f6617f-fa65-40b7-a13f-4f4dc7f4d60d.png)


#### GET donation by ID

![image](https://user-images.githubusercontent.com/79177865/134761758-f1f8f2a6-98a8-42eb-b339-93a3e8017b84.png)


## POST methods

#### POST users

![image](https://user-images.githubusercontent.com/79177865/134761886-08d87552-874b-4a01-8dc6-62942449f1db.png)


#### POST projects

![image](https://user-images.githubusercontent.com/79177865/134761937-82c011bc-cc62-43f5-985e-928a474915d3.png)

#### POST donations

![image](https://user-images.githubusercontent.com/79177865/134761982-dd4561e4-44b5-4b81-ae81-b128c6488ef6.png)


## PUT methods

#### PUT users

![image](https://user-images.githubusercontent.com/79177865/134762339-3d7c07c9-e7e1-46b5-96d6-92900f79f045.png)

#### PUT projects

![image](https://user-images.githubusercontent.com/79177865/134762381-11a329c8-0308-49a2-aa68-7af9d9d91417.png)

## DELETE methods

#### DELETE users

![image](https://user-images.githubusercontent.com/79177865/134762396-d35f1929-87c6-4b15-aa0c-63dc881101f6.png)

#### DELETE projects

![image](https://user-images.githubusercontent.com/79177865/134762413-cd955c01-1ced-4160-878a-8d4f3ea45398.png)

## TOKEN creation

![image](https://user-images.githubusercontent.com/79177865/134762005-d914fa8a-0dae-4f93-88d4-c9c4b2eb91f1.png)


## Step by step

#### How to register a new user

1. Navigate to the POST /users/ request
2. In the 'body' tab, select JSON
3. In the 'body' field, enter new user credentials:
    ```
    {
        "username": "username",
        "email": "email",
        "password": "password"
    }
4. Send the request and the new user is successfully created

![image](https://user-images.githubusercontent.com/79177865/134762166-1aedd269-c9f3-4fb3-be2a-ec81a0e0eff5.png)


#### How to create a new project

1. Navigate to the POST /projects/ request
2. In the 'body' tab, select JSON
3. In the 'body' field, enter new project details:
    ```
    {
	"title": "New Project",
	"description": "Another test project",
	"goal" : 5000,
    "location": "BARDON",
	"image": "https://via.placeholder.com/300.jpg",
	"is_open": true,
	"date_created": "2020-03-20T14:28:23.382748Z"
    }

4. Send the request and the new project is successfully created

![image](https://user-images.githubusercontent.com/79177865/134762308-12390796-1473-4675-86ab-2591ceb151fd.png)


## API Specification table

![image](https://user-images.githubusercontent.com/79177865/134762566-e2ef74d6-e50b-4dd8-ae77-800955536fb3.png)

## Database schema

![image](https://user-images.githubusercontent.com/79177865/134762827-7b8378d5-d54d-4a8f-8b6c-aa209a770c16.png)











