import asyncio
from quart import Quart, render_template, request, session

app = Quart(__name__)
app.secret_key = 'your_generated_secret_key'  # Replace with a secure secret key


# Asynchronous function to generate a response using the ALIENTELLIGENCE model
async def generate_response(character, user_input):
    # Template for ALIENTELLIGENCE model without unsupported flags
    prompt = f"You are {character} from My Hero Academia. Respond to this message: '{user_input}'"

    # Run the model asynchronously
    try:
        process = await asyncio.create_subprocess_exec(
            'ollama', 'run', 'ALIENTELLIGENCE/characterconversationsimulator', prompt,
            stdout=asyncio.subprocess.PIPE
        )
        stdout, _ = await process.communicate()  # Wait for the subprocess to finish and capture output
        response = stdout.decode('utf-8').strip()
        return response
    except Exception as e:
        print(f"Error generating response: {str(e)}")
        return "Sorry, I couldn't generate a response."


# Route for character selection
@app.route('/', methods=['GET'])
async def index():
    session.clear()  # Clear the session when returning to character selection
    return await render_template('index.html')


# Route for chat interaction
@app.route('/chat', methods=['GET', 'POST'])
async def chat():
    # Handle character selection (GET request)
    if request.method == 'GET':
        character = request.args.get('character', '')  # Get the selected character from query string
        session['character'] = character  # Store selected character in session
        session['conversation'] = []  # Initialize conversation history in session
        return await render_template('chat.html', character=character, conversation=[])

    # Handle message submission (POST request)
    if request.method == 'POST':
        # Await the form data retrieval
        user_input = (await request.form)['user_input']  # Get the user's message

        character = session.get('character', '')  # Get character from session

        # Generate response from the ALIENTELLIGENCE model asynchronously
        response = await generate_response(character, user_input)

        # Log the conversation (both user input and response)
        conversation = session.get('conversation', [])
        conversation.append({'user': user_input, 'response': response})
        session['conversation'] = conversation  # Save updated conversation in session

        # Render the chat page with the updated conversation
        return await render_template('chat.html', character=character, conversation=conversation)


if __name__ == '__main__':
    app.run(debug=True)
