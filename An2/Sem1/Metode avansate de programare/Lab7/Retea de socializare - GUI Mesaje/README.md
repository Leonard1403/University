# Java Project with JavaFX UI

**Description**  
This project includes a graphical interface for signing in (authentication). The client logs in with data stored in a database. If the client does not have an account, they can create a new one by clicking the "sign-in" button, entering their data, and then saving the new client to the database. Later, the client can connect to the database.

![Sign-In Screen 1](https://github.com/Leonard1403/University/blob/master/An2/Sem1/Metode%20avansate%20de%20programare/Lab7/1.png)
![Sign-In Screen 2](https://github.com/Leonard1403/University/blob/master/An2/Sem1/Metode%20avansate%20de%20programare/Lab7/2.png)
![Sign-In Screen 3](https://github.com/Leonard1403/University/blob/master/An2/Sem1/Metode%20avansate%20de%20programare/Lab7/3.png)

---

## Features

- **User Search**: A client can look up other users in the application’s user list.  
- **Friendship Management**: Clients can delete a friendship or accept a received friendship request.  
- **Real-Time Updates**: An observer monitors all users connected to the platform, so any change (in one window) is immediately reflected across all the other windows.  
- **Messaging**: Users can communicate with each other via a chatbox.

![Friend Management](https://github.com/Leonard1403/University/blob/master/An2/Sem1/Metode%20avansate%20de%20programare/Lab7/4.png)
![Chatbox Example](https://github.com/Leonard1403/University/blob/master/An2/Sem1/Metode%20avansate%20de%20programare/Lab7/6.png)

---

## Architecture

Below is the multi-layer (MVC) structure used in the project:

![MVC Architecture](https://github.com/Leonard1403/University/blob/master/An2/Sem1/Metode%20avansate%20de%20programare/Lab7/7.png)

This design separates the logic into **Model**, **View**, and **Controller** layers, making the application modular and easier to maintain.
