My Hero Academia Character Chat Application

This is a Flask (Quart) web application that allows users to have interactive conversations with characters from the anime My Hero Academia. The application uses the ALIENTELLIGENCE/characterconversationsimulator model from Ollama to generate character responses. Users can select a character and chat with them in a browser interface.
Features

    Select from various My Hero Academia characters to chat with.
    The model responds as the selected character based on user input.
    The conversation is logged and displayed for the user.
    Asynchronous support for improved performance and responsiveness.

Technologies Used

    Quart: An asynchronous alternative to Flask, used to build the web application and manage routes.
    Ollama: A local model that simulates character conversations.
    asyncio: For asynchronous process handling to improve response times.
    HTML/CSS: Used for building the front-end pages.

Installation
1. Clone the Repository

bash

git clone https://github.com/your-username/MHACharacterChat.git
cd MHACharacterChat

2. Set Up Virtual Environment

bash

python3 -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate

3. Install Required Packages

bash

pip install -r requirements.txt

Running the Application

    Start the Application

    bash

python app.py

Open in Browser Once the application is running, open your browser and navigate to:

arduino

    http://127.0.0.1:5000

    Select a Character Choose a character from the dropdown and start chatting with them.

Configuration

    Ollama: Make sure you have the Ollama engine installed and that the ALIENTELLIGENCE/characterconversationsimulator model is available for running locally. You can download the Ollama engine and necessary models by following the instructions on the Ollama website.

    Secret Key: The application requires a secret key for session management. You can configure it in the app.py file by replacing 'your_generated_secret_key' with a securely generated key using the secrets module in Python.

Project Structure

bash

MHACharacterChat/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── templates/          # HTML templates for the app
│   ├── index.html      # Character selection page
│   └── chat.html       # Chat interface page
└── README.md           # Documentation

Known Issues

    Response Delay: Depending on the system and the size of the model, the response time may vary. To mitigate this, the app uses asynchronous programming to improve responsiveness.

Future Enhancements

    Add more My Hero Academia characters and enhance the realism of conversations.
    Optimize the model's performance for faster responses.
    Add more features to the chat interface, like saving conversations or providing more character-specific interactions.

Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request. Suggestions and feature requests are also welcome.
License

This project is licensed under the MIT License. See the LICENSE file for details.